"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.phone_number_config

PhoneNumberConfigs: TypeAlias = list[
    "aws_sdk_connect.types.phone_number_config.PhoneNumberConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberConfigs) -> list:
    import aws_sdk_connect.types.phone_number_config

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.phone_number_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberConfigs:
    import aws_sdk_connect.types.phone_number_config

    out: PhoneNumberConfigs = []
    for item in data:
        out.append(aws_sdk_connect.types.phone_number_config.deserialize_json(item))
    return out
