"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowStateChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_id
    import aws_sdk_ec2.types.instance_event_window_state


class InstanceEventWindowStateChange(TypedDict, closed=True):
    instance_event_window_id: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_state.InstanceEventWindowState"
    ]
    """<p>The current state of the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowStateChange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_event_window_id" in value:
        pairs.append(
            (f"{prefix}.InstanceEventWindowId", str(value["instance_event_window_id"]))
        )
    if "state" in value:
        import aws_sdk_ec2.types.instance_event_window_state

        aws_sdk_ec2.types.instance_event_window_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> InstanceEventWindowStateChange:
    out: InstanceEventWindowStateChange = {}  # type: ignore[typeddict-item]
    child_instance_event_window_id = el.find("InstanceEventWindowId")
    if child_instance_event_window_id is not None:
        out["instance_event_window_id"] = str(child_instance_event_window_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.instance_event_window_state

        out["state"] = (
            aws_sdk_ec2.types.instance_event_window_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
