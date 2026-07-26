"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SourceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.source_configuration

SourceConfigurations: TypeAlias = list[
    "capo_iottwinmaker.types.source_configuration.SourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfigurations) -> list:
    import capo_iottwinmaker.types.source_configuration

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.source_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceConfigurations:
    import capo_iottwinmaker.types.source_configuration

    out: SourceConfigurations = []
    for item in data:
        out.append(capo_iottwinmaker.types.source_configuration.deserialize_json(item))
    return out
