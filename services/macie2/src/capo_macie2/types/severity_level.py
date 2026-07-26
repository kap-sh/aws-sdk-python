"""Generated from Smithy shape ``com.amazonaws.macie2#SeverityLevel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__long
    import capo_macie2.types.data_identifier_severity


class SeverityLevel(TypedDict, closed=True):
    occurrences_threshold: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The minimum number of occurrences of text that must match the custom data identifier's detection criteria in order to produce a finding with the specified severity (severity).</p>"""
    severity: NotRequired[
        "capo_macie2.types.data_identifier_severity.DataIdentifierSeverity"
    ]
    """<p>The severity to assign to a finding: if the number of occurrences is greater than or equal to the specified threshold (occurrencesThreshold); and, if applicable, the number of occurrences is less than the threshold for the next consecutive severity level for the custom data identifier, moving from LOW to HIGH.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeverityLevel) -> dict:
    out: dict = {}
    if "occurrences_threshold" in value:
        out["occurrencesThreshold"] = value["occurrences_threshold"]
    if "severity" in value:
        import capo_macie2.types.data_identifier_severity

        out["severity"] = capo_macie2.types.data_identifier_severity.serialize_json(
            value["severity"]
        )
    return out


def deserialize_json(data: dict) -> SeverityLevel:
    out: SeverityLevel = {}  # type: ignore[typeddict-item]
    if "occurrencesThreshold" in data:
        out["occurrences_threshold"] = data["occurrencesThreshold"]
    if "severity" in data:
        import capo_macie2.types.data_identifier_severity

        out["severity"] = capo_macie2.types.data_identifier_severity.deserialize_json(
            data["severity"]
        )
    return out
