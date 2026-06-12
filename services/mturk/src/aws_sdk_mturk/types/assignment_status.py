"""Generated from Smithy shape ``com.amazonaws.mturk#AssignmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

AssignmentStatus: TypeAlias = Literal[
    "Submitted",
    "Approved",
    "Rejected",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Submitted",
        "Approved",
        "Rejected",
    )
)


def serialize_aws_json_1_1(value: AssignmentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssignmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssignmentStatus value: {data!r}")
    return cast(AssignmentStatus, data)
