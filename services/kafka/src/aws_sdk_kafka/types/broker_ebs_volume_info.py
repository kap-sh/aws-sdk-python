"""Generated from Smithy shape ``com.amazonaws.kafka#BrokerEBSVolumeInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.provisioned_throughput


class BrokerEBSVolumeInfo(TypedDict):
    kafka_broker_node_id: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The ID of the broker to update.</p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_kafka.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>EBS volume provisioned throughput information.</p>"""
    volume_size_gb: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>Size of the EBS volume to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerEBSVolumeInfo) -> dict:
    out: dict = {}
    if "kafka_broker_node_id" in value:
        out["kafkaBrokerNodeId"] = value["kafka_broker_node_id"]
    if "provisioned_throughput" in value:
        import aws_sdk_kafka.types.provisioned_throughput

        out["provisionedThroughput"] = (
            aws_sdk_kafka.types.provisioned_throughput.serialize_json(
                value["provisioned_throughput"]
            )
        )
    if "volume_size_gb" in value:
        out["volumeSizeGB"] = value["volume_size_gb"]
    return out


def deserialize_json(data: dict) -> BrokerEBSVolumeInfo:
    out: BrokerEBSVolumeInfo = {}  # type: ignore[typeddict-item]
    if "kafkaBrokerNodeId" in data:
        out["kafka_broker_node_id"] = data["kafkaBrokerNodeId"]
    if "provisionedThroughput" in data:
        import aws_sdk_kafka.types.provisioned_throughput

        out["provisioned_throughput"] = (
            aws_sdk_kafka.types.provisioned_throughput.deserialize_json(
                data["provisionedThroughput"]
            )
        )
    if "volumeSizeGB" in data:
        out["volume_size_gb"] = data["volumeSizeGB"]
    return out
