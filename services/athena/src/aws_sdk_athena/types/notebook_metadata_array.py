"""Generated from Smithy shape ``com.amazonaws.athena#NotebookMetadataArray``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.notebook_metadata

NotebookMetadataArray: TypeAlias = list[
    "aws_sdk_athena.types.notebook_metadata.NotebookMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookMetadataArray) -> list:
    import aws_sdk_athena.types.notebook_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.notebook_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NotebookMetadataArray:
    import aws_sdk_athena.types.notebook_metadata

    out: NotebookMetadataArray = []
    for item in data:
        out.append(
            aws_sdk_athena.types.notebook_metadata.deserialize_aws_json_1_1(item)
        )
    return out
