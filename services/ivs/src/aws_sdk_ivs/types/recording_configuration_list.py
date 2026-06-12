"""Generated from Smithy shape ``com.amazonaws.ivs#RecordingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.recording_configuration_summary

RecordingConfigurationList: TypeAlias = list[
    "aws_sdk_ivs.types.recording_configuration_summary.RecordingConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordingConfigurationList) -> list:
    import aws_sdk_ivs.types.recording_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs.types.recording_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecordingConfigurationList:
    import aws_sdk_ivs.types.recording_configuration_summary

    out: RecordingConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_ivs.types.recording_configuration_summary.deserialize_json(item)
        )
    return out
