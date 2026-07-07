"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationLibraryEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.entity_details


class GetDataAutomationLibraryEntityResponse(TypedDict, closed=True):
    entity: NotRequired[
        "aws_sdk_bedrock_data_automation.types.entity_details.EntityDetails"
    ]
    """Detailed information about the entity"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationLibraryEntityResponse) -> dict:
    out: dict = {}
    if "entity" in value:
        import aws_sdk_bedrock_data_automation.types.entity_details

        out["entity"] = (
            aws_sdk_bedrock_data_automation.types.entity_details.serialize_json(
                value["entity"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataAutomationLibraryEntityResponse:
    out: GetDataAutomationLibraryEntityResponse = {}  # type: ignore[typeddict-item]
    if "entity" in data:
        import aws_sdk_bedrock_data_automation.types.entity_details

        out["entity"] = (
            aws_sdk_bedrock_data_automation.types.entity_details.deserialize_json(
                data["entity"]
            )
        )
    return out
