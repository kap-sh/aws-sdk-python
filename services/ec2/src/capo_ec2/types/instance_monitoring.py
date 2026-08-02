"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMonitoring``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.monitoring
    import capo_ec2.types.string


class InstanceMonitoring(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    monitoring: NotRequired["capo_ec2.types.monitoring.Monitoring"]
    """<p>The monitoring for the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceMonitoring, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "monitoring" in value:
        import capo_ec2.types.monitoring

        capo_ec2.types.monitoring.serialize_ec2_query(
            value["monitoring"], pairs, f"{key_prefix}Monitoring"
        )


def deserialize_ec2_query(el: Element) -> InstanceMonitoring:
    out: InstanceMonitoring = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_monitoring = el.find("Monitoring")
    if child_monitoring is not None:
        import capo_ec2.types.monitoring

        out["monitoring"] = capo_ec2.types.monitoring.deserialize_ec2_query(
            child_monitoring
        )
    return out
