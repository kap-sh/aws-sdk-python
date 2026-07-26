"""Generated from Smithy shape ``com.amazonaws.eks#UpdateParams``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.update_param

UpdateParams: TypeAlias = list["capo_eks.types.update_param.UpdateParam"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateParams) -> list:
    import capo_eks.types.update_param

    out: list = []
    for item in value:
        out.append(capo_eks.types.update_param.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateParams:
    import capo_eks.types.update_param

    out: UpdateParams = []
    for item in data:
        out.append(capo_eks.types.update_param.deserialize_json(item))
    return out
