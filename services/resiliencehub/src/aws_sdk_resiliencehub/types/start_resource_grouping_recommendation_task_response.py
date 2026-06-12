"""Generated from Smithy shape ``com.amazonaws.resiliencehub#StartResourceGroupingRecommendationTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.resources_grouping_rec_gen_status_type
    import aws_sdk_resiliencehub.types.string255
    import aws_sdk_resiliencehub.types.string500


class StartResourceGroupingRecommendationTaskResponse(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    grouping_id: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Identifier of the grouping recommendation task.</p>"""
    status: "aws_sdk_resiliencehub.types.resources_grouping_rec_gen_status_type.ResourcesGroupingRecGenStatusType"
    """<p>Status of the action.</p>"""
    error_message: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>Error that occurred while executing a grouping recommendation task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartResourceGroupingRecommendationTaskResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
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


def deserialize_json(data: dict) -> StartResourceGroupingRecommendationTaskResponse:
    out: StartResourceGroupingRecommendationTaskResponse = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "StartResourceGroupingRecommendationTaskResponse.app_arn required"
        )
    if "groupingId" in data:
        out["grouping_id"] = data["groupingId"]
    else:
        raise DeserializationError(
            "StartResourceGroupingRecommendationTaskResponse.grouping_id required"
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
            "StartResourceGroupingRecommendationTaskResponse.status required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
