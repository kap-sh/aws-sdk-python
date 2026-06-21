"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportViewType``."""

from typing import Literal, TypeAlias, cast

ExportViewType: TypeAlias = Literal[
    "NEW_IMAGE",
    "NEW_AND_OLD_IMAGES",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportViewType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportViewType:
    return cast(ExportViewType, data)
