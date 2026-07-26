"""Generated from Smithy shape ``com.amazonaws.lakeformation#SearchDatabasesByLFTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.database_lf_tags_list
    import capo_lakeformation.types.token


class SearchDatabasesByLFTagsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, present if the current list segment is not the last.</p>"""
    database_list: NotRequired[
        "capo_lakeformation.types.database_lf_tags_list.DatabaseLFTagsList"
    ]
    """<p>A list of databases that meet the LF-tag conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDatabasesByLFTagsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "database_list" in value:
        import capo_lakeformation.types.database_lf_tags_list

        out["DatabaseList"] = (
            capo_lakeformation.types.database_lf_tags_list.serialize_json(
                value["database_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchDatabasesByLFTagsResponse:
    out: SearchDatabasesByLFTagsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DatabaseList" in data:
        import capo_lakeformation.types.database_lf_tags_list

        out["database_list"] = (
            capo_lakeformation.types.database_lf_tags_list.deserialize_json(
                data["DatabaseList"]
            )
        )
    return out
