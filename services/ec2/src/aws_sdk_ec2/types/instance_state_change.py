"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStateChange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_state
    import aws_sdk_ec2.types.string


class InstanceStateChange(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    current_state: NotRequired["aws_sdk_ec2.types.instance_state.InstanceState"]
    """<p>The current state of the instance.</p>"""
    previous_state: NotRequired["aws_sdk_ec2.types.instance_state.InstanceState"]
    """<p>The previous state of the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStateChange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "current_state" in value:
        import aws_sdk_ec2.types.instance_state

        aws_sdk_ec2.types.instance_state.serialize_ec2_query(
            value["current_state"], pairs, f"{prefix}.CurrentState"
        )
    if "previous_state" in value:
        import aws_sdk_ec2.types.instance_state

        aws_sdk_ec2.types.instance_state.serialize_ec2_query(
            value["previous_state"], pairs, f"{prefix}.PreviousState"
        )


def deserialize_ec2_query(el: Element) -> InstanceStateChange:
    out: InstanceStateChange = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_current_state = el.find("CurrentState")
    if child_current_state is not None:
        import aws_sdk_ec2.types.instance_state

        out["current_state"] = aws_sdk_ec2.types.instance_state.deserialize_ec2_query(
            child_current_state
        )
    child_previous_state = el.find("PreviousState")
    if child_previous_state is not None:
        import aws_sdk_ec2.types.instance_state

        out["previous_state"] = aws_sdk_ec2.types.instance_state.deserialize_ec2_query(
            child_previous_state
        )
    return out
