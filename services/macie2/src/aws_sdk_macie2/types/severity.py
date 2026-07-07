"""Generated from Smithy shape ``com.amazonaws.macie2#Severity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.severity_description


class Severity(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_macie2.types.severity_description.SeverityDescription"
    ]
    """<p>The qualitative representation of the finding's severity, ranging from Low (least severe) to High (most severe).</p>"""
    score: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The numerical representation of the finding's severity, ranging from 1 (least severe) to 3 (most severe).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Severity) -> dict:
    out: dict = {}
    if "description" in value:
        import aws_sdk_macie2.types.severity_description

        out["description"] = aws_sdk_macie2.types.severity_description.serialize_json(
            value["description"]
        )
    if "score" in value:
        out["score"] = value["score"]
    return out


def deserialize_json(data: dict) -> Severity:
    out: Severity = {}  # type: ignore[typeddict-item]
    if "description" in data:
        import aws_sdk_macie2.types.severity_description

        out["description"] = aws_sdk_macie2.types.severity_description.deserialize_json(
            data["description"]
        )
    if "score" in data:
        out["score"] = data["score"]
    return out
