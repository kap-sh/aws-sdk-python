"""Generated from Smithy shape ``com.amazonaws.inspector2#GetClustersForImageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cluster_for_image_filter_criteria
    import aws_sdk_inspector2.types.get_clusters_for_image_next_token


class GetClustersForImageRequest(TypedDict):
    filter: "aws_sdk_inspector2.types.cluster_for_image_filter_criteria.ClusterForImageFilterCriteria"
    """<p>The resource Id for the Amazon ECR image.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to be returned in a single page of results.</p>"""
    next_token: NotRequired[
        "aws_sdk_inspector2.types.get_clusters_for_image_next_token.GetClustersForImageNextToken"
    ]
    """<p>The pagination token from a previous request used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClustersForImageRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.cluster_for_image_filter_criteria

    out["filter"] = (
        aws_sdk_inspector2.types.cluster_for_image_filter_criteria.serialize_json(
            value["filter"]
        )
    )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetClustersForImageRequest:
    out: GetClustersForImageRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_inspector2.types.cluster_for_image_filter_criteria

        out["filter"] = (
            aws_sdk_inspector2.types.cluster_for_image_filter_criteria.deserialize_json(
                data["filter"]
            )
        )
    else:
        raise DeserializationError("GetClustersForImageRequest.filter required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
