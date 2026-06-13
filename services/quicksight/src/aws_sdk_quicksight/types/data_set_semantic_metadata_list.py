"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetSemanticMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_semantic_metadata

DataSetSemanticMetadataList: TypeAlias = list[
    "aws_sdk_quicksight.types.data_set_semantic_metadata.DataSetSemanticMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSemanticMetadataList) -> list:
    import aws_sdk_quicksight.types.data_set_semantic_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.data_set_semantic_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataSetSemanticMetadataList:
    import aws_sdk_quicksight.types.data_set_semantic_metadata

    out: DataSetSemanticMetadataList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.data_set_semantic_metadata.deserialize_json(item)
        )
    return out
