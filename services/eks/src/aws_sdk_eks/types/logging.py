"""Generated from Smithy shape ``com.amazonaws.eks#Logging``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.log_setups


class Logging(TypedDict):
    cluster_logging: NotRequired["aws_sdk_eks.types.log_setups.LogSetups"]
    """<p>The cluster control plane logging configuration for your cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Logging) -> dict:
    out: dict = {}
    if "cluster_logging" in value:
        import aws_sdk_eks.types.log_setups

        out["clusterLogging"] = aws_sdk_eks.types.log_setups.serialize_json(
            value["cluster_logging"]
        )
    return out


def deserialize_json(data: dict) -> Logging:
    out: Logging = {}  # type: ignore[typeddict-item]
    if "clusterLogging" in data:
        import aws_sdk_eks.types.log_setups

        out["cluster_logging"] = aws_sdk_eks.types.log_setups.deserialize_json(
            data["clusterLogging"]
        )
    return out
