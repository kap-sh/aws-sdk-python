"""Generated from Smithy shape ``com.amazonaws.appfabric#ResultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appfabric.errors import DeserializationError

ResultStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "EXPIRED",
    )
)


def serialize_json(value: ResultStatus) -> str:
    return value


def deserialize_json(data: str) -> ResultStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResultStatus value: {data!r}")
    return cast(ResultStatus, data)
