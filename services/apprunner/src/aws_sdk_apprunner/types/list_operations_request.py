"""Generated from Smithy shape ``com.amazonaws.apprunner#ListOperationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.list_operations_max_results
    import aws_sdk_apprunner.types.string


class ListOperationsRequest(TypedDict):
    service_arn: "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service that you want a list of operations for.</p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>"""
    max_results: NotRequired[
        "aws_sdk_apprunner.types.list_operations_max_results.ListOperationsMaxResults"
    ]
    """<p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOperationsRequest) -> dict:
    out: dict = {}
    out["ServiceArn"] = value["service_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOperationsRequest:
    out: ListOperationsRequest = {}  # type: ignore[typeddict-item]
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    else:
        raise DeserializationError("ListOperationsRequest.service_arn required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
