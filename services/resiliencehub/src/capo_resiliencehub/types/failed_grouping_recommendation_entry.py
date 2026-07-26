"""Generated from Smithy shape ``com.amazonaws.resiliencehub#FailedGroupingRecommendationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.error_message
    import capo_resiliencehub.types.string255


class FailedGroupingRecommendationEntry(TypedDict, closed=True):
    grouping_recommendation_id: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates the identifier of the grouping recommendation.</p>"""
    error_message: "capo_resiliencehub.types.error_message.ErrorMessage"
    """<p>Indicates the error that occurred while implementing a grouping recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedGroupingRecommendationEntry) -> dict:
    out: dict = {}
    out["groupingRecommendationId"] = value["grouping_recommendation_id"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedGroupingRecommendationEntry:
    out: FailedGroupingRecommendationEntry = {}  # type: ignore[typeddict-item]
    if "groupingRecommendationId" in data:
        out["grouping_recommendation_id"] = data["groupingRecommendationId"]
    else:
        raise DeserializationError(
            "FailedGroupingRecommendationEntry.grouping_recommendation_id required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError(
            "FailedGroupingRecommendationEntry.error_message required"
        )
    return out
