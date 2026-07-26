"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetSemanticMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_semantic_metadata

DataSetSemanticMetadataList: TypeAlias = list[
    "capo_quicksight.types.data_set_semantic_metadata.DataSetSemanticMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSemanticMetadataList) -> list:
    import capo_quicksight.types.data_set_semantic_metadata

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.data_set_semantic_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataSetSemanticMetadataList:
    import capo_quicksight.types.data_set_semantic_metadata

    out: DataSetSemanticMetadataList = []
    for item in data:
        out.append(
            capo_quicksight.types.data_set_semantic_metadata.deserialize_json(item)
        )
    return out
