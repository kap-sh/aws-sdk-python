"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveBooleanEmailAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

ArchiveBooleanEmailAttribute: TypeAlias = Literal["HAS_ATTACHMENTS",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("HAS_ATTACHMENTS",))


def serialize_aws_json_1_0(value: ArchiveBooleanEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveBooleanEmailAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ArchiveBooleanEmailAttribute value: {data!r}"
        )
    return cast(ArchiveBooleanEmailAttribute, data)
