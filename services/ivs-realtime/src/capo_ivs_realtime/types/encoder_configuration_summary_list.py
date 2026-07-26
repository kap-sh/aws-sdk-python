"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#EncoderConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.encoder_configuration_summary

EncoderConfigurationSummaryList: TypeAlias = list[
    "capo_ivs_realtime.types.encoder_configuration_summary.EncoderConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EncoderConfigurationSummaryList) -> list:
    import capo_ivs_realtime.types.encoder_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_ivs_realtime.types.encoder_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EncoderConfigurationSummaryList:
    import capo_ivs_realtime.types.encoder_configuration_summary

    out: EncoderConfigurationSummaryList = []
    for item in data:
        out.append(
            capo_ivs_realtime.types.encoder_configuration_summary.deserialize_json(item)
        )
    return out
