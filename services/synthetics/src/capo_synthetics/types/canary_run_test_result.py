"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunTestResult``."""

from typing import Literal, TypeAlias, cast

CanaryRunTestResult: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRunTestResult) -> str:
    return value


def deserialize_json(data: str) -> CanaryRunTestResult:
    return cast(CanaryRunTestResult, data)
