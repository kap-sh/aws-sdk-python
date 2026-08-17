"""Generated from Smithy shape ``com.amazonaws.lambda#ArchitecturesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.architecture

ArchitecturesList: TypeAlias = list["capo_lambda.types.architecture.Architecture"]


# --- restJson1 ser/de ---
def serialize_json(value: ArchitecturesList) -> list:
    import capo_lambda.types.architecture

    out: list = []
    for item in value:
        out.append(capo_lambda.types.architecture.serialize_json(item))
    return out


def deserialize_json(data: list) -> ArchitecturesList:
    import capo_lambda.types.architecture

    out: ArchitecturesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.architecture.deserialize_json(item))
    return out
