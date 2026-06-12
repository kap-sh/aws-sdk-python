"""Generated from Smithy shape ``com.amazonaws.deadline#DesiredWorkerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

DesiredWorkerStatus: TypeAlias = Literal["STOPPED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STOPPED",))


def serialize_json(value: DesiredWorkerStatus) -> str:
    return value


def deserialize_json(data: str) -> DesiredWorkerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DesiredWorkerStatus value: {data!r}")
    return cast(DesiredWorkerStatus, data)
