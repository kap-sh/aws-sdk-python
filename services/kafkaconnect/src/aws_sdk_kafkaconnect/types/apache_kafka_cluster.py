"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ApacheKafkaCluster``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.vpc


class ApacheKafkaCluster(TypedDict):
    bootstrap_servers: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The bootstrap servers of the cluster.</p>"""
    vpc: "aws_sdk_kafkaconnect.types.vpc.Vpc"
    """<p>Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApacheKafkaCluster) -> dict:
    out: dict = {}
    out["bootstrapServers"] = value["bootstrap_servers"]
    import aws_sdk_kafkaconnect.types.vpc

    out["vpc"] = aws_sdk_kafkaconnect.types.vpc.serialize_json(value["vpc"])
    return out


def deserialize_json(data: dict) -> ApacheKafkaCluster:
    out: ApacheKafkaCluster = {}  # type: ignore[typeddict-item]
    if "bootstrapServers" in data:
        out["bootstrap_servers"] = data["bootstrapServers"]
    else:
        raise DeserializationError("ApacheKafkaCluster.bootstrap_servers required")
    if "vpc" in data:
        import aws_sdk_kafkaconnect.types.vpc

        out["vpc"] = aws_sdk_kafkaconnect.types.vpc.deserialize_json(data["vpc"])
    else:
        raise DeserializationError("ApacheKafkaCluster.vpc required")
    return out
