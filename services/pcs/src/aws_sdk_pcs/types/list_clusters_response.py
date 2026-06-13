"""Generated from Smithy shape ``com.amazonaws.pcs#ListClustersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pcs.types.cluster_list


class ListClustersResponse(TypedDict):
    clusters: "aws_sdk_pcs.types.cluster_list.ClusterList"
    """<p>The list of clusters.</p>"""
    next_token: NotRequired["str"]
    """<p>The value of <code>nextToken</code> is a unique pagination token for each page of results returned. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListClustersResponse) -> dict:
    out: dict = {}
    import aws_sdk_pcs.types.cluster_list

    out["clusters"] = aws_sdk_pcs.types.cluster_list.serialize_aws_json_1_0(
        value["clusters"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListClustersResponse:
    out: ListClustersResponse = {}  # type: ignore[typeddict-item]
    if "clusters" in data:
        import aws_sdk_pcs.types.cluster_list

        out["clusters"] = aws_sdk_pcs.types.cluster_list.deserialize_aws_json_1_0(
            data["clusters"]
        )
    else:
        raise DeserializationError("ListClustersResponse.clusters required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
