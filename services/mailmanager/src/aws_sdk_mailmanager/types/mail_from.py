"""Generated from Smithy shape ``com.amazonaws.mailmanager#MailFrom``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

MailFrom: TypeAlias = Literal[
    "REPLACE",
    "PRESERVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REPLACE",
        "PRESERVE",
    )
)


def serialize_aws_json_1_0(value: MailFrom) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MailFrom:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MailFrom value: {data!r}")
    return cast(MailFrom, data)
