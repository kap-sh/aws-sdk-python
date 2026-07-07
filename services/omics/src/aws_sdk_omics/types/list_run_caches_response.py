"""Generated from Smithy shape ``com.amazonaws.omics#ListRunCachesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.list_token
    import aws_sdk_omics.types.run_cache_list


class ListRunCachesResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_omics.types.run_cache_list.RunCacheList"]
    """<p>Details about each run cache in the response.</p>"""
    next_token: NotRequired["aws_sdk_omics.types.list_token.ListToken"]
    """<p>Pagination token to retrieve additional run caches. If the response does not have a <code>nextToken</code>value, you have reached to the end of the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunCachesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_omics.types.run_cache_list

        out["items"] = aws_sdk_omics.types.run_cache_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRunCachesResponse:
    out: ListRunCachesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_omics.types.run_cache_list

        out["items"] = aws_sdk_omics.types.run_cache_list.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
