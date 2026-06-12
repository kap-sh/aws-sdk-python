"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorAwsRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.voice_connector_aws_region

VoiceConnectorAwsRegionList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.voice_connector_aws_region.VoiceConnectorAwsRegion"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorAwsRegionList) -> list:
    import aws_sdk_chime_sdk_voice.types.voice_connector_aws_region

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.voice_connector_aws_region.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VoiceConnectorAwsRegionList:
    import aws_sdk_chime_sdk_voice.types.voice_connector_aws_region

    out: VoiceConnectorAwsRegionList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.voice_connector_aws_region.deserialize_json(
                item
            )
        )
    return out
