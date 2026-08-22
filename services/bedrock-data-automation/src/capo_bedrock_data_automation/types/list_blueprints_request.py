"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListBlueprintsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_stage_filter
    import capo_bedrock_data_automation.types.data_automation_project_filter
    import capo_bedrock_data_automation.types.max_results
    import capo_bedrock_data_automation.types.next_token
    import capo_bedrock_data_automation.types.resource_owner


class ListBlueprintsRequest(TypedDict, closed=True):
    blueprint_arn: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    ]
    resource_owner: NotRequired[
        "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
    ]
    blueprint_stage_filter: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_stage_filter.BlueprintStageFilter"
    ]
    max_results: NotRequired[
        "capo_bedrock_data_automation.types.max_results.MaxResults"
    ]
    next_token: NotRequired["capo_bedrock_data_automation.types.next_token.NextToken"]
    project_filter: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListBlueprintsRequest) -> dict:
    out: dict = {}
    if "blueprint_arn" in value:
        out["blueprintArn"] = value["blueprint_arn"]
    if "resource_owner" in value:
        import capo_bedrock_data_automation.types.resource_owner

        out["resourceOwner"] = (
            capo_bedrock_data_automation.types.resource_owner.serialize_json(
                value["resource_owner"]
            )
        )
    if "blueprint_stage_filter" in value:
        import capo_bedrock_data_automation.types.blueprint_stage_filter

        out["blueprintStageFilter"] = (
            capo_bedrock_data_automation.types.blueprint_stage_filter.serialize_json(
                value["blueprint_stage_filter"]
            )
        )
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


def deserialize_json(data: dict) -> ListBlueprintsRequest:
    out: ListBlueprintsRequest = {}  # type: ignore[typeddict-item]
    if data.get("blueprintArn") is not None:
        out["blueprint_arn"] = data["blueprintArn"]
    if data.get("resourceOwner") is not None:
        import capo_bedrock_data_automation.types.resource_owner

        out["resource_owner"] = (
            capo_bedrock_data_automation.types.resource_owner.deserialize_json(
                data["resourceOwner"]
            )
        )
    if data.get("blueprintStageFilter") is not None:
        import capo_bedrock_data_automation.types.blueprint_stage_filter

        out["blueprint_stage_filter"] = (
            capo_bedrock_data_automation.types.blueprint_stage_filter.deserialize_json(
                data["blueprintStageFilter"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("projectFilter") is not None:
        import capo_bedrock_data_automation.types.data_automation_project_filter

        out["project_filter"] = (
            capo_bedrock_data_automation.types.data_automation_project_filter.deserialize_json(
                data["projectFilter"]
            )
        )
    return out
