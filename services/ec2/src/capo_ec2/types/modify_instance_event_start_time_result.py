"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceEventStartTimeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_status_event


class ModifyInstanceEventStartTimeResult(TypedDict, closed=True):
    event: NotRequired["capo_ec2.types.instance_status_event.InstanceStatusEvent"]
    """<p>Information about the event.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceEventStartTimeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "event" in value:
        import capo_ec2.types.instance_status_event

        capo_ec2.types.instance_status_event.serialize_ec2_query(
            value["event"], pairs, f"{key_prefix}Event"
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceEventStartTimeResult:
    out: ModifyInstanceEventStartTimeResult = {}  # type: ignore[typeddict-item]
    child_event = el.find("Event")
    if child_event is not None:
        import capo_ec2.types.instance_status_event

        out["event"] = capo_ec2.types.instance_status_event.deserialize_ec2_query(
            child_event
        )
    return out
