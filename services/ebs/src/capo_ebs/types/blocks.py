"""Generated from Smithy shape ``com.amazonaws.ebs#Blocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ebs.types.block

Blocks: TypeAlias = list["capo_ebs.types.block.Block"]


# --- restJson1 ser/de ---
def serialize_json(value: Blocks) -> list:
    import capo_ebs.types.block

    out: list = []
    for item in value:
        out.append(capo_ebs.types.block.serialize_json(item))
    return out


def deserialize_json(data: list) -> Blocks:
    import capo_ebs.types.block

    out: Blocks = []
    for item in data:
        out.append(capo_ebs.types.block.deserialize_json(item))
    return out
