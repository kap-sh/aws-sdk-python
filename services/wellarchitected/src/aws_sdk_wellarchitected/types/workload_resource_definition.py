"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadResourceDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.definition_type

WorkloadResourceDefinition: TypeAlias = list[
    "aws_sdk_wellarchitected.types.definition_type.DefinitionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadResourceDefinition) -> list:
    import aws_sdk_wellarchitected.types.definition_type

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.definition_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkloadResourceDefinition:
    import aws_sdk_wellarchitected.types.definition_type

    out: WorkloadResourceDefinition = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.definition_type.deserialize_json(item))
    return out
