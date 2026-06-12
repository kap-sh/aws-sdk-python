"""Generated from Smithy shape ``com.amazonaws.transfer#CustomStepStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

CustomStepStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAILURE",
    )
)


def serialize_aws_json_1_1(value: CustomStepStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomStepStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomStepStatus value: {data!r}")
    return cast(CustomStepStatus, data)
