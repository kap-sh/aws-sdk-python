"""Generated from Smithy shape ``com.amazonaws.glue#ListDevEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string
    import capo_glue.types.page_size
    import capo_glue.types.tags_map


class ListDevEndpointsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if this is a continuation request.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum size of a list to return.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>Specifies to return only these tagged resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevEndpointsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevEndpointsRequest:
    out: ListDevEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Tags" in data:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
