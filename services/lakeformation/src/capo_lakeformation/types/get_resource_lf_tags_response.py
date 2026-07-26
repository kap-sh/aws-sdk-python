"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetResourceLFTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.column_lf_tags_list
    import capo_lakeformation.types.lf_tags_list


class GetResourceLFTagsResponse(TypedDict, closed=True):
    lf_tag_on_database: NotRequired["capo_lakeformation.types.lf_tags_list.LFTagsList"]
    """<p>A list of LF-tags applied to a database resource.</p>"""
    lf_tags_on_table: NotRequired["capo_lakeformation.types.lf_tags_list.LFTagsList"]
    """<p>A list of LF-tags applied to a table resource.</p>"""
    lf_tags_on_columns: NotRequired[
        "capo_lakeformation.types.column_lf_tags_list.ColumnLFTagsList"
    ]
    """<p>A list of LF-tags applied to a column resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceLFTagsResponse) -> dict:
    out: dict = {}
    if "lf_tag_on_database" in value:
        import capo_lakeformation.types.lf_tags_list

        out["LFTagOnDatabase"] = capo_lakeformation.types.lf_tags_list.serialize_json(
            value["lf_tag_on_database"]
        )
    if "lf_tags_on_table" in value:
        import capo_lakeformation.types.lf_tags_list

        out["LFTagsOnTable"] = capo_lakeformation.types.lf_tags_list.serialize_json(
            value["lf_tags_on_table"]
        )
    if "lf_tags_on_columns" in value:
        import capo_lakeformation.types.column_lf_tags_list

        out["LFTagsOnColumns"] = (
            capo_lakeformation.types.column_lf_tags_list.serialize_json(
                value["lf_tags_on_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetResourceLFTagsResponse:
    out: GetResourceLFTagsResponse = {}  # type: ignore[typeddict-item]
    if "LFTagOnDatabase" in data:
        import capo_lakeformation.types.lf_tags_list

        out["lf_tag_on_database"] = (
            capo_lakeformation.types.lf_tags_list.deserialize_json(
                data["LFTagOnDatabase"]
            )
        )
    if "LFTagsOnTable" in data:
        import capo_lakeformation.types.lf_tags_list

        out["lf_tags_on_table"] = (
            capo_lakeformation.types.lf_tags_list.deserialize_json(
                data["LFTagsOnTable"]
            )
        )
    if "LFTagsOnColumns" in data:
        import capo_lakeformation.types.column_lf_tags_list

        out["lf_tags_on_columns"] = (
            capo_lakeformation.types.column_lf_tags_list.deserialize_json(
                data["LFTagsOnColumns"]
            )
        )
    return out
