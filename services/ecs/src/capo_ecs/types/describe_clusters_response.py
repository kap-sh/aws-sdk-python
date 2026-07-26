"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeClustersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.clusters
    import capo_ecs.types.failures


class DescribeClustersResponse(TypedDict, closed=True):
    clusters: NotRequired["capo_ecs.types.clusters.Clusters"]
    """<p>The list of clusters.</p>"""
    failures: NotRequired["capo_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClustersResponse) -> dict:
    out: dict = {}
    if "clusters" in value:
        import capo_ecs.types.clusters

        out["clusters"] = capo_ecs.types.clusters.serialize_aws_json_1_1(
            value["clusters"]
        )
    if "failures" in value:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClustersResponse:
    out: DescribeClustersResponse = {}  # type: ignore[typeddict-item]
    if "clusters" in data:
        import capo_ecs.types.clusters

        out["clusters"] = capo_ecs.types.clusters.deserialize_aws_json_1_1(
            data["clusters"]
        )
    if "failures" in data:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
