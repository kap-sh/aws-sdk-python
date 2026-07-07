"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DeleteDataAutomationLibraryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn


class DeleteDataAutomationLibraryRequest(TypedDict, closed=True):
    library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    """ARN generated at the server side when a DataAutomationLibrary is created"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataAutomationLibraryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataAutomationLibraryRequest:
    out: DeleteDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
    return out
