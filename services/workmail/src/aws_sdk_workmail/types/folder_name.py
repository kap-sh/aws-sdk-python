"""Generated from Smithy shape ``com.amazonaws.workmail#FolderName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

FolderName: TypeAlias = Literal[
    "INBOX",
    "DELETED_ITEMS",
    "SENT_ITEMS",
    "DRAFTS",
    "JUNK_EMAIL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INBOX",
        "DELETED_ITEMS",
        "SENT_ITEMS",
        "DRAFTS",
        "JUNK_EMAIL",
    )
)


def serialize_aws_json_1_1(value: FolderName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FolderName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FolderName value: {data!r}")
    return cast(FolderName, data)
