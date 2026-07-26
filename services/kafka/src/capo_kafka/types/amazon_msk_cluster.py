"""Generated from Smithy shape ``com.amazonaws.kafka#AmazonMskCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class AmazonMskCluster(TypedDict, closed=True):
    msk_cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of an Amazon MSK cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMskCluster) -> dict:
    out: dict = {}
    if "msk_cluster_arn" in value:
        out["mskClusterArn"] = value["msk_cluster_arn"]
    return out


def deserialize_json(data: dict) -> AmazonMskCluster:
    out: AmazonMskCluster = {}  # type: ignore[typeddict-item]
    if "mskClusterArn" in data:
        out["msk_cluster_arn"] = data["mskClusterArn"]
    return out
