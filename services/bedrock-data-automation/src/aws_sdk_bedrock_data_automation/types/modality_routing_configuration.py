"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ModalityRoutingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.desired_modality


class ModalityRoutingConfiguration(TypedDict, closed=True):
    jpeg: NotRequired[
        "aws_sdk_bedrock_data_automation.types.desired_modality.DesiredModality"
    ]
    png: NotRequired[
        "aws_sdk_bedrock_data_automation.types.desired_modality.DesiredModality"
    ]
    mp4: NotRequired[
        "aws_sdk_bedrock_data_automation.types.desired_modality.DesiredModality"
    ]
    mov: NotRequired[
        "aws_sdk_bedrock_data_automation.types.desired_modality.DesiredModality"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ModalityRoutingConfiguration) -> dict:
    out: dict = {}
    if "jpeg" in value:
        import aws_sdk_bedrock_data_automation.types.desired_modality

        out["jpeg"] = (
            aws_sdk_bedrock_data_automation.types.desired_modality.serialize_json(
                value["jpeg"]
            )
        )
    if "png" in value:
        import aws_sdk_bedrock_data_automation.types.desired_modality

        out["png"] = (
            aws_sdk_bedrock_data_automation.types.desired_modality.serialize_json(
                value["png"]
            )
        )
    if "mp4" in value:
        import aws_sdk_bedrock_data_automation.types.desired_modality

        out["mp4"] = (
            aws_sdk_bedrock_data_automation.types.desired_modality.serialize_json(
                value["mp4"]
            )
        )
    if "mov" in value:
        import aws_sdk_bedrock_data_automation.types.desired_modality

        out["mov"] = (
            aws_sdk_bedrock_data_automation.types.desired_modality.serialize_json(
                value["mov"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModalityRoutingConfiguration:
    out: ModalityRoutingConfiguration = {}  # type: ignore[typeddict-item]
    if "jpeg" in data:
        import aws_sdk_bedrock_data_automation.types.desired_modality

        out["jpeg"] = (
            aws_sdk_bedrock_data_automation.types.desired_modality.deserialize_json(
                data["jpeg"]
            )
        )
    if "png" in data:
        import aws_sdk_bedrock_data_automation.types.desired_modality

        out["png"] = (
            aws_sdk_bedrock_data_automation.types.desired_modality.deserialize_json(
                data["png"]
            )
        )
    if "mp4" in data:
        import aws_sdk_bedrock_data_automation.types.desired_modality

        out["mp4"] = (
            aws_sdk_bedrock_data_automation.types.desired_modality.deserialize_json(
                data["mp4"]
            )
        )
    if "mov" in data:
        import aws_sdk_bedrock_data_automation.types.desired_modality

        out["mov"] = (
            aws_sdk_bedrock_data_automation.types.desired_modality.deserialize_json(
                data["mov"]
            )
        )
    return out
