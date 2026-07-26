"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias

LensAliases: TypeAlias = list["capo_wellarchitected.types.lens_alias.LensAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: LensAliases) -> list:
    return list(value)


def deserialize_json(data: list) -> LensAliases:
    return list(data)
