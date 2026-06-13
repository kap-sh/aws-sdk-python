"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#EnrollmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

EnrollmentStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


def serialize_aws_json_1_0(value: EnrollmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnrollmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnrollmentStatus value: {data!r}")
    return cast(EnrollmentStatus, data)
