"""Generated from Smithy shape ``com.amazonaws.evs#CheckResult``."""

from typing import Literal, TypeAlias, cast

CheckResult: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "UNKNOWN",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CheckResult) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CheckResult:
    return cast(CheckResult, data)
