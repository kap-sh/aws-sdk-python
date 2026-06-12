"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentsSourceKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AttachmentsSourceKey: TypeAlias = Literal[
    "SourceUrl",
    "S3FileUrl",
    "AttachmentReference",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SourceUrl",
        "S3FileUrl",
        "AttachmentReference",
    )
)


def serialize_aws_json_1_1(value: AttachmentsSourceKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttachmentsSourceKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentsSourceKey value: {data!r}")
    return cast(AttachmentsSourceKey, data)
