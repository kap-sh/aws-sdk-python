"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListVirtualClustersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.next_token
    import aws_sdk_emr_containers.types.virtual_clusters


class ListVirtualClustersResponse(TypedDict):
    virtual_clusters: NotRequired[
        "aws_sdk_emr_containers.types.virtual_clusters.VirtualClusters"
    ]
    """<p>This output lists the specified virtual clusters.</p>"""
    next_token: NotRequired["aws_sdk_emr_containers.types.next_token.NextToken"]
    """<p>This output displays the token for the next set of virtual clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVirtualClustersResponse) -> dict:
    out: dict = {}
    if "virtual_clusters" in value:
        import aws_sdk_emr_containers.types.virtual_clusters

        out["virtualClusters"] = (
            aws_sdk_emr_containers.types.virtual_clusters.serialize_json(
                value["virtual_clusters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVirtualClustersResponse:
    out: ListVirtualClustersResponse = {}  # type: ignore[typeddict-item]
    if "virtualClusters" in data:
        import aws_sdk_emr_containers.types.virtual_clusters

        out["virtual_clusters"] = (
            aws_sdk_emr_containers.types.virtual_clusters.deserialize_json(
                data["virtualClusters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
