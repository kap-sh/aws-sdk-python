"""Generated from Smithy shape ``com.amazonaws.medialive#H265TreeblockSize``."""

from typing import Literal, TypeAlias, cast

"""H265 Treeblock Size"""
H265TreeblockSize: TypeAlias = Literal[
    "AUTO",
    "TREE_SIZE_32X32",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265TreeblockSize) -> str:
    return value


def deserialize_json(data: str) -> H265TreeblockSize:
    return cast(H265TreeblockSize, data)
