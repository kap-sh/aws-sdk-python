"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#EncoderConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.encoder_configuration_summary

EncoderConfigurationSummaryList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.encoder_configuration_summary.EncoderConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EncoderConfigurationSummaryList) -> list:
    import aws_sdk_ivs_realtime.types.encoder_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs_realtime.types.encoder_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EncoderConfigurationSummaryList:
    import aws_sdk_ivs_realtime.types.encoder_configuration_summary

    out: EncoderConfigurationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.encoder_configuration_summary.deserialize_json(
                item
            )
        )
    return out
