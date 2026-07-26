"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadResourceDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.definition_type

WorkloadResourceDefinition: TypeAlias = list[
    "capo_wellarchitected.types.definition_type.DefinitionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadResourceDefinition) -> list:
    import capo_wellarchitected.types.definition_type

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.definition_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkloadResourceDefinition:
    import capo_wellarchitected.types.definition_type

    out: WorkloadResourceDefinition = []
    for item in data:
        out.append(capo_wellarchitected.types.definition_type.deserialize_json(item))
    return out
