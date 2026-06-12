"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.next_token
    import aws_sdk_opensearch.types.version_list


class ListVersionsResponse(TypedDict):
    versions: NotRequired["aws_sdk_opensearch.types.version_list.VersionList"]
    """<p>A list of all versions of OpenSearch and Elasticsearch that Amazon OpenSearch Service supports.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsResponse) -> dict:
    out: dict = {}
    if "versions" in value:
        import aws_sdk_opensearch.types.version_list

        out["Versions"] = aws_sdk_opensearch.types.version_list.serialize_json(
            value["versions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVersionsResponse:
    out: ListVersionsResponse = {}  # type: ignore[typeddict-item]
    if "Versions" in data:
        import aws_sdk_opensearch.types.version_list

        out["versions"] = aws_sdk_opensearch.types.version_list.deserialize_json(
            data["Versions"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
