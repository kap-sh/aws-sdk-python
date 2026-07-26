"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageBoundingBox``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.state


class ImageBoundingBox(TypedDict, closed=True):
    state: "capo_bedrock_data_automation.types.state.State"


# --- restJson1 ser/de ---
def serialize_json(value: ImageBoundingBox) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.state

    out["state"] = capo_bedrock_data_automation.types.state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> ImageBoundingBox:
    out: ImageBoundingBox = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import capo_bedrock_data_automation.types.state

        out["state"] = capo_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("ImageBoundingBox.state required")
    return out
