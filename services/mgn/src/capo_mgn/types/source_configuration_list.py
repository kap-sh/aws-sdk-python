"""Generated from Smithy shape ``com.amazonaws.mgn#SourceConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.source_configuration

SourceConfigurationList: TypeAlias = list[
    "capo_mgn.types.source_configuration.SourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfigurationList) -> list:
    import capo_mgn.types.source_configuration

    out: list = []
    for item in value:
        out.append(capo_mgn.types.source_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceConfigurationList:
    import capo_mgn.types.source_configuration

    out: SourceConfigurationList = []
    for item in data:
        out.append(capo_mgn.types.source_configuration.deserialize_json(item))
    return out
