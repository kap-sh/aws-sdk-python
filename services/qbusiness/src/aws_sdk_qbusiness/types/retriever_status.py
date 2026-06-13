"""Generated from Smithy shape ``com.amazonaws.qbusiness#RetrieverStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

RetrieverStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "FAILED",
    )
)


def serialize_json(value: RetrieverStatus) -> str:
    return value


def deserialize_json(data: str) -> RetrieverStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetrieverStatus value: {data!r}")
    return cast(RetrieverStatus, data)
