"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadLenses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias

WorkloadLenses: TypeAlias = list["capo_wellarchitected.types.lens_alias.LensAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadLenses) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkloadLenses:
    return list(data)
