"""Generated from Smithy shape ``com.amazonaws.inspector2#Remediation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.recommendation


class Remediation(TypedDict, closed=True):
    recommendation: NotRequired[
        "aws_sdk_inspector2.types.recommendation.Recommendation"
    ]
    """<p>An object that contains information about the recommended course of action to remediate the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Remediation) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import aws_sdk_inspector2.types.recommendation

        out["recommendation"] = aws_sdk_inspector2.types.recommendation.serialize_json(
            value["recommendation"]
        )
    return out


def deserialize_json(data: dict) -> Remediation:
    out: Remediation = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import aws_sdk_inspector2.types.recommendation

        out["recommendation"] = (
            aws_sdk_inspector2.types.recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    return out
