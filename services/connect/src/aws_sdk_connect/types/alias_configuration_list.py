"""Generated from Smithy shape ``com.amazonaws.connect#AliasConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.alias_configuration

AliasConfigurationList: TypeAlias = list[
    "aws_sdk_connect.types.alias_configuration.AliasConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AliasConfigurationList) -> list:
    import aws_sdk_connect.types.alias_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.alias_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> AliasConfigurationList:
    import aws_sdk_connect.types.alias_configuration

    out: AliasConfigurationList = []
    for item in data:
        out.append(aws_sdk_connect.types.alias_configuration.deserialize_json(item))
    return out
