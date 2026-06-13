"""Generated from Smithy shape ``com.amazonaws.emr#AdjustmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

AdjustmentType: TypeAlias = Literal[
    "CHANGE_IN_CAPACITY",
    "PERCENT_CHANGE_IN_CAPACITY",
    "EXACT_CAPACITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHANGE_IN_CAPACITY",
        "PERCENT_CHANGE_IN_CAPACITY",
        "EXACT_CAPACITY",
    )
)


def serialize_aws_json_1_1(value: AdjustmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdjustmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdjustmentType value: {data!r}")
    return cast(AdjustmentType, data)
