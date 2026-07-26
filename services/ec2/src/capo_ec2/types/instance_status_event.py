"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.event_code
    import capo_ec2.types.instance_event_id
    import capo_ec2.types.string


class InstanceStatusEvent(TypedDict, closed=True):
    instance_event_id: NotRequired["capo_ec2.types.instance_event_id.InstanceEventId"]
    """<p>The ID of the event.</p>"""
    code: NotRequired["capo_ec2.types.event_code.EventCode"]
    """<p>The event code.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the event.</p> <p>After a scheduled event is completed, it can still be described for up to a week. If the event has been completed, this description starts with the following text: [Completed].</p>"""
    not_after: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The latest scheduled end time for the event.</p>"""
    not_before: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The earliest scheduled start time for the event.</p>"""
    not_before_deadline: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The deadline for starting the event.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStatusEvent, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_event_id" in value:
        pairs.append((f"{prefix}.InstanceEventId", str(value["instance_event_id"])))
    if "code" in value:
        import capo_ec2.types.event_code

        capo_ec2.types.event_code.serialize_ec2_query(
            value["code"], pairs, f"{prefix}.Code"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "not_after" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["not_after"], pairs, f"{prefix}.NotAfter"
        )
    if "not_before" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["not_before"], pairs, f"{prefix}.NotBefore"
        )
    if "not_before_deadline" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["not_before_deadline"], pairs, f"{prefix}.NotBeforeDeadline"
        )


def deserialize_ec2_query(el: Element) -> InstanceStatusEvent:
    out: InstanceStatusEvent = {}  # type: ignore[typeddict-item]
    child_instance_event_id = el.find("InstanceEventId")
    if child_instance_event_id is not None:
        out["instance_event_id"] = str(child_instance_event_id.text or "")
    child_code = el.find("Code")
    if child_code is not None:
        import capo_ec2.types.event_code

        out["code"] = capo_ec2.types.event_code.deserialize_ec2_query(child_code)
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_not_after = el.find("NotAfter")
    if child_not_after is not None:
        import capo_ec2.types.date_time

        out["not_after"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_not_after
        )
    child_not_before = el.find("NotBefore")
    if child_not_before is not None:
        import capo_ec2.types.date_time

        out["not_before"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_not_before
        )
    child_not_before_deadline = el.find("NotBeforeDeadline")
    if child_not_before_deadline is not None:
        import capo_ec2.types.date_time

        out["not_before_deadline"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_not_before_deadline
        )
    return out
