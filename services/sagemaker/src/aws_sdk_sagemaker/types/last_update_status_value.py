"""Generated from Smithy shape ``com.amazonaws.sagemaker#LastUpdateStatusValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

LastUpdateStatusValue: TypeAlias = Literal[
    "Successful",
    "Failed",
    "InProgress",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Successful",
        "Failed",
        "InProgress",
    )
)


def serialize_aws_json_1_1(value: LastUpdateStatusValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastUpdateStatusValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LastUpdateStatusValue value: {data!r}")
    return cast(LastUpdateStatusValue, data)
