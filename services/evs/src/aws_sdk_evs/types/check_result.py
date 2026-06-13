"""Generated from Smithy shape ``com.amazonaws.evs#CheckResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

CheckResult: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "UNKNOWN",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "FAILED",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_0(value: CheckResult) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CheckResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CheckResult value: {data!r}")
    return cast(CheckResult, data)
