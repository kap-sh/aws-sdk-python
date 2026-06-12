"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class Recommendation(TypedDict):
    recommendation_text: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>Text of the recommendations that are provided to make an application more recovery resilient.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    if "recommendation_text" in value:
        out["recommendationText"] = value["recommendation_text"]
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "recommendationText" in data:
        out["recommendation_text"] = data["recommendationText"]
    return out
