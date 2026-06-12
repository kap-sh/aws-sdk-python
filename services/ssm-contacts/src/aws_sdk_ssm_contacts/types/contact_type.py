"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ContactType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_contacts.errors import DeserializationError

ContactType: TypeAlias = Literal[
    "PERSONAL",
    "ESCALATION",
    "ONCALL_SCHEDULE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERSONAL",
        "ESCALATION",
        "ONCALL_SCHEDULE",
    )
)


def serialize_aws_json_1_1(value: ContactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactType value: {data!r}")
    return cast(ContactType, data)
