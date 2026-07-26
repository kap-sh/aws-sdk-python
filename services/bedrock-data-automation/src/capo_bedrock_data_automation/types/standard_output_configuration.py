"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#StandardOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.audio_standard_output_configuration
    import capo_bedrock_data_automation.types.document_standard_output_configuration
    import capo_bedrock_data_automation.types.image_standard_output_configuration
    import capo_bedrock_data_automation.types.video_standard_output_configuration


class StandardOutputConfiguration(TypedDict, closed=True):
    document: NotRequired[
        "capo_bedrock_data_automation.types.document_standard_output_configuration.DocumentStandardOutputConfiguration"
    ]
    image: NotRequired[
        "capo_bedrock_data_automation.types.image_standard_output_configuration.ImageStandardOutputConfiguration"
    ]
    video: NotRequired[
        "capo_bedrock_data_automation.types.video_standard_output_configuration.VideoStandardOutputConfiguration"
    ]
    audio: NotRequired[
        "capo_bedrock_data_automation.types.audio_standard_output_configuration.AudioStandardOutputConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: StandardOutputConfiguration) -> dict:
    out: dict = {}
    if "document" in value:
        import capo_bedrock_data_automation.types.document_standard_output_configuration

        out["document"] = (
            capo_bedrock_data_automation.types.document_standard_output_configuration.serialize_json(
                value["document"]
            )
        )
    if "image" in value:
        import capo_bedrock_data_automation.types.image_standard_output_configuration

        out["image"] = (
            capo_bedrock_data_automation.types.image_standard_output_configuration.serialize_json(
                value["image"]
            )
        )
    if "video" in value:
        import capo_bedrock_data_automation.types.video_standard_output_configuration

        out["video"] = (
            capo_bedrock_data_automation.types.video_standard_output_configuration.serialize_json(
                value["video"]
            )
        )
    if "audio" in value:
        import capo_bedrock_data_automation.types.audio_standard_output_configuration

        out["audio"] = (
            capo_bedrock_data_automation.types.audio_standard_output_configuration.serialize_json(
                value["audio"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardOutputConfiguration:
    out: StandardOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "document" in data:
        import capo_bedrock_data_automation.types.document_standard_output_configuration

        out["document"] = (
            capo_bedrock_data_automation.types.document_standard_output_configuration.deserialize_json(
                data["document"]
            )
        )
    if "image" in data:
        import capo_bedrock_data_automation.types.image_standard_output_configuration

        out["image"] = (
            capo_bedrock_data_automation.types.image_standard_output_configuration.deserialize_json(
                data["image"]
            )
        )
    if "video" in data:
        import capo_bedrock_data_automation.types.video_standard_output_configuration

        out["video"] = (
            capo_bedrock_data_automation.types.video_standard_output_configuration.deserialize_json(
                data["video"]
            )
        )
    if "audio" in data:
        import capo_bedrock_data_automation.types.audio_standard_output_configuration

        out["audio"] = (
            capo_bedrock_data_automation.types.audio_standard_output_configuration.deserialize_json(
                data["audio"]
            )
        )
    return out
