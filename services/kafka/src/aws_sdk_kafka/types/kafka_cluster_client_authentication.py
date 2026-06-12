"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterClientAuthentication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.kafka_cluster_sasl_scram_authentication


class KafkaClusterClientAuthentication(TypedDict):
    sasl_scram: NotRequired[
        "aws_sdk_kafka.types.kafka_cluster_sasl_scram_authentication.KafkaClusterSaslScramAuthentication"
    ]
    """<p>Details for SASL/SCRAM client authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterClientAuthentication) -> dict:
    out: dict = {}
    if "sasl_scram" in value:
        import aws_sdk_kafka.types.kafka_cluster_sasl_scram_authentication

        out["saslScram"] = (
            aws_sdk_kafka.types.kafka_cluster_sasl_scram_authentication.serialize_json(
                value["sasl_scram"]
            )
        )
    return out


def deserialize_json(data: dict) -> KafkaClusterClientAuthentication:
    out: KafkaClusterClientAuthentication = {}  # type: ignore[typeddict-item]
    if "saslScram" in data:
        import aws_sdk_kafka.types.kafka_cluster_sasl_scram_authentication

        out["sasl_scram"] = (
            aws_sdk_kafka.types.kafka_cluster_sasl_scram_authentication.deserialize_json(
                data["saslScram"]
            )
        )
    return out
