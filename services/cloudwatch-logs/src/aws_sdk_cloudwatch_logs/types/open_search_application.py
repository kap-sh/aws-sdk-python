"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchApplication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.open_search_application_endpoint
    import aws_sdk_cloudwatch_logs.types.open_search_application_id
    import aws_sdk_cloudwatch_logs.types.open_search_resource_status


class OpenSearchApplication(TypedDict):
    application_endpoint: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_application_endpoint.OpenSearchApplicationEndpoint"
    ]
    """<p>The endpoint of the application.</p>"""
    application_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    application_id: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_application_id.OpenSearchApplicationId"
    ]
    """<p>The ID of the application.</p>"""
    status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_resource_status.OpenSearchResourceStatus"
    ]
    """<p>This structure contains information about the status of this OpenSearch Service resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchApplication) -> dict:
    out: dict = {}
    if "application_endpoint" in value:
        out["applicationEndpoint"] = value["application_endpoint"]
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "status" in value:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchApplication:
    out: OpenSearchApplication = {}  # type: ignore[typeddict-item]
    if "applicationEndpoint" in data:
        out["application_endpoint"] = data["applicationEndpoint"]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
