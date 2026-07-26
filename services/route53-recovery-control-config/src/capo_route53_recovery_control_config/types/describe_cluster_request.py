"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DescribeClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string


class DescribeClusterRequest(TypedDict, closed=True):
    cluster_arn: "capo_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeClusterRequest:
    out: DescribeClusterRequest = {}  # type: ignore[typeddict-item]
    return out
