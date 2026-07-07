"""Generated from Smithy shape ``com.amazonaws.ec2#MonitorInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_monitoring_list


class MonitorInstancesResult(TypedDict, closed=True):
    instance_monitorings: NotRequired[
        "aws_sdk_ec2.types.instance_monitoring_list.InstanceMonitoringList"
    ]
    """<p>The monitoring information.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MonitorInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_monitorings" in value:
        import aws_sdk_ec2.types.instance_monitoring_list

        aws_sdk_ec2.types.instance_monitoring_list.serialize_ec2_query(
            value["instance_monitorings"], pairs, f"{prefix}.InstancesSet"
        )


def deserialize_ec2_query(el: Element) -> MonitorInstancesResult:
    out: MonitorInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("InstancesSet") is not None:
        import aws_sdk_ec2.types.instance_monitoring_list

        out["instance_monitorings"] = (
            aws_sdk_ec2.types.instance_monitoring_list.deserialize_ec2_query(
                el, "InstancesSet"
            )
        )
    return out
