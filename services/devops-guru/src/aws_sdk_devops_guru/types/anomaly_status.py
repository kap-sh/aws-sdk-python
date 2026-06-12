"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

AnomalyStatus: TypeAlias = Literal[
    "ONGOING",
    "CLOSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONGOING",
        "CLOSED",
    )
)


def serialize_json(value: AnomalyStatus) -> str:
    return value


def deserialize_json(data: str) -> AnomalyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnomalyStatus value: {data!r}")
    return cast(AnomalyStatus, data)
