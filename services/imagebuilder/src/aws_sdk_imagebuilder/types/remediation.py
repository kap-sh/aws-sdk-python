"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Remediation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.remediation_recommendation


class Remediation(TypedDict):
    recommendation: NotRequired[
        "aws_sdk_imagebuilder.types.remediation_recommendation.RemediationRecommendation"
    ]
    """<p>An object that contains information about the recommended course of action to remediate the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Remediation) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import aws_sdk_imagebuilder.types.remediation_recommendation

        out["recommendation"] = (
            aws_sdk_imagebuilder.types.remediation_recommendation.serialize_json(
                value["recommendation"]
            )
        )
    return out


def deserialize_json(data: dict) -> Remediation:
    out: Remediation = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import aws_sdk_imagebuilder.types.remediation_recommendation

        out["recommendation"] = (
            aws_sdk_imagebuilder.types.remediation_recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    return out
