"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingModeOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.recording_mode_override

RecordingModeOverrides: TypeAlias = list[
    "aws_sdk_config_service.types.recording_mode_override.RecordingModeOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordingModeOverrides) -> list:
    import aws_sdk_config_service.types.recording_mode_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.recording_mode_override.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecordingModeOverrides:
    import aws_sdk_config_service.types.recording_mode_override

    out: RecordingModeOverrides = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.recording_mode_override.deserialize_aws_json_1_1(
                item
            )
        )
    return out
