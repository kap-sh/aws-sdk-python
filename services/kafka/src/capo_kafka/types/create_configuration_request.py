"""Generated from Smithy shape ``com.amazonaws.kafka#CreateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__blob
    import capo_kafka.types.__list_of__string
    import capo_kafka.types.__string


class CreateConfigurationRequest(TypedDict, closed=True):
    description: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The description of the configuration.</p>"""
    kafka_versions: NotRequired["capo_kafka.types.__list_of__string.__listOf__string"]
    """<p>The versions of Apache Kafka with which you can use this MSK configuration.</p>"""
    name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the configuration.</p>"""
    server_properties: NotRequired["capo_kafka.types.__blob.__blob"]
    """<p>Contents of the <filename>server.properties</filename> file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the AWS Management Console, the SDK, or the AWS CLI, the contents of <filename>server.properties</filename> can be in plaintext.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "kafka_versions" in value:
        import capo_kafka.types.__list_of__string

        out["kafkaVersions"] = capo_kafka.types.__list_of__string.serialize_json(
            value["kafka_versions"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "server_properties" in value:
        import capo_kafka.types.__blob

        out["serverProperties"] = capo_kafka.types.__blob.serialize_json(
            value["server_properties"]
        )
    return out


def deserialize_json(data: dict) -> CreateConfigurationRequest:
    out: CreateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "kafkaVersions" in data:
        import capo_kafka.types.__list_of__string

        out["kafka_versions"] = capo_kafka.types.__list_of__string.deserialize_json(
            data["kafkaVersions"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "serverProperties" in data:
        import capo_kafka.types.__blob

        out["server_properties"] = capo_kafka.types.__blob.deserialize_json(
            data["serverProperties"]
        )
    return out
