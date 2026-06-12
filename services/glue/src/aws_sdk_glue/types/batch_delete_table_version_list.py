"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeleteTableVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.version_string

BatchDeleteTableVersionList: TypeAlias = list[
    "aws_sdk_glue.types.version_string.VersionString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteTableVersionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BatchDeleteTableVersionList:
    return list(data)
