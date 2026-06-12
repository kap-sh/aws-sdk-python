"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

Status: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: Status) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
