"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteInstanceEventWindowResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_event_window_state_change


class DeleteInstanceEventWindowResult(TypedDict, closed=True):
    instance_event_window_state: NotRequired[
        "capo_ec2.types.instance_event_window_state_change.InstanceEventWindowStateChange"
    ]
    """<p>The state of the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteInstanceEventWindowResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_event_window_state" in value:
        import capo_ec2.types.instance_event_window_state_change

        capo_ec2.types.instance_event_window_state_change.serialize_ec2_query(
            value["instance_event_window_state"],
            pairs,
            f"{key_prefix}InstanceEventWindowState",
        )


def deserialize_ec2_query(el: Element) -> DeleteInstanceEventWindowResult:
    out: DeleteInstanceEventWindowResult = {}  # type: ignore[typeddict-item]
    child_instance_event_window_state = el.find("instanceEventWindowState")
    if child_instance_event_window_state is not None:
        import capo_ec2.types.instance_event_window_state_change

        out["instance_event_window_state"] = (
            capo_ec2.types.instance_event_window_state_change.deserialize_ec2_query(
                child_instance_event_window_state
            )
        )
    return out
