"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EnrollmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

EnrollmentStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
    "Pending",
    "Failed",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
        "Pending",
        "Failed",
    )
)


def serialize_aws_json_1_0(value: EnrollmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnrollmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnrollmentStatus value: {data!r}")
    return cast(EnrollmentStatus, data)
