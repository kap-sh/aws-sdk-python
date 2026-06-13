"""Generated from Smithy shape ``com.amazonaws.wisdom#QueryRecommendationTriggerData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.query_text


class QueryRecommendationTriggerData(TypedDict):
    text: NotRequired["aws_sdk_wisdom.types.query_text.QueryText"]
    """<p>The text associated with the recommendation trigger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryRecommendationTriggerData) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> QueryRecommendationTriggerData:
    out: QueryRecommendationTriggerData = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    return out
