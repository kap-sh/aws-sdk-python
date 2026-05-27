"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeClustersResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.clusters
    import aws_sdk_ecs.types.failures


class DescribeClustersResponse(TypedDict):
    clusters: NotRequired["aws_sdk_ecs.types.clusters.Clusters"]
    """<p>The list of clusters.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
