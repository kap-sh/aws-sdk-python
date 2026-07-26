"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AcceptGroupingRecommendationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.string255


class AcceptGroupingRecommendationEntry(TypedDict, closed=True):
    grouping_recommendation_id: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates the identifier of the grouping recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptGroupingRecommendationEntry) -> dict:
    out: dict = {}
    out["groupingRecommendationId"] = value["grouping_recommendation_id"]
    return out


def deserialize_json(data: dict) -> AcceptGroupingRecommendationEntry:
    out: AcceptGroupingRecommendationEntry = {}  # type: ignore[typeddict-item]
    if "groupingRecommendationId" in data:
        out["grouping_recommendation_id"] = data["groupingRecommendationId"]
    else:
        raise DeserializationError(
            "AcceptGroupingRecommendationEntry.grouping_recommendation_id required"
        )
    return out
