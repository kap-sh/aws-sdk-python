"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListLFTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.lf_tags_list
    import capo_lakeformation.types.token


class ListLFTagsResponse(TypedDict, closed=True):
    lf_tags: NotRequired["capo_lakeformation.types.lf_tags_list.LFTagsList"]
    """<p>A list of LF-tags that the requested has permission to view.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, present if the current list segment is not the last.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLFTagsResponse) -> dict:
    out: dict = {}
    if "lf_tags" in value:
        import capo_lakeformation.types.lf_tags_list

        out["LFTags"] = capo_lakeformation.types.lf_tags_list.serialize_json(
            value["lf_tags"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLFTagsResponse:
    out: ListLFTagsResponse = {}  # type: ignore[typeddict-item]
    if "LFTags" in data:
        import capo_lakeformation.types.lf_tags_list

        out["lf_tags"] = capo_lakeformation.types.lf_tags_list.deserialize_json(
            data["LFTags"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
