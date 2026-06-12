"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#FormatConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.format_config_key
    import aws_sdk_kinesis_video.types.format_config_value

FormatConfig: TypeAlias = dict[
    "aws_sdk_kinesis_video.types.format_config_key.FormatConfigKey",
    "aws_sdk_kinesis_video.types.format_config_value.FormatConfigValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FormatConfig) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_kinesis_video.types.format_config_key

        out[aws_sdk_kinesis_video.types.format_config_key.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> FormatConfig:
    out: FormatConfig = {}
    for key, value in data.items():
        import aws_sdk_kinesis_video.types.format_config_key

        out[aws_sdk_kinesis_video.types.format_config_key.deserialize_json(key)] = value
    return out
