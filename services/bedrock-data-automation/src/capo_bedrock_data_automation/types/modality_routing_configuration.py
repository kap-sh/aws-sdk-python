"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ModalityRoutingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.desired_modality


class ModalityRoutingConfiguration(TypedDict, closed=True):
    jpeg: NotRequired[
        "capo_bedrock_data_automation.types.desired_modality.DesiredModality"
    ]
    png: NotRequired[
        "capo_bedrock_data_automation.types.desired_modality.DesiredModality"
    ]
    mp4: NotRequired[
        "capo_bedrock_data_automation.types.desired_modality.DesiredModality"
    ]
    mov: NotRequired[
        "capo_bedrock_data_automation.types.desired_modality.DesiredModality"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ModalityRoutingConfiguration) -> dict:
    out: dict = {}
    if "jpeg" in value:
        import capo_bedrock_data_automation.types.desired_modality

        out["jpeg"] = (
            capo_bedrock_data_automation.types.desired_modality.serialize_json(
                value["jpeg"]
            )
        )
    if "png" in value:
        import capo_bedrock_data_automation.types.desired_modality

        out["png"] = capo_bedrock_data_automation.types.desired_modality.serialize_json(
            value["png"]
        )
    if "mp4" in value:
        import capo_bedrock_data_automation.types.desired_modality

        out["mp4"] = capo_bedrock_data_automation.types.desired_modality.serialize_json(
            value["mp4"]
        )
    if "mov" in value:
        import capo_bedrock_data_automation.types.desired_modality

        out["mov"] = capo_bedrock_data_automation.types.desired_modality.serialize_json(
            value["mov"]
        )
    return out


def deserialize_json(data: dict) -> ModalityRoutingConfiguration:
    out: ModalityRoutingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("jpeg") is not None:
        import capo_bedrock_data_automation.types.desired_modality

        out["jpeg"] = (
            capo_bedrock_data_automation.types.desired_modality.deserialize_json(
                data["jpeg"]
            )
        )
    if data.get("png") is not None:
        import capo_bedrock_data_automation.types.desired_modality

        out["png"] = (
            capo_bedrock_data_automation.types.desired_modality.deserialize_json(
                data["png"]
            )
        )
    if data.get("mp4") is not None:
        import capo_bedrock_data_automation.types.desired_modality

        out["mp4"] = (
            capo_bedrock_data_automation.types.desired_modality.deserialize_json(
                data["mp4"]
            )
        )
    if data.get("mov") is not None:
        import capo_bedrock_data_automation.types.desired_modality

        out["mov"] = (
            capo_bedrock_data_automation.types.desired_modality.deserialize_json(
                data["mov"]
            )
        )
    return out
