"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RejectGroupingRecommendationEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.grouping_recommendation_rejection_reason
    import aws_sdk_resiliencehub.types.string255


class RejectGroupingRecommendationEntry(TypedDict):
    grouping_recommendation_id: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Indicates the identifier of the grouping recommendation.</p>"""
    rejection_reason: NotRequired[
        "aws_sdk_resiliencehub.types.grouping_recommendation_rejection_reason.GroupingRecommendationRejectionReason"
    ]
    """<p>Indicates the reason you had selected while rejecting a grouping recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectGroupingRecommendationEntry) -> dict:
    out: dict = {}
    out["groupingRecommendationId"] = value["grouping_recommendation_id"]
    if "rejection_reason" in value:
        import aws_sdk_resiliencehub.types.grouping_recommendation_rejection_reason

        out["rejectionReason"] = (
            aws_sdk_resiliencehub.types.grouping_recommendation_rejection_reason.serialize_json(
                value["rejection_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> RejectGroupingRecommendationEntry:
    out: RejectGroupingRecommendationEntry = {}  # type: ignore[typeddict-item]
    if "groupingRecommendationId" in data:
        out["grouping_recommendation_id"] = data["groupingRecommendationId"]
    else:
        raise DeserializationError(
            "RejectGroupingRecommendationEntry.grouping_recommendation_id required"
        )
    if "rejectionReason" in data:
        import aws_sdk_resiliencehub.types.grouping_recommendation_rejection_reason

        out["rejection_reason"] = (
            aws_sdk_resiliencehub.types.grouping_recommendation_rejection_reason.deserialize_json(
                data["rejectionReason"]
            )
        )
    return out
