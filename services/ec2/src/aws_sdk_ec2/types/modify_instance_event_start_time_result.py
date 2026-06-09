"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceEventStartTimeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_status_event


class ModifyInstanceEventStartTimeResult(TypedDict):
    event: NotRequired["aws_sdk_ec2.types.instance_status_event.InstanceStatusEvent"]
    """<p>Information about the event.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceEventStartTimeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "event" in value:
        import aws_sdk_ec2.types.instance_status_event

        aws_sdk_ec2.types.instance_status_event.serialize_ec2_query(
            value["event"], pairs, f"{prefix}.Event"
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceEventStartTimeResult:
    out: ModifyInstanceEventStartTimeResult = {}  # type: ignore[typeddict-item]
    child_event = el.find("Event")
    if child_event is not None:
        import aws_sdk_ec2.types.instance_status_event

        out["event"] = aws_sdk_ec2.types.instance_status_event.deserialize_ec2_query(
            child_event
        )
    return out
