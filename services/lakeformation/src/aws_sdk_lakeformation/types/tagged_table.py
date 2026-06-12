"""Generated from Smithy shape ``com.amazonaws.lakeformation#TaggedTable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.column_lf_tags_list
    import aws_sdk_lakeformation.types.lf_tags_list
    import aws_sdk_lakeformation.types.table_resource


class TaggedTable(TypedDict):
    table: NotRequired["aws_sdk_lakeformation.types.table_resource.TableResource"]
    """<p>A table that has LF-tags attached to it.</p>"""
    lf_tag_on_database: NotRequired[
        "aws_sdk_lakeformation.types.lf_tags_list.LFTagsList"
    ]
    """<p>A list of LF-tags attached to the database where the table resides.</p>"""
    lf_tags_on_table: NotRequired["aws_sdk_lakeformation.types.lf_tags_list.LFTagsList"]
    """<p>A list of LF-tags attached to the table.</p>"""
    lf_tags_on_columns: NotRequired[
        "aws_sdk_lakeformation.types.column_lf_tags_list.ColumnLFTagsList"
    ]
    """<p>A list of LF-tags attached to columns in the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaggedTable) -> dict:
    out: dict = {}
    if "table" in value:
        import aws_sdk_lakeformation.types.table_resource

        out["Table"] = aws_sdk_lakeformation.types.table_resource.serialize_json(
            value["table"]
        )
    if "lf_tag_on_database" in value:
        import aws_sdk_lakeformation.types.lf_tags_list

        out["LFTagOnDatabase"] = (
            aws_sdk_lakeformation.types.lf_tags_list.serialize_json(
                value["lf_tag_on_database"]
            )
        )
    if "lf_tags_on_table" in value:
        import aws_sdk_lakeformation.types.lf_tags_list

        out["LFTagsOnTable"] = aws_sdk_lakeformation.types.lf_tags_list.serialize_json(
            value["lf_tags_on_table"]
        )
    if "lf_tags_on_columns" in value:
        import aws_sdk_lakeformation.types.column_lf_tags_list

        out["LFTagsOnColumns"] = (
            aws_sdk_lakeformation.types.column_lf_tags_list.serialize_json(
                value["lf_tags_on_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> TaggedTable:
    out: TaggedTable = {}  # type: ignore[typeddict-item]
    if "Table" in data:
        import aws_sdk_lakeformation.types.table_resource

        out["table"] = aws_sdk_lakeformation.types.table_resource.deserialize_json(
            data["Table"]
        )
    if "LFTagOnDatabase" in data:
        import aws_sdk_lakeformation.types.lf_tags_list

        out["lf_tag_on_database"] = (
            aws_sdk_lakeformation.types.lf_tags_list.deserialize_json(
                data["LFTagOnDatabase"]
            )
        )
    if "LFTagsOnTable" in data:
        import aws_sdk_lakeformation.types.lf_tags_list

        out["lf_tags_on_table"] = (
            aws_sdk_lakeformation.types.lf_tags_list.deserialize_json(
                data["LFTagsOnTable"]
            )
        )
    if "LFTagsOnColumns" in data:
        import aws_sdk_lakeformation.types.column_lf_tags_list

        out["lf_tags_on_columns"] = (
            aws_sdk_lakeformation.types.column_lf_tags_list.deserialize_json(
                data["LFTagsOnColumns"]
            )
        )
    return out
