"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterSaslScramAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.kafka_cluster_sasl_scram_mechanism


class KafkaClusterSaslScramAuthentication(TypedDict, closed=True):
    mechanism: NotRequired[
        "aws_sdk_kafka.types.kafka_cluster_sasl_scram_mechanism.KafkaClusterSaslScramMechanism"
    ]
    """<p>The SASL/SCRAM authentication mechanism.</p>"""
    secret_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterSaslScramAuthentication) -> dict:
    out: dict = {}
    if "mechanism" in value:
        import aws_sdk_kafka.types.kafka_cluster_sasl_scram_mechanism

        out["mechanism"] = (
            aws_sdk_kafka.types.kafka_cluster_sasl_scram_mechanism.serialize_json(
                value["mechanism"]
            )
        )
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> KafkaClusterSaslScramAuthentication:
    out: KafkaClusterSaslScramAuthentication = {}  # type: ignore[typeddict-item]
    if "mechanism" in data:
        import aws_sdk_kafka.types.kafka_cluster_sasl_scram_mechanism

        out["mechanism"] = (
            aws_sdk_kafka.types.kafka_cluster_sasl_scram_mechanism.deserialize_json(
                data["mechanism"]
            )
        )
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    return out
