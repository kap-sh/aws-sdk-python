"""Generated from Smithy shape ``com.amazonaws.bedrock#RoutingCriteria``."""

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError


class RoutingCriteria(TypedDict, closed=True):
    response_quality_difference: "float"
    """<p>The criteria's response quality difference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingCriteria) -> dict:
    out: dict = {}
    out["responseQualityDifference"] = value["response_quality_difference"]
    return out


def deserialize_json(data: dict) -> RoutingCriteria:
    out: RoutingCriteria = {}  # type: ignore[typeddict-item]
    if "responseQualityDifference" in data:
        out["response_quality_difference"] = data["responseQualityDifference"]
    else:
        raise DeserializationError(
            "RoutingCriteria.response_quality_difference required"
        )
    return out
