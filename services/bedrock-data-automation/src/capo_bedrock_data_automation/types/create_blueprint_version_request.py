"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateBlueprintVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.client_token


class CreateBlueprintVersionRequest(TypedDict, closed=True):
    blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """ARN generated at the server side when a Blueprint is created"""
    client_token: NotRequired[
        "capo_bedrock_data_automation.types.client_token.ClientToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateBlueprintVersionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateBlueprintVersionRequest:
    out: CreateBlueprintVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
