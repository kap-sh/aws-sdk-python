"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DescribeClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.cluster


class DescribeClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_route53_recovery_control_config.types.cluster.Cluster"]
    """<p>The cluster for the DescribeCluster request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_route53_recovery_control_config.types.cluster

        out["Cluster"] = (
            capo_route53_recovery_control_config.types.cluster.serialize_json(
                value["cluster"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeClusterResponse:
    out: DescribeClusterResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import capo_route53_recovery_control_config.types.cluster

        out["cluster"] = (
            capo_route53_recovery_control_config.types.cluster.deserialize_json(
                data["Cluster"]
            )
        )
    return out
