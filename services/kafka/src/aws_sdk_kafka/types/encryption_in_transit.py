"""Generated from Smithy shape ``com.amazonaws.kafka#EncryptionInTransit``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean
    import aws_sdk_kafka.types.client_broker


class EncryptionInTransit(TypedDict):
    client_broker: NotRequired["aws_sdk_kafka.types.client_broker.ClientBroker"]
    """<p>Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values.</p> <p> TLS means that client-broker communication is enabled with TLS only.</p> <p> TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.</p> <p> PLAINTEXT means that client-broker communication is enabled in plaintext only.</p> <p>The default value is TLS_PLAINTEXT.</p>"""
    in_cluster: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.</p> <p>The default value is true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionInTransit) -> dict:
    out: dict = {}
    if "client_broker" in value:
        import aws_sdk_kafka.types.client_broker

        out["clientBroker"] = aws_sdk_kafka.types.client_broker.serialize_json(
            value["client_broker"]
        )
    if "in_cluster" in value:
        out["inCluster"] = value["in_cluster"]
    return out


def deserialize_json(data: dict) -> EncryptionInTransit:
    out: EncryptionInTransit = {}  # type: ignore[typeddict-item]
    if "clientBroker" in data:
        import aws_sdk_kafka.types.client_broker

        out["client_broker"] = aws_sdk_kafka.types.client_broker.deserialize_json(
            data["clientBroker"]
        )
    if "inCluster" in data:
        out["in_cluster"] = data["inCluster"]
    return out
