"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Remediation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.remediation_recommendation


class Remediation(TypedDict, closed=True):
    recommendation: NotRequired[
        "capo_imagebuilder.types.remediation_recommendation.RemediationRecommendation"
    ]
    """<p>An object that contains information about the recommended course of action to remediate the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Remediation) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import capo_imagebuilder.types.remediation_recommendation

        out["recommendation"] = (
            capo_imagebuilder.types.remediation_recommendation.serialize_json(
                value["recommendation"]
            )
        )
    return out


def deserialize_json(data: dict) -> Remediation:
    out: Remediation = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import capo_imagebuilder.types.remediation_recommendation

        out["recommendation"] = (
            capo_imagebuilder.types.remediation_recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    return out
