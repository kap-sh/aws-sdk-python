"""Generated from Smithy shape ``com.amazonaws.kafka#ConsumerGroupReplicationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean
    import capo_kafka.types.__list_of__string_max256


class ConsumerGroupReplicationUpdate(TypedDict, closed=True):
    consumer_groups_to_exclude: NotRequired[
        "capo_kafka.types.__list_of__string_max256.__listOf__stringMax256"
    ]
    """<p>List of regular expression patterns indicating the consumer groups that should not be replicated.</p>"""
    consumer_groups_to_replicate: NotRequired[
        "capo_kafka.types.__list_of__string_max256.__listOf__stringMax256"
    ]
    """<p>List of regular expression patterns indicating the consumer groups to copy.</p>"""
    detect_and_copy_new_consumer_groups: NotRequired[
        "capo_kafka.types.__boolean.__boolean"
    ]
    """<p>Enables synchronization of consumer groups to target cluster.</p>"""
    synchronise_consumer_group_offsets: NotRequired[
        "capo_kafka.types.__boolean.__boolean"
    ]
    """<p>Enables synchronization of consumer group offsets to target cluster. The translated offsets will be written to topic __consumer_offsets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsumerGroupReplicationUpdate) -> dict:
    out: dict = {}
    if "consumer_groups_to_exclude" in value:
        import capo_kafka.types.__list_of__string_max256

        out["consumerGroupsToExclude"] = (
            capo_kafka.types.__list_of__string_max256.serialize_json(
                value["consumer_groups_to_exclude"]
            )
        )
    if "consumer_groups_to_replicate" in value:
        import capo_kafka.types.__list_of__string_max256

        out["consumerGroupsToReplicate"] = (
            capo_kafka.types.__list_of__string_max256.serialize_json(
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
    return out


def deserialize_json(data: dict) -> ConsumerGroupReplicationUpdate:
    out: ConsumerGroupReplicationUpdate = {}  # type: ignore[typeddict-item]
    if "consumerGroupsToExclude" in data:
        import capo_kafka.types.__list_of__string_max256

        out["consumer_groups_to_exclude"] = (
            capo_kafka.types.__list_of__string_max256.deserialize_json(
                data["consumerGroupsToExclude"]
            )
        )
    if "consumerGroupsToReplicate" in data:
        import capo_kafka.types.__list_of__string_max256

        out["consumer_groups_to_replicate"] = (
            capo_kafka.types.__list_of__string_max256.deserialize_json(
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
    return out
