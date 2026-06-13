"""Generated from Smithy shape ``com.amazonaws.quicksight#TableSemanticMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.shared_column_semantic_metadata_list


class TableSemanticMetadata(TypedDict):
    column_metadata: NotRequired[
        "aws_sdk_quicksight.types.shared_column_semantic_metadata_list.SharedColumnSemanticMetadataList"
    ]
    """<p>A list of column semantic metadata entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableSemanticMetadata) -> dict:
    out: dict = {}
    if "column_metadata" in value:
        import aws_sdk_quicksight.types.shared_column_semantic_metadata_list

        out["ColumnMetadata"] = (
            aws_sdk_quicksight.types.shared_column_semantic_metadata_list.serialize_json(
                value["column_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableSemanticMetadata:
    out: TableSemanticMetadata = {}  # type: ignore[typeddict-item]
    if "ColumnMetadata" in data:
        import aws_sdk_quicksight.types.shared_column_semantic_metadata_list

        out["column_metadata"] = (
            aws_sdk_quicksight.types.shared_column_semantic_metadata_list.deserialize_json(
                data["ColumnMetadata"]
            )
        )
    return out
