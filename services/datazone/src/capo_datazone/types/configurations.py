"""Generated from Smithy shape ``com.amazonaws.datazone#Configurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.configuration

Configurations: TypeAlias = list["capo_datazone.types.configuration.Configuration"]


# --- restJson1 ser/de ---
def serialize_json(value: Configurations) -> list:
    import capo_datazone.types.configuration

    out: list = []
    for item in value:
        out.append(capo_datazone.types.configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> Configurations:
    import capo_datazone.types.configuration

    out: Configurations = []
    for item in data:
        out.append(capo_datazone.types.configuration.deserialize_json(item))
    return out
