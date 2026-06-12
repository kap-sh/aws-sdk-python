"""Generated from Smithy shape ``com.amazonaws.ssm#StopType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

StopType: TypeAlias = Literal[
    "Complete",
    "Cancel",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Complete",
        "Cancel",
    )
)


def serialize_aws_json_1_1(value: StopType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StopType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StopType value: {data!r}")
    return cast(StopType, data)
