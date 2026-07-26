"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.next_token
    import capo_opensearch.types.version_list


class ListVersionsResponse(TypedDict, closed=True):
    versions: NotRequired["capo_opensearch.types.version_list.VersionList"]
    """<p>A list of all versions of OpenSearch and Elasticsearch that Amazon OpenSearch Service supports.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsResponse) -> dict:
    out: dict = {}
    if "versions" in value:
        import capo_opensearch.types.version_list

        out["Versions"] = capo_opensearch.types.version_list.serialize_json(
            value["versions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVersionsResponse:
    out: ListVersionsResponse = {}  # type: ignore[typeddict-item]
    if "Versions" in data:
        import capo_opensearch.types.version_list

        out["versions"] = capo_opensearch.types.version_list.deserialize_json(
            data["Versions"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
