"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeResourceGroupingRecommendationTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.resources_grouping_rec_gen_status_type
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.string500


class DescribeResourceGroupingRecommendationTaskResponse(TypedDict, closed=True):
    grouping_id: "capo_resiliencehub.types.string255.String255"
    """<p>Identifier of the grouping recommendation task.</p>"""
    status: "capo_resiliencehub.types.resources_grouping_rec_gen_status_type.ResourcesGroupingRecGenStatusType"
    """<p>Status of the action.</p>"""
    error_message: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Error that occurred while generating a grouping recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourceGroupingRecommendationTaskResponse) -> dict:
    out: dict = {}
    out["groupingId"] = value["grouping_id"]
    import capo_resiliencehub.types.resources_grouping_rec_gen_status_type

    out["status"] = (
        capo_resiliencehub.types.resources_grouping_rec_gen_status_type.serialize_json(
            value["status"]
        )
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> DescribeResourceGroupingRecommendationTaskResponse:
    out: DescribeResourceGroupingRecommendationTaskResponse = {}  # type: ignore[typeddict-item]
    if "groupingId" in data:
        out["grouping_id"] = data["groupingId"]
    else:
        raise DeserializationError(
            "DescribeResourceGroupingRecommendationTaskResponse.grouping_id required"
        )
    if "status" in data:
        import capo_resiliencehub.types.resources_grouping_rec_gen_status_type

        out["status"] = (
            capo_resiliencehub.types.resources_grouping_rec_gen_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeResourceGroupingRecommendationTaskResponse.status required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
