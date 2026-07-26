"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceInputSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.id_namespace_input_source

IdNamespaceInputSourceConfig: TypeAlias = list[
    "capo_entityresolution.types.id_namespace_input_source.IdNamespaceInputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceInputSourceConfig) -> list:
    import capo_entityresolution.types.id_namespace_input_source

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.id_namespace_input_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IdNamespaceInputSourceConfig:
    import capo_entityresolution.types.id_namespace_input_source

    out: IdNamespaceInputSourceConfig = []
    for item in data:
        out.append(
            capo_entityresolution.types.id_namespace_input_source.deserialize_json(item)
        )
    return out
