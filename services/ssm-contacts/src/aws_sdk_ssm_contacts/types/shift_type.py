"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ShiftType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_contacts.errors import DeserializationError

ShiftType: TypeAlias = Literal[
    "REGULAR",
    "OVERRIDDEN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGULAR",
        "OVERRIDDEN",
    )
)


def serialize_aws_json_1_1(value: ShiftType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShiftType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShiftType value: {data!r}")
    return cast(ShiftType, data)
