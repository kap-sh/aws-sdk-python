"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateClusterKafkaVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.configuration_info


class UpdateClusterKafkaVersionRequest(TypedDict, closed=True):
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>"""
    configuration_info: NotRequired[
        "capo_kafka.types.configuration_info.ConfigurationInfo"
    ]
    """<p>The custom configuration that should be applied on the new version of cluster.</p>"""
    current_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Current cluster version.</p>"""
    target_kafka_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Target Kafka version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterKafkaVersionRequest) -> dict:
    out: dict = {}
    if "configuration_info" in value:
        import capo_kafka.types.configuration_info

        out["configurationInfo"] = capo_kafka.types.configuration_info.serialize_json(
            value["configuration_info"]
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "target_kafka_version" in value:
        out["targetKafkaVersion"] = value["target_kafka_version"]
    return out


def deserialize_json(data: dict) -> UpdateClusterKafkaVersionRequest:
    out: UpdateClusterKafkaVersionRequest = {}  # type: ignore[typeddict-item]
    if "configurationInfo" in data:
        import capo_kafka.types.configuration_info

        out["configuration_info"] = (
            capo_kafka.types.configuration_info.deserialize_json(
                data["configurationInfo"]
            )
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "targetKafkaVersion" in data:
        out["target_kafka_version"] = data["targetKafkaVersion"]
    return out
