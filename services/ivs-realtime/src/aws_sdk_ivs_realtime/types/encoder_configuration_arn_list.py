"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#EncoderConfigurationArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.encoder_configuration_arn

EncoderConfigurationArnList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: EncoderConfigurationArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> EncoderConfigurationArnList:
    return list(data)
