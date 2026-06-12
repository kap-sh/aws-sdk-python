"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeResourceGroupingRecommendationTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.resources_grouping_rec_gen_status_type
    import aws_sdk_resiliencehub.types.string255
    import aws_sdk_resiliencehub.types.string500


class DescribeResourceGroupingRecommendationTaskResponse(TypedDict):
    grouping_id: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Identifier of the grouping recommendation task.</p>"""
    status: "aws_sdk_resiliencehub.types.resources_grouping_rec_gen_status_type.ResourcesGroupingRecGenStatusType"
    """<p>Status of the action.</p>"""
    error_message: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>Error that occurred while generating a grouping recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourceGroupingRecommendationTaskResponse) -> dict:
    out: dict = {}
    out["groupingId"] = value["grouping_id"]
    import aws_sdk_resiliencehub.types.resources_grouping_rec_gen_status_type

    out["status"] = (
        aws_sdk_resiliencehub.types.resources_grouping_rec_gen_status_type.serialize_json(
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
        import aws_sdk_resiliencehub.types.resources_grouping_rec_gen_status_type

        out["status"] = (
            aws_sdk_resiliencehub.types.resources_grouping_rec_gen_status_type.deserialize_json(
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
