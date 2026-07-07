"""Generated from Smithy shape ``com.amazonaws.kafka#TopicReplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean
    import aws_sdk_kafka.types.__list_of__string_max249
    import aws_sdk_kafka.types.replication_starting_position
    import aws_sdk_kafka.types.replication_topic_name_configuration


class TopicReplication(TypedDict, closed=True):
    copy_access_control_lists_for_topics: NotRequired[
        "aws_sdk_kafka.types.__boolean.__boolean"
    ]
    """<p>Whether to periodically configure remote topic ACLs to match their corresponding upstream topics.</p>"""
    copy_topic_configurations: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Whether to periodically configure remote topics to match their corresponding upstream topics.</p>"""
    detect_and_copy_new_topics: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Whether to periodically check for new topics and partitions.</p>"""
    starting_position: NotRequired[
        "aws_sdk_kafka.types.replication_starting_position.ReplicationStartingPosition"
    ]
    """<p>Configuration for specifying the position in the topics to start replicating from.</p>"""
    topic_name_configuration: NotRequired[
        "aws_sdk_kafka.types.replication_topic_name_configuration.ReplicationTopicNameConfiguration"
    ]
    """<p>Configuration for specifying replicated topic names should be the same as their corresponding upstream topics or prefixed with source cluster alias.</p>"""
    topics_to_exclude: NotRequired[
        "aws_sdk_kafka.types.__list_of__string_max249.__listOf__stringMax249"
    ]
    """<p>List of regular expression patterns indicating the topics that should not be replicated.</p>"""
    topics_to_replicate: NotRequired[
        "aws_sdk_kafka.types.__list_of__string_max249.__listOf__stringMax249"
    ]
    """<p>List of regular expression patterns indicating the topics to copy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicReplication) -> dict:
    out: dict = {}
    if "copy_access_control_lists_for_topics" in value:
        out["copyAccessControlListsForTopics"] = value[
            "copy_access_control_lists_for_topics"
        ]
    if "copy_topic_configurations" in value:
        out["copyTopicConfigurations"] = value["copy_topic_configurations"]
    if "detect_and_copy_new_topics" in value:
        out["detectAndCopyNewTopics"] = value["detect_and_copy_new_topics"]
    if "starting_position" in value:
        import aws_sdk_kafka.types.replication_starting_position

        out["startingPosition"] = (
            aws_sdk_kafka.types.replication_starting_position.serialize_json(
                value["starting_position"]
            )
        )
    if "topic_name_configuration" in value:
        import aws_sdk_kafka.types.replication_topic_name_configuration

        out["topicNameConfiguration"] = (
            aws_sdk_kafka.types.replication_topic_name_configuration.serialize_json(
                value["topic_name_configuration"]
            )
        )
    if "topics_to_exclude" in value:
        import aws_sdk_kafka.types.__list_of__string_max249

        out["topicsToExclude"] = (
            aws_sdk_kafka.types.__list_of__string_max249.serialize_json(
                value["topics_to_exclude"]
            )
        )
    if "topics_to_replicate" in value:
        import aws_sdk_kafka.types.__list_of__string_max249

        out["topicsToReplicate"] = (
            aws_sdk_kafka.types.__list_of__string_max249.serialize_json(
                value["topics_to_replicate"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicReplication:
    out: TopicReplication = {}  # type: ignore[typeddict-item]
    if "copyAccessControlListsForTopics" in data:
        out["copy_access_control_lists_for_topics"] = data[
            "copyAccessControlListsForTopics"
        ]
    if "copyTopicConfigurations" in data:
        out["copy_topic_configurations"] = data["copyTopicConfigurations"]
    if "detectAndCopyNewTopics" in data:
        out["detect_and_copy_new_topics"] = data["detectAndCopyNewTopics"]
    if "startingPosition" in data:
        import aws_sdk_kafka.types.replication_starting_position

        out["starting_position"] = (
            aws_sdk_kafka.types.replication_starting_position.deserialize_json(
                data["startingPosition"]
            )
        )
    if "topicNameConfiguration" in data:
        import aws_sdk_kafka.types.replication_topic_name_configuration

        out["topic_name_configuration"] = (
            aws_sdk_kafka.types.replication_topic_name_configuration.deserialize_json(
                data["topicNameConfiguration"]
            )
        )
    if "topicsToExclude" in data:
        import aws_sdk_kafka.types.__list_of__string_max249

        out["topics_to_exclude"] = (
            aws_sdk_kafka.types.__list_of__string_max249.deserialize_json(
                data["topicsToExclude"]
            )
        )
    if "topicsToReplicate" in data:
        import aws_sdk_kafka.types.__list_of__string_max249

        out["topics_to_replicate"] = (
            aws_sdk_kafka.types.__list_of__string_max249.deserialize_json(
                data["topicsToReplicate"]
            )
        )
    return out
