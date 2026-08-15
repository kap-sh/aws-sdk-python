"""Generated from Smithy shape ``com.amazonaws.ec2#HealthCheckPathDestinationResponseObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class HealthCheckPathDestinationResponseObject(TypedDict, closed=True):
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet for the destination.</p>"""
    security_group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the security group for the destination.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HealthCheckPathDestinationResponseObject,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "security_group_id" in value:
        pairs.append((f"{key_prefix}SecurityGroupId", str(value["security_group_id"])))


def deserialize_ec2_query(el: Element) -> HealthCheckPathDestinationResponseObject:
    out: HealthCheckPathDestinationResponseObject = {}  # type: ignore[typeddict-item]
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_security_group_id = el.find("securityGroupId")
    if child_security_group_id is not None:
        out["security_group_id"] = str(child_security_group_id.text or "")
    return out
