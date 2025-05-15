import re
from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification

class DecimalMismatchDetector(AbstractDetector):
    """
    Detects hardcoded power-of-ten expressions instead of token.decimals()
    """
    ARGUMENT = 'decimal-mismatch'
    HELP = 'Flag hardcoded decimal scale mismatches'
    IMPACT = DetectorClassification.MEDIUM
    CONFIDENCE = DetectorClassification.HIGH

    # ───── Required wiki attributes ─────
    WIKI = 'decimal-mismatch'
    WIKI_TITLE = 'Decimal Mismatch'
    WIKI_DESCRIPTION = 'Hardcoded power-of-ten without using token.decimals()'
    WIKI_EXPLOIT_SCENARIO = (
        'If token.decimals() is not used, amount calculations may suffer precision loss.'
    )
    WIKI_RECOMMENDATION = (
        'Always call token.decimals() for correct decimal scale or avoid hardcoded exponent math.'
    )
    # ─────────────────────────────────────

    def _detect(self):
        findings = []
        for contract in self.compilation_unit.contracts:
            for function in contract.functions:
                for node in function.nodes:
                    # retrieve code snippet via source mapping
                    mapping = node.source_mapping
                    if mapping is None:
                        continue
                    source = mapping.content
                    # crude pattern: any power operator with numeric literal
                    if '**' in source and re.search(r'\*\*\s*\d+', source):
                        description = (
                            f"Hardcoded power-of-ten in {contract.name}.{function.name}: {source.strip()}"
                        )
                        findings.append(self.generate_result([description]))
        return findings

# If using as a plugin package, include a factory:

def make_plugin():
    return DecimalMismatchDetector()
