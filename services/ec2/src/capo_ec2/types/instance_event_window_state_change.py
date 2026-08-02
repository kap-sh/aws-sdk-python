"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowStateChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_event_window_id
    import capo_ec2.types.instance_event_window_state


class InstanceEventWindowStateChange(TypedDict, closed=True):
    instance_event_window_id: NotRequired[
        "capo_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""
    state: NotRequired[
        "capo_ec2.types.instance_event_window_state.InstanceEventWindowState"
    ]
    """<p>The current state of the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowStateChange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_event_window_id" in value:
        pairs.append(
            (
                f"{key_prefix}InstanceEventWindowId",
                str(value["instance_event_window_id"]),
            )
        )
    if "state" in value:
        import capo_ec2.types.instance_event_window_state

        capo_ec2.types.instance_event_window_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> InstanceEventWindowStateChange:
    out: InstanceEventWindowStateChange = {}  # type: ignore[typeddict-item]
    child_instance_event_window_id = el.find("InstanceEventWindowId")
    if child_instance_event_window_id is not None:
        out["instance_event_window_id"] = str(child_instance_event_window_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.instance_event_window_state

        out["state"] = capo_ec2.types.instance_event_window_state.deserialize_ec2_query(
            child_state
        )
    return out
