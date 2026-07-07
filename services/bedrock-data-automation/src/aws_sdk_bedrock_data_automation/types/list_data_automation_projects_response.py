"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationProjectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_project_summaries
    import aws_sdk_bedrock_data_automation.types.next_token


class ListDataAutomationProjectsResponse(TypedDict, closed=True):
    projects: "aws_sdk_bedrock_data_automation.types.data_automation_project_summaries.DataAutomationProjectSummaries"
    next_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationProjectsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.data_automation_project_summaries

    out["projects"] = (
        aws_sdk_bedrock_data_automation.types.data_automation_project_summaries.serialize_json(
            value["projects"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAutomationProjectsResponse:
    out: ListDataAutomationProjectsResponse = {}  # type: ignore[typeddict-item]
    if "projects" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_summaries

        out["projects"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_summaries.deserialize_json(
                data["projects"]
            )
        )
    else:
        raise DeserializationError(
            "ListDataAutomationProjectsResponse.projects required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
