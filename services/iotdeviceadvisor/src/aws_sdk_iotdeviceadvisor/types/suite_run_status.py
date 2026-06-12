"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#SuiteRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotdeviceadvisor.errors import DeserializationError

SuiteRunStatus: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "CANCELED",
    "PENDING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "PASS_WITH_WARNINGS",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASS",
        "FAIL",
        "CANCELED",
        "PENDING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
        "PASS_WITH_WARNINGS",
        "ERROR",
    )
)


def serialize_json(value: SuiteRunStatus) -> str:
    return value


def deserialize_json(data: str) -> SuiteRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SuiteRunStatus value: {data!r}")
    return cast(SuiteRunStatus, data)
