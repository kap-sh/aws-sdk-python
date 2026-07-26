"""Generated from Smithy shape ``com.amazonaws.connect#AliasConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.alias_configuration

AliasConfigurationList: TypeAlias = list[
    "capo_connect.types.alias_configuration.AliasConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AliasConfigurationList) -> list:
    import capo_connect.types.alias_configuration

    out: list = []
    for item in value:
        out.append(capo_connect.types.alias_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> AliasConfigurationList:
    import capo_connect.types.alias_configuration

    out: AliasConfigurationList = []
    for item in data:
        out.append(capo_connect.types.alias_configuration.deserialize_json(item))
    return out
