"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationLibraryIngestionJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn
    import aws_sdk_bedrock_data_automation.types.max_results
    import aws_sdk_bedrock_data_automation.types.next_token


class ListDataAutomationLibraryIngestionJobsRequest(TypedDict):
    library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    """ARN generated at the server side when a DataAutomationLibrary is created"""
    max_results: NotRequired[
        "aws_sdk_bedrock_data_automation.types.max_results.MaxResults"
    ]
    next_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
    ]
    """Pagination token for retrieving the next set of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationLibraryIngestionJobsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAutomationLibraryIngestionJobsRequest:
    out: ListDataAutomationLibraryIngestionJobsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
