"""Generated from Smithy shape ``com.amazonaws.ecs#ListClustersResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListClustersResponse(TypedDict):
    cluster_arns: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of full Amazon Resource Name (ARN) entries for each cluster that's associated with your account.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListClusters</code> request. When the results of a <code>ListClusters</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClustersResponse) -> dict:
    out: dict = {}
    if "cluster_arns" in value:
        import aws_sdk_ecs.types.string_list

        out["clusterArns"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["cluster_arns"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClustersResponse:
    out: ListClustersResponse = {}  # type: ignore[typeddict-item]
    if "clusterArns" in data:
        import aws_sdk_ecs.types.string_list

        out["cluster_arns"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["clusterArns"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
