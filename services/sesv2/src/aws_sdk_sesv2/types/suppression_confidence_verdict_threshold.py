"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionConfidenceVerdictThreshold``."""

from typing import Literal, TypeAlias, cast

"""<p>The confidence level threshold for suppression validation:</p> <ul> <li> <p> <code>MEDIUM</code> – Allows emails to be sent to addresses with medium or high delivery likelihood.</p> </li> <li> <p> <code>HIGH</code> – Allows emails to be sent only to addresses with high delivery likelihood.</p> </li> <li> <p> <code>MANAGED</code> – Managed confidence threshold where Amazon SES automatically determines the appropriate level.</p> </li> </ul>"""
SuppressionConfidenceVerdictThreshold: TypeAlias = Literal[
    "MEDIUM",
    "HIGH",
    "MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionConfidenceVerdictThreshold) -> str:
    return value


def deserialize_json(data: str) -> SuppressionConfidenceVerdictThreshold:
    return cast(SuppressionConfidenceVerdictThreshold, data)
