"""Generated from Smithy shape ``com.amazonaws.kafka#Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of__string
    import capo_kafka.types.__string
    import capo_kafka.types.__timestamp_iso8601
    import capo_kafka.types.configuration_revision
    import capo_kafka.types.configuration_state


class Configuration(TypedDict, closed=True):
    arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the configuration.</p>"""
    creation_time: NotRequired[
        "capo_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the configuration was created.</p>"""
    description: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The description of the configuration.</p>"""
    kafka_versions: NotRequired["capo_kafka.types.__list_of__string.__listOf__string"]
    """<p>An array of the versions of Apache Kafka with which you can use this MSK configuration. You can use this configuration for an MSK cluster only if the Apache Kafka version specified for the cluster appears in this array.</p>"""
    latest_revision: NotRequired[
        "capo_kafka.types.configuration_revision.ConfigurationRevision"
    ]
    """<p>Latest revision of the configuration.</p>"""
    name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the configuration.</p>"""
    state: NotRequired["capo_kafka.types.configuration_state.ConfigurationState"]
    """<p>The state of the configuration. The possible states are ACTIVE, DELETING, and DELETE_FAILED. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "creation_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["creationTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "kafka_versions" in value:
        import capo_kafka.types.__list_of__string

        out["kafkaVersions"] = capo_kafka.types.__list_of__string.serialize_json(
            value["kafka_versions"]
        )
    if "latest_revision" in value:
        import capo_kafka.types.configuration_revision

        out["latestRevision"] = capo_kafka.types.configuration_revision.serialize_json(
            value["latest_revision"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "state" in value:
        import capo_kafka.types.configuration_state

        out["state"] = capo_kafka.types.configuration_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "creationTime" in data:
        import capo_kafka.types.__timestamp_iso8601

        out["creation_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "kafkaVersions" in data:
        import capo_kafka.types.__list_of__string

        out["kafka_versions"] = capo_kafka.types.__list_of__string.deserialize_json(
            data["kafkaVersions"]
        )
    if "latestRevision" in data:
        import capo_kafka.types.configuration_revision

        out["latest_revision"] = (
            capo_kafka.types.configuration_revision.deserialize_json(
                data["latestRevision"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "state" in data:
        import capo_kafka.types.configuration_state

        out["state"] = capo_kafka.types.configuration_state.deserialize_json(
            data["state"]
        )
    return out
