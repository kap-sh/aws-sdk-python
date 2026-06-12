"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DeleteBlueprintRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_arn
    import aws_sdk_bedrock_data_automation.types.blueprint_version


class DeleteBlueprintRequest(TypedDict):
    blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """ARN generated at the server side when a Blueprint is created"""
    blueprint_version: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
    ]
    """Optional field to delete a specific Blueprint version"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBlueprintRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBlueprintRequest:
    out: DeleteBlueprintRequest = {}  # type: ignore[typeddict-item]
    return out
