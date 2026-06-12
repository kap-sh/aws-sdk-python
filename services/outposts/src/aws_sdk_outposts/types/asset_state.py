"""Generated from Smithy shape ``com.amazonaws.outposts#AssetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

AssetState: TypeAlias = Literal[
    "ACTIVE",
    "RETIRING",
    "ISOLATED",
    "INSTALLING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "RETIRING",
        "ISOLATED",
        "INSTALLING",
    )
)


def serialize_json(value: AssetState) -> str:
    return value


def deserialize_json(data: str) -> AssetState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetState value: {data!r}")
    return cast(AssetState, data)
