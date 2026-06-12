"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#AcceptType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_contacts.errors import DeserializationError

AcceptType: TypeAlias = Literal[
    "DELIVERED",
    "READ",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELIVERED",
        "READ",
    )
)


def serialize_aws_json_1_1(value: AcceptType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceptType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceptType value: {data!r}")
    return cast(AcceptType, data)
