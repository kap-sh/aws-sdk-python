"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.open_search_application_endpoint
    import capo_cloudwatch_logs.types.open_search_application_id
    import capo_cloudwatch_logs.types.open_search_resource_status


class OpenSearchApplication(TypedDict, closed=True):
    application_endpoint: NotRequired[
        "capo_cloudwatch_logs.types.open_search_application_endpoint.OpenSearchApplicationEndpoint"
    ]
    """<p>The endpoint of the application.</p>"""
    application_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    application_id: NotRequired[
        "capo_cloudwatch_logs.types.open_search_application_id.OpenSearchApplicationId"
    ]
    """<p>The ID of the application.</p>"""
    status: NotRequired[
        "capo_cloudwatch_logs.types.open_search_resource_status.OpenSearchResourceStatus"
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
        import capo_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            capo_cloudwatch_logs.types.open_search_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchApplication:
    out: OpenSearchApplication = {}  # type: ignore[typeddict-item]
    if data.get("applicationEndpoint") is not None:
        out["application_endpoint"] = data["applicationEndpoint"]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("status") is not None:
        import capo_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            capo_cloudwatch_logs.types.open_search_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
