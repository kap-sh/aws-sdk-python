"""Generated from Smithy shape ``com.amazonaws.emr#CancelStepsRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

CancelStepsRequestStatus: TypeAlias = Literal[
    "SUBMITTED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: CancelStepsRequestStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CancelStepsRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CancelStepsRequestStatus value: {data!r}")
    return cast(CancelStepsRequestStatus, data)
