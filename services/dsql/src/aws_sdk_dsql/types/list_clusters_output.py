"""Generated from Smithy shape ``com.amazonaws.dsql#ListClustersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_list
    import aws_sdk_dsql.types.next_token


class ListClustersOutput(TypedDict):
    next_token: NotRequired["aws_sdk_dsql.types.next_token.NextToken"]
    """<p>If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.</p>"""
    clusters: "aws_sdk_dsql.types.cluster_list.ClusterList"
    """<p>An array of the returned clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_dsql.types.cluster_list

    out["clusters"] = aws_sdk_dsql.types.cluster_list.serialize_json(value["clusters"])
    return out


def deserialize_json(data: dict) -> ListClustersOutput:
    out: ListClustersOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "clusters" in data:
        import aws_sdk_dsql.types.cluster_list

        out["clusters"] = aws_sdk_dsql.types.cluster_list.deserialize_json(
            data["clusters"]
        )
    else:
        raise DeserializationError("ListClustersOutput.clusters required")
    return out
