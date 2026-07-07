"""Generated from Smithy shape ``com.amazonaws.quicksight#SemanticModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_semantic_metadata_list
    import aws_sdk_quicksight.types.semantic_table_map


class SemanticModelConfiguration(TypedDict, closed=True):
    table_map: NotRequired[
        "aws_sdk_quicksight.types.semantic_table_map.SemanticTableMap"
    ]
    """<p>A map of semantic tables that define the analytical structure.</p>"""
    semantic_metadata: NotRequired[
        "aws_sdk_quicksight.types.data_set_semantic_metadata_list.DataSetSemanticMetadataList"
    ]
    """<p>The dataset-level semantic metadata, including a description and custom instructions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticModelConfiguration) -> dict:
    out: dict = {}
    if "table_map" in value:
        import aws_sdk_quicksight.types.semantic_table_map

        out["TableMap"] = aws_sdk_quicksight.types.semantic_table_map.serialize_json(
            value["table_map"]
        )
    if "semantic_metadata" in value:
        import aws_sdk_quicksight.types.data_set_semantic_metadata_list

        out["SemanticMetadata"] = (
            aws_sdk_quicksight.types.data_set_semantic_metadata_list.serialize_json(
                value["semantic_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SemanticModelConfiguration:
    out: SemanticModelConfiguration = {}  # type: ignore[typeddict-item]
    if "TableMap" in data:
        import aws_sdk_quicksight.types.semantic_table_map

        out["table_map"] = aws_sdk_quicksight.types.semantic_table_map.deserialize_json(
            data["TableMap"]
        )
    if "SemanticMetadata" in data:
        import aws_sdk_quicksight.types.data_set_semantic_metadata_list

        out["semantic_metadata"] = (
            aws_sdk_quicksight.types.data_set_semantic_metadata_list.deserialize_json(
                data["SemanticMetadata"]
            )
        )
    return out
