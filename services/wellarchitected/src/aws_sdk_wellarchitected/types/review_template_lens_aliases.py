"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateLensAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias

ReviewTemplateLensAliases: TypeAlias = list[
    "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplateLensAliases) -> list:
    return list(value)


def deserialize_json(data: list) -> ReviewTemplateLensAliases:
    return list(data)
