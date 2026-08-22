"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ModalityProcessingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.state


class ModalityProcessingConfiguration(TypedDict, closed=True):
    state: NotRequired["capo_bedrock_data_automation.types.state.State"]


# --- restJson1 ser/de ---
def serialize_json(value: ModalityProcessingConfiguration) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_bedrock_data_automation.types.state

        out["state"] = capo_bedrock_data_automation.types.state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> ModalityProcessingConfiguration:
    out: ModalityProcessingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_bedrock_data_automation.types.state

        out["state"] = capo_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    return out
