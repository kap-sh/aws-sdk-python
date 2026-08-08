"""Generated from Smithy shape ``com.amazonaws.ec2#ActiveInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_health_status
    import capo_ec2.types.string


class ActiveInstance(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    spot_instance_request_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Spot Instance request.</p>"""
    instance_health: NotRequired[
        "capo_ec2.types.instance_health_status.InstanceHealthStatus"
    ]
    """<p>The health status of the instance. If the status of either the instance status check or the system status check is <code>impaired</code>, the health status of the instance is <code>unhealthy</code>. Otherwise, the health status is <code>healthy</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ActiveInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "spot_instance_request_id" in value:
        pairs.append(
            (
                f"{key_prefix}SpotInstanceRequestId",
                str(value["spot_instance_request_id"]),
            )
        )
    if "instance_health" in value:
        import capo_ec2.types.instance_health_status

        capo_ec2.types.instance_health_status.serialize_ec2_query(
            value["instance_health"], pairs, f"{key_prefix}InstanceHealth"
        )


def deserialize_ec2_query(el: Element) -> ActiveInstance:
    out: ActiveInstance = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_spot_instance_request_id = el.find("spotInstanceRequestId")
    if child_spot_instance_request_id is not None:
        out["spot_instance_request_id"] = str(child_spot_instance_request_id.text or "")
    child_instance_health = el.find("instanceHealth")
    if child_instance_health is not None:
        import capo_ec2.types.instance_health_status

        out["instance_health"] = (
            capo_ec2.types.instance_health_status.deserialize_ec2_query(
                child_instance_health
            )
        )
    return out
