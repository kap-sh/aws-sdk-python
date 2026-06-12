"""Generated from Smithy shape ``com.amazonaws.wafv2#SizeInspectionLimit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

SizeInspectionLimit: TypeAlias = Literal[
    "KB_16",
    "KB_32",
    "KB_48",
    "KB_64",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KB_16",
        "KB_32",
        "KB_48",
        "KB_64",
    )
)


def serialize_aws_json_1_1(value: SizeInspectionLimit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SizeInspectionLimit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SizeInspectionLimit value: {data!r}")
    return cast(SizeInspectionLimit, data)
