"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DeleteBlueprintRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_version


class DeleteBlueprintRequest(TypedDict, closed=True):
    blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """ARN generated at the server side when a Blueprint is created"""
    blueprint_version: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
    ]
    """Optional field to delete a specific Blueprint version"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBlueprintRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBlueprintRequest:
    out: DeleteBlueprintRequest = {}  # type: ignore[typeddict-item]
    return out
