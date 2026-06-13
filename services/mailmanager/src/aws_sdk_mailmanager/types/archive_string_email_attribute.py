"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveStringEmailAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

ArchiveStringEmailAttribute: TypeAlias = Literal[
    "TO",
    "FROM",
    "CC",
    "SUBJECT",
    "ENVELOPE_TO",
    "ENVELOPE_FROM",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TO",
        "FROM",
        "CC",
        "SUBJECT",
        "ENVELOPE_TO",
        "ENVELOPE_FROM",
    )
)


def serialize_aws_json_1_0(value: ArchiveStringEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveStringEmailAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ArchiveStringEmailAttribute value: {data!r}"
        )
    return cast(ArchiveStringEmailAttribute, data)
