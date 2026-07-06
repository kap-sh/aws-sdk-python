"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationLibraryEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn
    import aws_sdk_bedrock_data_automation.types.entity_id
    import aws_sdk_bedrock_data_automation.types.entity_type


class GetDataAutomationLibraryEntityRequest(TypedDict, closed=True):
    library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    """ARN generated at the server side when a DataAutomationLibrary is created"""
    entity_type: "aws_sdk_bedrock_data_automation.types.entity_type.EntityType"
    """The entity type for which the entity is requested"""
    entity_id: "aws_sdk_bedrock_data_automation.types.entity_id.EntityId"
    """Unique identifier for the entity"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationLibraryEntityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataAutomationLibraryEntityRequest:
    out: GetDataAutomationLibraryEntityRequest = {}  # type: ignore[typeddict-item]
    return out
