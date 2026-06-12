"""Generated from Smithy shape ``com.amazonaws.kafka#ConsumerGroupReplication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean
    import aws_sdk_kafka.types.__list_of__string_max256
    import aws_sdk_kafka.types.consumer_group_offset_sync_mode


class ConsumerGroupReplication(TypedDict):
    consumer_groups_to_exclude: NotRequired[
        "aws_sdk_kafka.types.__list_of__string_max256.__listOf__stringMax256"
    ]
    """<p>List of regular expression patterns indicating the consumer groups that should not be replicated.</p>"""
    consumer_groups_to_replicate: NotRequired[
        "aws_sdk_kafka.types.__list_of__string_max256.__listOf__stringMax256"
    ]
    """<p>List of regular expression patterns indicating the consumer groups to copy.</p>"""
    detect_and_copy_new_consumer_groups: NotRequired[
        "aws_sdk_kafka.types.__boolean.__boolean"
    ]
    """<p>Enables synchronization of consumer groups to target cluster.</p>"""
    synchronise_consumer_group_offsets: NotRequired[
        "aws_sdk_kafka.types.__boolean.__boolean"
    ]
    """<p>Enables synchronization of consumer group offsets to target cluster. The translated offsets will be written to topic __consumer_offsets.</p>"""
    consumer_group_offset_sync_mode: NotRequired[
        "aws_sdk_kafka.types.consumer_group_offset_sync_mode.ConsumerGroupOffsetSyncMode"
    ]
    """<p>The consumer group offset synchronization mode. With LEGACY, offsets are synchronized when producers write to the source cluster. With ENHANCED, consumer offsets are synchronized regardless of producer location. ENHANCED requires a corresponding replicator that replicates data from the target cluster to the source cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsumerGroupReplication) -> dict:
    out: dict = {}
    if "consumer_groups_to_exclude" in value:
        import aws_sdk_kafka.types.__list_of__string_max256

        out["consumerGroupsToExclude"] = (
            aws_sdk_kafka.types.__list_of__string_max256.serialize_json(
                value["consumer_groups_to_exclude"]
            )
        )
    if "consumer_groups_to_replicate" in value:
        import aws_sdk_kafka.types.__list_of__string_max256

        out["consumerGroupsToReplicate"] = (
            aws_sdk_kafka.types.__list_of__string_max256.serialize_json(
                value["consumer_groups_to_replicate"]
            )
        )
    if "detect_and_copy_new_consumer_groups" in value:
        out["detectAndCopyNewConsumerGroups"] = value[
            "detect_and_copy_new_consumer_groups"
        ]
    if "synchronise_consumer_group_offsets" in value:
        out["synchroniseConsumerGroupOffsets"] = value[
            "synchronise_consumer_group_offsets"
        ]
    if "consumer_group_offset_sync_mode" in value:
        import aws_sdk_kafka.types.consumer_group_offset_sync_mode

        out["consumerGroupOffsetSyncMode"] = (
            aws_sdk_kafka.types.consumer_group_offset_sync_mode.serialize_json(
                value["consumer_group_offset_sync_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConsumerGroupReplication:
    out: ConsumerGroupReplication = {}  # type: ignore[typeddict-item]
    if "consumerGroupsToExclude" in data:
        import aws_sdk_kafka.types.__list_of__string_max256

        out["consumer_groups_to_exclude"] = (
            aws_sdk_kafka.types.__list_of__string_max256.deserialize_json(
                data["consumerGroupsToExclude"]
            )
        )
    if "consumerGroupsToReplicate" in data:
        import aws_sdk_kafka.types.__list_of__string_max256

        out["consumer_groups_to_replicate"] = (
            aws_sdk_kafka.types.__list_of__string_max256.deserialize_json(
                data["consumerGroupsToReplicate"]
            )
        )
    if "detectAndCopyNewConsumerGroups" in data:
        out["detect_and_copy_new_consumer_groups"] = data[
            "detectAndCopyNewConsumerGroups"
        ]
    if "synchroniseConsumerGroupOffsets" in data:
        out["synchronise_consumer_group_offsets"] = data[
            "synchroniseConsumerGroupOffsets"
        ]
    if "consumerGroupOffsetSyncMode" in data:
        import aws_sdk_kafka.types.consumer_group_offset_sync_mode

        out["consumer_group_offset_sync_mode"] = (
            aws_sdk_kafka.types.consumer_group_offset_sync_mode.deserialize_json(
                data["consumerGroupOffsetSyncMode"]
            )
        )
    return out
