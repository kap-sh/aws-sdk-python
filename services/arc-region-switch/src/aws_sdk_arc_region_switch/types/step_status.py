"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#StepStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

StepStatus: TypeAlias = Literal[
    "notStarted",
    "running",
    "failed",
    "completed",
    "canceled",
    "skipped",
    "pendingApproval",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "notStarted",
        "running",
        "failed",
        "completed",
        "canceled",
        "skipped",
        "pendingApproval",
    )
)


def serialize_aws_json_1_0(value: StepStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StepStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepStatus value: {data!r}")
    return cast(StepStatus, data)
