"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#KafkaClusterClientAuthenticationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.kafka_cluster_client_authentication_type


class KafkaClusterClientAuthenticationDescription(TypedDict, closed=True):
    authentication_type: NotRequired[
        "capo_kafkaconnect.types.kafka_cluster_client_authentication_type.KafkaClusterClientAuthenticationType"
    ]
    """<p>The type of client authentication used to connect to the Apache Kafka cluster. Value NONE means that no client authentication is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterClientAuthenticationDescription) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        out["authenticationType"] = value["authentication_type"]
    return out


def deserialize_json(data: dict) -> KafkaClusterClientAuthenticationDescription:
    out: KafkaClusterClientAuthenticationDescription = {}  # type: ignore[typeddict-item]
    if "authenticationType" in data:
        out["authentication_type"] = data["authenticationType"]
    return out
