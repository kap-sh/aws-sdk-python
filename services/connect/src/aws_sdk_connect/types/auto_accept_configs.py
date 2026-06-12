"""Generated from Smithy shape ``com.amazonaws.connect#AutoAcceptConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.auto_accept_config

AutoAcceptConfigs: TypeAlias = list[
    "aws_sdk_connect.types.auto_accept_config.AutoAcceptConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoAcceptConfigs) -> list:
    import aws_sdk_connect.types.auto_accept_config

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.auto_accept_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> AutoAcceptConfigs:
    import aws_sdk_connect.types.auto_accept_config

    out: AutoAcceptConfigs = []
    for item in data:
        out.append(aws_sdk_connect.types.auto_accept_config.deserialize_json(item))
    return out
