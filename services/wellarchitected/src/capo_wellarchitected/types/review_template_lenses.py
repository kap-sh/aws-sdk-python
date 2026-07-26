"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateLenses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias

ReviewTemplateLenses: TypeAlias = list[
    "capo_wellarchitected.types.lens_alias.LensAlias"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplateLenses) -> list:
    return list(value)


def deserialize_json(data: list) -> ReviewTemplateLenses:
    return list(data)
