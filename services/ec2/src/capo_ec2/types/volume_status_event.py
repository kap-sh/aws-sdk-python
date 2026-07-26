"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class VolumeStatusEvent(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the event.</p>"""
    event_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of this event.</p>"""
    event_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of this event.</p>"""
    not_after: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The latest end time of the event.</p>"""
    not_before: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The earliest start time of the event.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance associated with the event.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeStatusEvent, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "event_id" in value:
        pairs.append((f"{prefix}.EventId", str(value["event_id"])))
    if "event_type" in value:
        pairs.append((f"{prefix}.EventType", str(value["event_type"])))
    if "not_after" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["not_after"], pairs, f"{prefix}.NotAfter"
        )
    if "not_before" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["not_before"], pairs, f"{prefix}.NotBefore"
        )
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))


def deserialize_ec2_query(el: Element) -> VolumeStatusEvent:
    out: VolumeStatusEvent = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_event_id = el.find("EventId")
    if child_event_id is not None:
        out["event_id"] = str(child_event_id.text or "")
    child_event_type = el.find("EventType")
    if child_event_type is not None:
        out["event_type"] = str(child_event_type.text or "")
    child_not_after = el.find("NotAfter")
    if child_not_after is not None:
        import capo_ec2.types.millisecond_date_time

        out["not_after"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_not_after
        )
    child_not_before = el.find("NotBefore")
    if child_not_before is not None:
        import capo_ec2.types.millisecond_date_time

        out["not_before"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_not_before
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    return out
