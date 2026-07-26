"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationLibrariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_project_filter
    import capo_bedrock_data_automation.types.max_results
    import capo_bedrock_data_automation.types.next_token


class ListDataAutomationLibrariesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_bedrock_data_automation.types.max_results.MaxResults"
    ]
    next_token: NotRequired["capo_bedrock_data_automation.types.next_token.NextToken"]
    project_filter: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationLibrariesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "project_filter" in value:
        import capo_bedrock_data_automation.types.data_automation_project_filter

        out["projectFilter"] = (
            capo_bedrock_data_automation.types.data_automation_project_filter.serialize_json(
                value["project_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDataAutomationLibrariesRequest:
    out: ListDataAutomationLibrariesRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "projectFilter" in data:
        import capo_bedrock_data_automation.types.data_automation_project_filter

        out["project_filter"] = (
            capo_bedrock_data_automation.types.data_automation_project_filter.deserialize_json(
                data["projectFilter"]
            )
        )
    return out
