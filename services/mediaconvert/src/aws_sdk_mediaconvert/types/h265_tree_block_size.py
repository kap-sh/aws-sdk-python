"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265TreeBlockSize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Select the tree block size used for encoding. If you enter \"auto\", the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter \"auto\"."""
H265TreeBlockSize: TypeAlias = Literal[
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


def serialize_json(value: H265TreeBlockSize) -> str:
    return value


def deserialize_json(data: str) -> H265TreeBlockSize:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265TreeBlockSize value: {data!r}")
    return cast(H265TreeBlockSize, data)
