"""Generated from Smithy shape ``com.amazonaws.workmail#FolderName``."""

from typing import Literal, TypeAlias, cast

FolderName: TypeAlias = Literal[
    "INBOX",
    "DELETED_ITEMS",
    "SENT_ITEMS",
    "DRAFTS",
    "JUNK_EMAIL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FolderName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FolderName:
    return cast(FolderName, data)
