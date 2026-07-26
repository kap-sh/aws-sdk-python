"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationProjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_filter
    import capo_bedrock_data_automation.types.data_automation_library_filter
    import capo_bedrock_data_automation.types.data_automation_project_stage_filter
    import capo_bedrock_data_automation.types.max_results
    import capo_bedrock_data_automation.types.next_token
    import capo_bedrock_data_automation.types.resource_owner


class ListDataAutomationProjectsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_bedrock_data_automation.types.max_results.MaxResults"
    ]
    next_token: NotRequired["capo_bedrock_data_automation.types.next_token.NextToken"]
    project_stage_filter: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_stage_filter.DataAutomationProjectStageFilter"
    ]
    blueprint_filter: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_filter.BlueprintFilter"
    ]
    resource_owner: NotRequired[
        "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
    ]
    library_filter: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_filter.DataAutomationLibraryFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationProjectsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "project_stage_filter" in value:
        import capo_bedrock_data_automation.types.data_automation_project_stage_filter

        out["projectStageFilter"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage_filter.serialize_json(
                value["project_stage_filter"]
            )
        )
    if "blueprint_filter" in value:
        import capo_bedrock_data_automation.types.blueprint_filter

        out["blueprintFilter"] = (
            capo_bedrock_data_automation.types.blueprint_filter.serialize_json(
                value["blueprint_filter"]
            )
        )
    if "resource_owner" in value:
        import capo_bedrock_data_automation.types.resource_owner

        out["resourceOwner"] = (
            capo_bedrock_data_automation.types.resource_owner.serialize_json(
                value["resource_owner"]
            )
        )
    if "library_filter" in value:
        import capo_bedrock_data_automation.types.data_automation_library_filter

        out["libraryFilter"] = (
            capo_bedrock_data_automation.types.data_automation_library_filter.serialize_json(
                value["library_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDataAutomationProjectsRequest:
    out: ListDataAutomationProjectsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "projectStageFilter" in data:
        import capo_bedrock_data_automation.types.data_automation_project_stage_filter

        out["project_stage_filter"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage_filter.deserialize_json(
                data["projectStageFilter"]
            )
        )
    if "blueprintFilter" in data:
        import capo_bedrock_data_automation.types.blueprint_filter

        out["blueprint_filter"] = (
            capo_bedrock_data_automation.types.blueprint_filter.deserialize_json(
                data["blueprintFilter"]
            )
        )
    if "resourceOwner" in data:
        import capo_bedrock_data_automation.types.resource_owner

        out["resource_owner"] = (
            capo_bedrock_data_automation.types.resource_owner.deserialize_json(
                data["resourceOwner"]
            )
        )
    if "libraryFilter" in data:
        import capo_bedrock_data_automation.types.data_automation_library_filter

        out["library_filter"] = (
            capo_bedrock_data_automation.types.data_automation_library_filter.deserialize_json(
                data["libraryFilter"]
            )
        )
    return out
