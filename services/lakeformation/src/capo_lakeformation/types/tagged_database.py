"""Generated from Smithy shape ``com.amazonaws.lakeformation#TaggedDatabase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.database_resource
    import capo_lakeformation.types.lf_tags_list


class TaggedDatabase(TypedDict, closed=True):
    database: NotRequired["capo_lakeformation.types.database_resource.DatabaseResource"]
    """<p>A database that has LF-tags attached to it.</p>"""
    lf_tags: NotRequired["capo_lakeformation.types.lf_tags_list.LFTagsList"]
    """<p>A list of LF-tags attached to the database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaggedDatabase) -> dict:
    out: dict = {}
    if "database" in value:
        import capo_lakeformation.types.database_resource

        out["Database"] = capo_lakeformation.types.database_resource.serialize_json(
            value["database"]
        )
    if "lf_tags" in value:
        import capo_lakeformation.types.lf_tags_list

        out["LFTags"] = capo_lakeformation.types.lf_tags_list.serialize_json(
            value["lf_tags"]
        )
    return out


def deserialize_json(data: dict) -> TaggedDatabase:
    out: TaggedDatabase = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        import capo_lakeformation.types.database_resource

        out["database"] = capo_lakeformation.types.database_resource.deserialize_json(
            data["Database"]
        )
    if "LFTags" in data:
        import capo_lakeformation.types.lf_tags_list

        out["lf_tags"] = capo_lakeformation.types.lf_tags_list.deserialize_json(
            data["LFTags"]
        )
    return out
