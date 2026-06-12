"""Generated from Smithy shape ``com.amazonaws.kafka#AmazonMskCluster``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class AmazonMskCluster(TypedDict):
    msk_cluster_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
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
