"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#TranscriptConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.channel_labeling_configuration
    import aws_sdk_bedrock_data_automation.types.speaker_labeling_configuration


class TranscriptConfiguration(TypedDict, closed=True):
    speaker_labeling: NotRequired[
        "aws_sdk_bedrock_data_automation.types.speaker_labeling_configuration.SpeakerLabelingConfiguration"
    ]
    channel_labeling: NotRequired[
        "aws_sdk_bedrock_data_automation.types.channel_labeling_configuration.ChannelLabelingConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptConfiguration) -> dict:
    out: dict = {}
    if "speaker_labeling" in value:
        import aws_sdk_bedrock_data_automation.types.speaker_labeling_configuration

        out["speakerLabeling"] = (
            aws_sdk_bedrock_data_automation.types.speaker_labeling_configuration.serialize_json(
                value["speaker_labeling"]
            )
        )
    if "channel_labeling" in value:
        import aws_sdk_bedrock_data_automation.types.channel_labeling_configuration

        out["channelLabeling"] = (
            aws_sdk_bedrock_data_automation.types.channel_labeling_configuration.serialize_json(
                value["channel_labeling"]
            )
        )
    return out


def deserialize_json(data: dict) -> TranscriptConfiguration:
    out: TranscriptConfiguration = {}  # type: ignore[typeddict-item]
    if "speakerLabeling" in data:
        import aws_sdk_bedrock_data_automation.types.speaker_labeling_configuration

        out["speaker_labeling"] = (
            aws_sdk_bedrock_data_automation.types.speaker_labeling_configuration.deserialize_json(
                data["speakerLabeling"]
            )
        )
    if "channelLabeling" in data:
        import aws_sdk_bedrock_data_automation.types.channel_labeling_configuration

        out["channel_labeling"] = (
            aws_sdk_bedrock_data_automation.types.channel_labeling_configuration.deserialize_json(
                data["channelLabeling"]
            )
        )
    return out
