"""Generated from Smithy shape ``com.amazonaws.glue#JobBookmarksEncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

JobBookmarksEncryptionMode: TypeAlias = Literal[
    "DISABLED",
    "CSE-KMS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "CSE-KMS",
    )
)


def serialize_aws_json_1_1(value: JobBookmarksEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobBookmarksEncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown JobBookmarksEncryptionMode value: {data!r}"
        )
    return cast(JobBookmarksEncryptionMode, data)
