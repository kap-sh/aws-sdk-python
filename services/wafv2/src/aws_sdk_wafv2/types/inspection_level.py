"""Generated from Smithy shape ``com.amazonaws.wafv2#InspectionLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

InspectionLevel: TypeAlias = Literal[
    "COMMON",
    "TARGETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMMON",
        "TARGETED",
    )
)


def serialize_aws_json_1_1(value: InspectionLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InspectionLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InspectionLevel value: {data!r}")
    return cast(InspectionLevel, data)
