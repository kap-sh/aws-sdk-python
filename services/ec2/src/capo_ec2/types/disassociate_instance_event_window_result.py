"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateInstanceEventWindowResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_event_window


class DisassociateInstanceEventWindowResult(TypedDict, closed=True):
    instance_event_window: NotRequired[
        "capo_ec2.types.instance_event_window.InstanceEventWindow"
    ]
    """<p>Information about the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateInstanceEventWindowResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_event_window" in value:
        import capo_ec2.types.instance_event_window

        capo_ec2.types.instance_event_window.serialize_ec2_query(
            value["instance_event_window"], pairs, f"{key_prefix}InstanceEventWindow"
        )


def deserialize_ec2_query(el: Element) -> DisassociateInstanceEventWindowResult:
    out: DisassociateInstanceEventWindowResult = {}  # type: ignore[typeddict-item]
    child_instance_event_window = el.find("InstanceEventWindow")
    if child_instance_event_window is not None:
        import capo_ec2.types.instance_event_window

        out["instance_event_window"] = (
            capo_ec2.types.instance_event_window.deserialize_ec2_query(
                child_instance_event_window
            )
        )
    return out
