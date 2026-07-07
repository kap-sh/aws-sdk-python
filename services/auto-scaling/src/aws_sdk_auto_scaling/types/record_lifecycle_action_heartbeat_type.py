"""Generated from Smithy shape ``com.amazonaws.autoscaling#RecordLifecycleActionHeartbeatType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.ascii_string_max_len255
    import aws_sdk_auto_scaling.types.lifecycle_action_token
    import aws_sdk_auto_scaling.types.resource_name
    import aws_sdk_auto_scaling.types.xml_string_max_len19


class RecordLifecycleActionHeartbeatType(TypedDict, closed=True):
    lifecycle_hook_name: NotRequired[
        "aws_sdk_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
    ]
    """<p>The name of the lifecycle hook.</p>"""
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.resource_name.ResourceName"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    lifecycle_action_token: NotRequired[
        "aws_sdk_auto_scaling.types.lifecycle_action_token.LifecycleActionToken"
    ]
    """<p>A token that uniquely identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target that you specified when you created the lifecycle hook.</p>"""
    instance_id: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
    ]
    """<p>The ID of the instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RecordLifecycleActionHeartbeatType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "lifecycle_hook_name" in value:
        pairs.append((f"{prefix}.LifecycleHookName", str(value["lifecycle_hook_name"])))
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "lifecycle_action_token" in value:
        pairs.append(
            (f"{prefix}.LifecycleActionToken", str(value["lifecycle_action_token"]))
        )
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))


def deserialize_query(el: Element) -> RecordLifecycleActionHeartbeatType:
    out: RecordLifecycleActionHeartbeatType = {}  # type: ignore[typeddict-item]
    child_lifecycle_hook_name = el.find("LifecycleHookName")
    if child_lifecycle_hook_name is not None:
        out["lifecycle_hook_name"] = str(child_lifecycle_hook_name.text or "")
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_lifecycle_action_token = el.find("LifecycleActionToken")
    if child_lifecycle_action_token is not None:
        out["lifecycle_action_token"] = str(child_lifecycle_action_token.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    return out
