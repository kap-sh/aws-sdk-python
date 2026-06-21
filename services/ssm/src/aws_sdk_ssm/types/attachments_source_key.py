"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentsSourceKey``."""

from typing import Literal, TypeAlias, cast

AttachmentsSourceKey: TypeAlias = Literal[
    "SourceUrl",
    "S3FileUrl",
    "AttachmentReference",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentsSourceKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttachmentsSourceKey:
    return cast(AttachmentsSourceKey, data)
