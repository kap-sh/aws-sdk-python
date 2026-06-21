"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#SuiteRunStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SuiteRunStatus) -> str:
    return value


def deserialize_json(data: str) -> SuiteRunStatus:
    return cast(SuiteRunStatus, data)
