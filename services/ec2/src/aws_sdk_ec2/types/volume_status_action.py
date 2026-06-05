"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusAction``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class VolumeStatusAction(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The code identifying the operation, for example, <code>enable-volume-io</code>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the operation.</p>"""
    event_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the event associated with this operation.</p>"""
    event_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The event type associated with this operation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeStatusAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        pairs.append((f"{prefix}.Code", str(value["code"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "event_id" in value:
        pairs.append((f"{prefix}.EventId", str(value["event_id"])))
    if "event_type" in value:
        pairs.append((f"{prefix}.EventType", str(value["event_type"])))


def deserialize_ec2_query(el: Element) -> VolumeStatusAction:
    out: VolumeStatusAction = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_event_id = el.find("EventId")
    if child_event_id is not None:
        out["event_id"] = str(child_event_id.text or "")
    child_event_type = el.find("EventType")
    if child_event_type is not None:
        out["event_type"] = str(child_event_type.text or "")
    return out
