"""Generated from Smithy shape ``com.amazonaws.iot#CheckCustomConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.config_name
    import aws_sdk_iot.types.config_value

CheckCustomConfiguration: TypeAlias = dict[
    "aws_sdk_iot.types.config_name.ConfigName",
    "aws_sdk_iot.types.config_value.ConfigValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CheckCustomConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iot.types.config_name

        out[aws_sdk_iot.types.config_name.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> CheckCustomConfiguration:
    out: CheckCustomConfiguration = {}
    for key, value in data.items():
        import aws_sdk_iot.types.config_name

        out[aws_sdk_iot.types.config_name.deserialize_json(key)] = value
    return out
