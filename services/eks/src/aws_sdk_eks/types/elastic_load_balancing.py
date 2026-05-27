"""Generated from Smithy shape ``com.amazonaws.eks#ElasticLoadBalancing``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean


class ElasticLoadBalancing(TypedDict):
    enabled: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates if the load balancing capability is enabled on your EKS Auto Mode cluster. If the load balancing capability is enabled, EKS Auto Mode will create and delete load balancers in your Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticLoadBalancing) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ElasticLoadBalancing:
    out: ElasticLoadBalancing = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
