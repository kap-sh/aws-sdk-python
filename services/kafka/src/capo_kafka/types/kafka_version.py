"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.kafka_version_status


class KafkaVersion(TypedDict, closed=True):
    version: NotRequired["capo_kafka.types.__string.__string"]
    status: NotRequired["capo_kafka.types.kafka_version_status.KafkaVersionStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaVersion) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "status" in value:
        import capo_kafka.types.kafka_version_status

        out["status"] = capo_kafka.types.kafka_version_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> KafkaVersion:
    out: KafkaVersion = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    if "status" in data:
        import capo_kafka.types.kafka_version_status

        out["status"] = capo_kafka.types.kafka_version_status.deserialize_json(
            data["status"]
        )
    return out
