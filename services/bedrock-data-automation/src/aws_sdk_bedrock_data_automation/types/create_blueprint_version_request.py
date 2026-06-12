"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateBlueprintVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_arn
    import aws_sdk_bedrock_data_automation.types.client_token


class CreateBlueprintVersionRequest(TypedDict):
    blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """ARN generated at the server side when a Blueprint is created"""
    client_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateBlueprintVersionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateBlueprintVersionRequest:
    out: CreateBlueprintVersionRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
