"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerMonitoredTagKey``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_status
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class CapacityManagerMonitoredTagKey(TypedDict):
    tag_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The tag key being monitored. </p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_monitored_tag_key_status.CapacityManagerMonitoredTagKeyStatus"
    ]
    """<p> The current status of the monitored tag key. Valid values are <code>activating</code>, <code>activated</code>, <code>deactivating</code>, and <code>suspended</code>. </p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> A message providing additional details about the current status of the monitored tag key. </p>"""
    capacity_manager_provided: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Indicates whether this tag key is provided by Capacity Manager by default, rather than being user-activated. </p>"""
    earliest_datapoint_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The earliest timestamp from which tag data is available for queries, in UTC ISO 8601 format. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerMonitoredTagKey, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tag_key" in value:
        pairs.append((f"{prefix}.TagKey", str(value["tag_key"])))
    if "status" in value:
        import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_status

        aws_sdk_ec2.types.capacity_manager_monitored_tag_key_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "capacity_manager_provided" in value:
        pairs.append(
            (
                f"{prefix}.CapacityManagerProvided",
                "true" if value["capacity_manager_provided"] else "false",
            )
        )
    if "earliest_datapoint_timestamp" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["earliest_datapoint_timestamp"],
            pairs,
            f"{prefix}.EarliestDatapointTimestamp",
        )


def deserialize_ec2_query(el: Element) -> CapacityManagerMonitoredTagKey:
    out: CapacityManagerMonitoredTagKey = {}  # type: ignore[typeddict-item]
    child_tag_key = el.find("TagKey")
    if child_tag_key is not None:
        out["tag_key"] = str(child_tag_key.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_status

        out["status"] = (
            aws_sdk_ec2.types.capacity_manager_monitored_tag_key_status.deserialize_ec2_query(
                child_status
            )
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_capacity_manager_provided = el.find("CapacityManagerProvided")
    if child_capacity_manager_provided is not None:
        out["capacity_manager_provided"] = (
            child_capacity_manager_provided.text or ""
        ).lower() == "true"
    child_earliest_datapoint_timestamp = el.find("EarliestDatapointTimestamp")
    if child_earliest_datapoint_timestamp is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["earliest_datapoint_timestamp"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_earliest_datapoint_timestamp
            )
        )
    return out
