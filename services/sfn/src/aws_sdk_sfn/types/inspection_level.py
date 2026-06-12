"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

InspectionLevel: TypeAlias = Literal[
    "INFO",
    "DEBUG",
    "TRACE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFO",
        "DEBUG",
        "TRACE",
    )
)


def serialize_aws_json_1_0(value: InspectionLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InspectionLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InspectionLevel value: {data!r}")
    return cast(InspectionLevel, data)
