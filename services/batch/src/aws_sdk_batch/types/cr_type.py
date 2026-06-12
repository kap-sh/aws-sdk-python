"""Generated from Smithy shape ``com.amazonaws.batch#CRType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

CRType: TypeAlias = Literal[
    "EC2",
    "SPOT",
    "FARGATE",
    "FARGATE_SPOT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "SPOT",
        "FARGATE",
        "FARGATE_SPOT",
    )
)


def serialize_json(value: CRType) -> str:
    return value


def deserialize_json(data: str) -> CRType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CRType value: {data!r}")
    return cast(CRType, data)
