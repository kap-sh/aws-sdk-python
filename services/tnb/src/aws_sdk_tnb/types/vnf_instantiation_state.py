"""Generated from Smithy shape ``com.amazonaws.tnb#VnfInstantiationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

VnfInstantiationState: TypeAlias = Literal[
    "INSTANTIATED",
    "NOT_INSTANTIATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTANTIATED",
        "NOT_INSTANTIATED",
    )
)


def serialize_json(value: VnfInstantiationState) -> str:
    return value


def deserialize_json(data: str) -> VnfInstantiationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VnfInstantiationState value: {data!r}")
    return cast(VnfInstantiationState, data)
