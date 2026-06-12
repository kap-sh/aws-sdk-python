"""Generated from Smithy shape ``com.amazonaws.datasync#PhaseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

PhaseStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCESS",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: PhaseStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PhaseStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhaseStatus value: {data!r}")
    return cast(PhaseStatus, data)
