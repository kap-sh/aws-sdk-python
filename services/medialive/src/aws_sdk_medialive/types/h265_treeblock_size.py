"""Generated from Smithy shape ``com.amazonaws.medialive#H265TreeblockSize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Treeblock Size"""
H265TreeblockSize: TypeAlias = Literal[
    "AUTO",
    "TREE_SIZE_32X32",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "TREE_SIZE_32X32",
    )
)


def serialize_json(value: H265TreeblockSize) -> str:
    return value


def deserialize_json(data: str) -> H265TreeblockSize:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265TreeblockSize value: {data!r}")
    return cast(H265TreeblockSize, data)
