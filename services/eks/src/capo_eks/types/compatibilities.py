"""Generated from Smithy shape ``com.amazonaws.eks#Compatibilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.compatibility

Compatibilities: TypeAlias = list["capo_eks.types.compatibility.Compatibility"]


# --- restJson1 ser/de ---
def serialize_json(value: Compatibilities) -> list:
    import capo_eks.types.compatibility

    out: list = []
    for item in value:
        out.append(capo_eks.types.compatibility.serialize_json(item))
    return out


def deserialize_json(data: list) -> Compatibilities:
    import capo_eks.types.compatibility

    out: Compatibilities = []
    for item in data:
        out.append(capo_eks.types.compatibility.deserialize_json(item))
    return out
