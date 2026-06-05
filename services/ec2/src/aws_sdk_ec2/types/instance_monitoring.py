"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMonitoring``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.monitoring
    import aws_sdk_ec2.types.string


class InstanceMonitoring(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    monitoring: NotRequired["aws_sdk_ec2.types.monitoring.Monitoring"]
    """<p>The monitoring for the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceMonitoring, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "monitoring" in value:
        import aws_sdk_ec2.types.monitoring

        aws_sdk_ec2.types.monitoring.serialize_ec2_query(
            value["monitoring"], pairs, f"{prefix}.Monitoring"
        )


def deserialize_ec2_query(el: Element) -> InstanceMonitoring:
    out: InstanceMonitoring = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_monitoring = el.find("Monitoring")
    if child_monitoring is not None:
        import aws_sdk_ec2.types.monitoring

        out["monitoring"] = aws_sdk_ec2.types.monitoring.deserialize_ec2_query(
            child_monitoring
        )
    return out
