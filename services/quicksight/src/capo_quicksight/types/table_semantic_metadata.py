"""Generated from Smithy shape ``com.amazonaws.quicksight#TableSemanticMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.shared_column_semantic_metadata_list


class TableSemanticMetadata(TypedDict, closed=True):
    column_metadata: NotRequired[
        "capo_quicksight.types.shared_column_semantic_metadata_list.SharedColumnSemanticMetadataList"
    ]
    """<p>A list of column semantic metadata entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableSemanticMetadata) -> dict:
    out: dict = {}
    if "column_metadata" in value:
        import capo_quicksight.types.shared_column_semantic_metadata_list

        out["ColumnMetadata"] = (
            capo_quicksight.types.shared_column_semantic_metadata_list.serialize_json(
                value["column_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableSemanticMetadata:
    out: TableSemanticMetadata = {}  # type: ignore[typeddict-item]
    if "ColumnMetadata" in data:
        import capo_quicksight.types.shared_column_semantic_metadata_list

        out["column_metadata"] = (
            capo_quicksight.types.shared_column_semantic_metadata_list.deserialize_json(
                data["ColumnMetadata"]
            )
        )
    return out
