"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateBlueprintResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint


class CreateBlueprintResponse(TypedDict):
    blueprint: "aws_sdk_bedrock_data_automation.types.blueprint.Blueprint"


# --- restJson1 ser/de ---
def serialize_json(value: CreateBlueprintResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.blueprint

    out["blueprint"] = aws_sdk_bedrock_data_automation.types.blueprint.serialize_json(
        value["blueprint"]
    )
    return out


def deserialize_json(data: dict) -> CreateBlueprintResponse:
    out: CreateBlueprintResponse = {}  # type: ignore[typeddict-item]
    if "blueprint" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint

        out["blueprint"] = (
            aws_sdk_bedrock_data_automation.types.blueprint.deserialize_json(
                data["blueprint"]
            )
        )
    else:
        raise DeserializationError("CreateBlueprintResponse.blueprint required")
    return out
