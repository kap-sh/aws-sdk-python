"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateBlueprintResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint


class CreateBlueprintResponse(TypedDict, closed=True):
    blueprint: "capo_bedrock_data_automation.types.blueprint.Blueprint"


# --- restJson1 ser/de ---
def serialize_json(value: CreateBlueprintResponse) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.blueprint

    out["blueprint"] = capo_bedrock_data_automation.types.blueprint.serialize_json(
        value["blueprint"]
    )
    return out


def deserialize_json(data: dict) -> CreateBlueprintResponse:
    out: CreateBlueprintResponse = {}  # type: ignore[typeddict-item]
    if "blueprint" in data:
        import capo_bedrock_data_automation.types.blueprint

        out["blueprint"] = (
            capo_bedrock_data_automation.types.blueprint.deserialize_json(
                data["blueprint"]
            )
        )
    else:
        raise DeserializationError("CreateBlueprintResponse.blueprint required")
    return out
