"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ListApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_name
    import aws_sdk_kinesis_analytics.types.list_applications_input_limit


class ListApplicationsRequest(TypedDict):
    limit: NotRequired[
        "aws_sdk_kinesis_analytics.types.list_applications_input_limit.ListApplicationsInputLimit"
    ]
    """<p>Maximum number of applications to list.</p>"""
    exclusive_start_application_name: NotRequired[
        "aws_sdk_kinesis_analytics.types.application_name.ApplicationName"
    ]
    """<p>Name of the application to start the list with. When using pagination to retrieve the list, you don't need to specify this parameter in the first request. However, in subsequent requests, you add the last application name from the previous response to get the next page of applications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "exclusive_start_application_name" in value:
        out["ExclusiveStartApplicationName"] = value["exclusive_start_application_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "ExclusiveStartApplicationName" in data:
        out["exclusive_start_application_name"] = data["ExclusiveStartApplicationName"]
    return out
