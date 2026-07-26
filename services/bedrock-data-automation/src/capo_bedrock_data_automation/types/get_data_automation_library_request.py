"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationLibraryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_arn


class GetDataAutomationLibraryRequest(TypedDict, closed=True):
    library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    """ARN generated at the server side when a DataAutomationLibrary is created"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationLibraryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataAutomationLibraryRequest:
    out: GetDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
    return out
