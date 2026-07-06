"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationLibraryEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summaries
    import aws_sdk_bedrock_data_automation.types.next_token


class ListDataAutomationLibraryEntitiesResponse(TypedDict, closed=True):
    entities: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summaries.DataAutomationLibraryEntitySummaries"
    ]
    """List of entities"""
    next_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
    ]
    """Pagination token for retrieving the next set of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationLibraryEntitiesResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summaries

        out["entities"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summaries.serialize_json(
                value["entities"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAutomationLibraryEntitiesResponse:
    out: ListDataAutomationLibraryEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "entities" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summaries

        out["entities"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summaries.deserialize_json(
                data["entities"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
