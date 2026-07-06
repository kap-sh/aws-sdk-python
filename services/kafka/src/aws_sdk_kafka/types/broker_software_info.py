"""Generated from Smithy shape ``com.amazonaws.kafka#BrokerSoftwareInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__long
    import aws_sdk_kafka.types.__string


class BrokerSoftwareInfo(TypedDict, closed=True):
    configuration_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the configuration used for the cluster. This field isn't visible in this preview release.</p>"""
    configuration_revision: NotRequired["aws_sdk_kafka.types.__long.__long"]
    """<p>The revision of the configuration to use. This field isn't visible in this preview release.</p>"""
    kafka_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The version of Apache Kafka.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerSoftwareInfo) -> dict:
    out: dict = {}
    if "configuration_arn" in value:
        out["configurationArn"] = value["configuration_arn"]
    if "configuration_revision" in value:
        out["configurationRevision"] = value["configuration_revision"]
    if "kafka_version" in value:
        out["kafkaVersion"] = value["kafka_version"]
    return out


def deserialize_json(data: dict) -> BrokerSoftwareInfo:
    out: BrokerSoftwareInfo = {}  # type: ignore[typeddict-item]
    if "configurationArn" in data:
        out["configuration_arn"] = data["configurationArn"]
    if "configurationRevision" in data:
        out["configuration_revision"] = data["configurationRevision"]
    if "kafkaVersion" in data:
        out["kafka_version"] = data["kafkaVersion"]
    return out
