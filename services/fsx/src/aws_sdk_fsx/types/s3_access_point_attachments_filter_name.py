"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentsFilterName``."""

from typing import Literal, TypeAlias, cast

S3AccessPointAttachmentsFilterName: TypeAlias = Literal[
    "file-system-id",
    "volume-id",
    "type",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointAttachmentsFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3AccessPointAttachmentsFilterName:
    return cast(S3AccessPointAttachmentsFilterName, data)
