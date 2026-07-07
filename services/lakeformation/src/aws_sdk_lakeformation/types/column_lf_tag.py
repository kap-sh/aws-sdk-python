"""Generated from Smithy shape ``com.amazonaws.lakeformation#ColumnLFTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lf_tags_list
    import aws_sdk_lakeformation.types.name_string


class ColumnLFTag(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lakeformation.types.name_string.NameString"]
    """<p>The name of a column resource.</p>"""
    lf_tags: NotRequired["aws_sdk_lakeformation.types.lf_tags_list.LFTagsList"]
    """<p>The LF-tags attached to a column resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnLFTag) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "lf_tags" in value:
        import aws_sdk_lakeformation.types.lf_tags_list

        out["LFTags"] = aws_sdk_lakeformation.types.lf_tags_list.serialize_json(
            value["lf_tags"]
        )
    return out


def deserialize_json(data: dict) -> ColumnLFTag:
    out: ColumnLFTag = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LFTags" in data:
        import aws_sdk_lakeformation.types.lf_tags_list

        out["lf_tags"] = aws_sdk_lakeformation.types.lf_tags_list.deserialize_json(
            data["LFTags"]
        )
    return out
