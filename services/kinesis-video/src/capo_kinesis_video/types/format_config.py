"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#FormatConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_video.types.format_config_key
    import capo_kinesis_video.types.format_config_value

FormatConfig: TypeAlias = dict[
    "capo_kinesis_video.types.format_config_key.FormatConfigKey",
    "capo_kinesis_video.types.format_config_value.FormatConfigValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FormatConfig) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_kinesis_video.types.format_config_key

        out[capo_kinesis_video.types.format_config_key.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> FormatConfig:
    out: FormatConfig = {}
    for key, value in data.items():
        import capo_kinesis_video.types.format_config_key

        out[capo_kinesis_video.types.format_config_key.deserialize_json(key)] = value
    return out
