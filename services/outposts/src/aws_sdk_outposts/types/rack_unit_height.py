"""Generated from Smithy shape ``com.amazonaws.outposts#RackUnitHeight``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

RackUnitHeight: TypeAlias = Literal[
    "HEIGHT_42U",
    "HEIGHT_2U",
    "HEIGHT_1U",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEIGHT_42U",
        "HEIGHT_2U",
        "HEIGHT_1U",
    )
)


def serialize_json(value: RackUnitHeight) -> str:
    return value


def deserialize_json(data: str) -> RackUnitHeight:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RackUnitHeight value: {data!r}")
    return cast(RackUnitHeight, data)
