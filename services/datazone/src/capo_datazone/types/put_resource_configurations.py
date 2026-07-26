"""Generated from Smithy shape ``com.amazonaws.datazone#PutResourceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.put_resource_configuration

PutResourceConfigurations: TypeAlias = list[
    "capo_datazone.types.put_resource_configuration.PutResourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: PutResourceConfigurations) -> list:
    import capo_datazone.types.put_resource_configuration

    out: list = []
    for item in value:
        out.append(capo_datazone.types.put_resource_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> PutResourceConfigurations:
    import capo_datazone.types.put_resource_configuration

    out: PutResourceConfigurations = []
    for item in data:
        out.append(
            capo_datazone.types.put_resource_configuration.deserialize_json(item)
        )
    return out
