"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationLibrariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_summaries
    import capo_bedrock_data_automation.types.next_token


class ListDataAutomationLibrariesResponse(TypedDict, closed=True):
    libraries: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_summaries.DataAutomationLibrarySummaries"
    ]
    next_token: NotRequired["capo_bedrock_data_automation.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationLibrariesResponse) -> dict:
    out: dict = {}
    if "libraries" in value:
        import capo_bedrock_data_automation.types.data_automation_library_summaries

        out["libraries"] = (
            capo_bedrock_data_automation.types.data_automation_library_summaries.serialize_json(
                value["libraries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAutomationLibrariesResponse:
    out: ListDataAutomationLibrariesResponse = {}  # type: ignore[typeddict-item]
    if "libraries" in data:
        import capo_bedrock_data_automation.types.data_automation_library_summaries

        out["libraries"] = (
            capo_bedrock_data_automation.types.data_automation_library_summaries.deserialize_json(
                data["libraries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
