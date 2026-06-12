"""Generated from Smithy shape ``com.amazonaws.autoscaling#ScalingProcessQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.process_names
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class ScalingProcessQuery(TypedDict):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    scaling_processes: NotRequired[
        "aws_sdk_auto_scaling.types.process_names.ProcessNames"
    ]
    """<p>One or more of the following processes:</p> <ul> <li> <p> <code>Launch</code> </p> </li> <li> <p> <code>Terminate</code> </p> </li> <li> <p> <code>AddToLoadBalancer</code> </p> </li> <li> <p> <code>AlarmNotification</code> </p> </li> <li> <p> <code>AZRebalance</code> </p> </li> <li> <p> <code>HealthCheck</code> </p> </li> <li> <p> <code>InstanceRefresh</code> </p> </li> <li> <p> <code>ReplaceUnhealthy</code> </p> </li> <li> <p> <code>ScheduledActions</code> </p> </li> </ul> <p>If you omit this property, all processes are specified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScalingProcessQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "scaling_processes" in value:
        import aws_sdk_auto_scaling.types.process_names

        aws_sdk_auto_scaling.types.process_names.serialize_query(
            value["scaling_processes"], pairs, f"{prefix}.ScalingProcesses"
        )


def deserialize_query(el: Element) -> ScalingProcessQuery:
    out: ScalingProcessQuery = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_scaling_processes = el.find("ScalingProcesses")
    if child_scaling_processes is not None:
        import aws_sdk_auto_scaling.types.process_names

        out["scaling_processes"] = (
            aws_sdk_auto_scaling.types.process_names.deserialize_query(
                child_scaling_processes
            )
        )
    return out
