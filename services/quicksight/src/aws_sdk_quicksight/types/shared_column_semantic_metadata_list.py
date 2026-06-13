"""Generated from Smithy shape ``com.amazonaws.quicksight#SharedColumnSemanticMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.shared_column_semantic_metadata

SharedColumnSemanticMetadataList: TypeAlias = list[
    "aws_sdk_quicksight.types.shared_column_semantic_metadata.SharedColumnSemanticMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: SharedColumnSemanticMetadataList) -> list:
    import aws_sdk_quicksight.types.shared_column_semantic_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.shared_column_semantic_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SharedColumnSemanticMetadataList:
    import aws_sdk_quicksight.types.shared_column_semantic_metadata

    out: SharedColumnSemanticMetadataList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.shared_column_semantic_metadata.deserialize_json(
                item
            )
        )
    return out
