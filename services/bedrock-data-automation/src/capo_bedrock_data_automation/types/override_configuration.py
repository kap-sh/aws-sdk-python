"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#OverrideConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.audio_override_configuration
    import capo_bedrock_data_automation.types.document_override_configuration
    import capo_bedrock_data_automation.types.image_override_configuration
    import capo_bedrock_data_automation.types.modality_routing_configuration
    import capo_bedrock_data_automation.types.video_override_configuration


class OverrideConfiguration(TypedDict, closed=True):
    document: NotRequired[
        "capo_bedrock_data_automation.types.document_override_configuration.DocumentOverrideConfiguration"
    ]
    image: NotRequired[
        "capo_bedrock_data_automation.types.image_override_configuration.ImageOverrideConfiguration"
    ]
    video: NotRequired[
        "capo_bedrock_data_automation.types.video_override_configuration.VideoOverrideConfiguration"
    ]
    audio: NotRequired[
        "capo_bedrock_data_automation.types.audio_override_configuration.AudioOverrideConfiguration"
    ]
    modality_routing: NotRequired[
        "capo_bedrock_data_automation.types.modality_routing_configuration.ModalityRoutingConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: OverrideConfiguration) -> dict:
    out: dict = {}
    if "document" in value:
        import capo_bedrock_data_automation.types.document_override_configuration

        out["document"] = (
            capo_bedrock_data_automation.types.document_override_configuration.serialize_json(
                value["document"]
            )
        )
    if "image" in value:
        import capo_bedrock_data_automation.types.image_override_configuration

        out["image"] = (
            capo_bedrock_data_automation.types.image_override_configuration.serialize_json(
                value["image"]
            )
        )
    if "video" in value:
        import capo_bedrock_data_automation.types.video_override_configuration

        out["video"] = (
            capo_bedrock_data_automation.types.video_override_configuration.serialize_json(
                value["video"]
            )
        )
    if "audio" in value:
        import capo_bedrock_data_automation.types.audio_override_configuration

        out["audio"] = (
            capo_bedrock_data_automation.types.audio_override_configuration.serialize_json(
                value["audio"]
            )
        )
    if "modality_routing" in value:
        import capo_bedrock_data_automation.types.modality_routing_configuration

        out["modalityRouting"] = (
            capo_bedrock_data_automation.types.modality_routing_configuration.serialize_json(
                value["modality_routing"]
            )
        )
    return out


def deserialize_json(data: dict) -> OverrideConfiguration:
    out: OverrideConfiguration = {}  # type: ignore[typeddict-item]
    if "document" in data:
        import capo_bedrock_data_automation.types.document_override_configuration

        out["document"] = (
            capo_bedrock_data_automation.types.document_override_configuration.deserialize_json(
                data["document"]
            )
        )
    if "image" in data:
        import capo_bedrock_data_automation.types.image_override_configuration

        out["image"] = (
            capo_bedrock_data_automation.types.image_override_configuration.deserialize_json(
                data["image"]
            )
        )
    if "video" in data:
        import capo_bedrock_data_automation.types.video_override_configuration

        out["video"] = (
            capo_bedrock_data_automation.types.video_override_configuration.deserialize_json(
                data["video"]
            )
        )
    if "audio" in data:
        import capo_bedrock_data_automation.types.audio_override_configuration

        out["audio"] = (
            capo_bedrock_data_automation.types.audio_override_configuration.deserialize_json(
                data["audio"]
            )
        )
    if "modalityRouting" in data:
        import capo_bedrock_data_automation.types.modality_routing_configuration

        out["modality_routing"] = (
            capo_bedrock_data_automation.types.modality_routing_configuration.deserialize_json(
                data["modalityRouting"]
            )
        )
    return out
