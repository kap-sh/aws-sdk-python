"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceEventStartTimeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.string


class ModifyInstanceEventStartTimeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance with the scheduled event.</p>"""
    instance_event_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the event whose date and time you are modifying.</p>"""
    not_before: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The new date and time when the event will take place.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceEventStartTimeRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "instance_event_id" in value:
        pairs.append((f"{prefix}.InstanceEventId", str(value["instance_event_id"])))
    if "not_before" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["not_before"], pairs, f"{prefix}.NotBefore"
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceEventStartTimeRequest:
    out: ModifyInstanceEventStartTimeRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_event_id = el.find("InstanceEventId")
    if child_instance_event_id is not None:
        out["instance_event_id"] = str(child_instance_event_id.text or "")
    child_not_before = el.find("NotBefore")
    if child_not_before is not None:
        import aws_sdk_ec2.types.date_time

        out["not_before"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_not_before
        )
    return out
