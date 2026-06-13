"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#StatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_quicksetup.errors import DeserializationError

StatusType: TypeAlias = Literal[
    "Deployment",
    "AsyncExecutions",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Deployment",
        "AsyncExecutions",
    )
)


def serialize_json(value: StatusType) -> str:
    return value


def deserialize_json(data: str) -> StatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusType value: {data!r}")
    return cast(StatusType, data)
