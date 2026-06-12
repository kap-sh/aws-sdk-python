"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#AcceptCodeValidation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_contacts.errors import DeserializationError

AcceptCodeValidation: TypeAlias = Literal[
    "IGNORE",
    "ENFORCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORE",
        "ENFORCE",
    )
)


def serialize_aws_json_1_1(value: AcceptCodeValidation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceptCodeValidation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceptCodeValidation value: {data!r}")
    return cast(AcceptCodeValidation, data)
