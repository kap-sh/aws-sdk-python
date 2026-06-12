"""Generated from Smithy shape ``com.amazonaws.outposts#ComputeAssetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

ComputeAssetState: TypeAlias = Literal[
    "ACTIVE",
    "ISOLATED",
    "RETIRING",
    "INSTALLING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ISOLATED",
        "RETIRING",
        "INSTALLING",
    )
)


def serialize_json(value: ComputeAssetState) -> str:
    return value


def deserialize_json(data: str) -> ComputeAssetState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeAssetState value: {data!r}")
    return cast(ComputeAssetState, data)
