"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ApacheKafkaClusterDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.vpc_description


class ApacheKafkaClusterDescription(TypedDict):
    bootstrap_servers: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The bootstrap servers of the cluster.</p>"""
    vpc: NotRequired["aws_sdk_kafkaconnect.types.vpc_description.VpcDescription"]
    """<p>Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApacheKafkaClusterDescription) -> dict:
    out: dict = {}
    if "bootstrap_servers" in value:
        out["bootstrapServers"] = value["bootstrap_servers"]
    if "vpc" in value:
        import aws_sdk_kafkaconnect.types.vpc_description

        out["vpc"] = aws_sdk_kafkaconnect.types.vpc_description.serialize_json(
            value["vpc"]
        )
    return out


def deserialize_json(data: dict) -> ApacheKafkaClusterDescription:
    out: ApacheKafkaClusterDescription = {}  # type: ignore[typeddict-item]
    if "bootstrapServers" in data:
        out["bootstrap_servers"] = data["bootstrapServers"]
    if "vpc" in data:
        import aws_sdk_kafkaconnect.types.vpc_description

        out["vpc"] = aws_sdk_kafkaconnect.types.vpc_description.deserialize_json(
            data["vpc"]
        )
    return out
