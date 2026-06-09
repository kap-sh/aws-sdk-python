"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceEventWindowResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window


class CreateInstanceEventWindowResult(TypedDict):
    instance_event_window: NotRequired[
        "aws_sdk_ec2.types.instance_event_window.InstanceEventWindow"
    ]
    """<p>Information about the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInstanceEventWindowResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_event_window" in value:
        import aws_sdk_ec2.types.instance_event_window

        aws_sdk_ec2.types.instance_event_window.serialize_ec2_query(
            value["instance_event_window"], pairs, f"{prefix}.InstanceEventWindow"
        )


def deserialize_ec2_query(el: Element) -> CreateInstanceEventWindowResult:
    out: CreateInstanceEventWindowResult = {}  # type: ignore[typeddict-item]
    child_instance_event_window = el.find("InstanceEventWindow")
    if child_instance_event_window is not None:
        import aws_sdk_ec2.types.instance_event_window

        out["instance_event_window"] = (
            aws_sdk_ec2.types.instance_event_window.deserialize_ec2_query(
                child_instance_event_window
            )
        )
    return out
