"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TestCaseScenarioStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotdeviceadvisor.errors import DeserializationError

TestCaseScenarioStatus: TypeAlias = Literal[
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


def serialize_json(value: TestCaseScenarioStatus) -> str:
    return value


def deserialize_json(data: str) -> TestCaseScenarioStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestCaseScenarioStatus value: {data!r}")
    return cast(TestCaseScenarioStatus, data)
