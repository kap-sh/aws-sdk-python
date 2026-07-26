"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ApacheKafkaClusterDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.vpc_description


class ApacheKafkaClusterDescription(TypedDict, closed=True):
    bootstrap_servers: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The bootstrap servers of the cluster.</p>"""
    vpc: NotRequired["capo_kafkaconnect.types.vpc_description.VpcDescription"]
    """<p>Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApacheKafkaClusterDescription) -> dict:
    out: dict = {}
    if "bootstrap_servers" in value:
        out["bootstrapServers"] = value["bootstrap_servers"]
    if "vpc" in value:
        import capo_kafkaconnect.types.vpc_description

        out["vpc"] = capo_kafkaconnect.types.vpc_description.serialize_json(
            value["vpc"]
        )
    return out


def deserialize_json(data: dict) -> ApacheKafkaClusterDescription:
    out: ApacheKafkaClusterDescription = {}  # type: ignore[typeddict-item]
    if "bootstrapServers" in data:
        out["bootstrap_servers"] = data["bootstrapServers"]
    if "vpc" in data:
        import capo_kafkaconnect.types.vpc_description

        out["vpc"] = capo_kafkaconnect.types.vpc_description.deserialize_json(
            data["vpc"]
        )
    return out
