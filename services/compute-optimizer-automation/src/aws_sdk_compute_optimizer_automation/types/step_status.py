"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StepStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

StepStatus: TypeAlias = Literal[
    "Ready",
    "InProgress",
    "Complete",
    "Failed",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ready",
        "InProgress",
        "Complete",
        "Failed",
    )
)


def serialize_aws_json_1_0(value: StepStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StepStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepStatus value: {data!r}")
    return cast(StepStatus, data)
