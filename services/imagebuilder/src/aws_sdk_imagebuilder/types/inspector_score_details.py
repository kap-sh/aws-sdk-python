"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InspectorScoreDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.cvss_score_details


class InspectorScoreDetails(TypedDict):
    adjusted_cvss: NotRequired[
        "aws_sdk_imagebuilder.types.cvss_score_details.CvssScoreDetails"
    ]
    """<p>An object that contains details about an adjustment that Amazon Inspector made to the CVSS score for the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InspectorScoreDetails) -> dict:
    out: dict = {}
    if "adjusted_cvss" in value:
        import aws_sdk_imagebuilder.types.cvss_score_details

        out["adjustedCvss"] = (
            aws_sdk_imagebuilder.types.cvss_score_details.serialize_json(
                value["adjusted_cvss"]
            )
        )
    return out


def deserialize_json(data: dict) -> InspectorScoreDetails:
    out: InspectorScoreDetails = {}  # type: ignore[typeddict-item]
    if "adjustedCvss" in data:
        import aws_sdk_imagebuilder.types.cvss_score_details

        out["adjusted_cvss"] = (
            aws_sdk_imagebuilder.types.cvss_score_details.deserialize_json(
                data["adjustedCvss"]
            )
        )
    return out
