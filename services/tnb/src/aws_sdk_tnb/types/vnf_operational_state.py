"""Generated from Smithy shape ``com.amazonaws.tnb#VnfOperationalState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

VnfOperationalState: TypeAlias = Literal[
    "STARTED",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTED",
        "STOPPED",
    )
)


def serialize_json(value: VnfOperationalState) -> str:
    return value


def deserialize_json(data: str) -> VnfOperationalState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VnfOperationalState value: {data!r}")
    return cast(VnfOperationalState, data)
