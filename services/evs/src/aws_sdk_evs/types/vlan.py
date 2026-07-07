"""Generated from Smithy shape ``com.amazonaws.evs#Vlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_evs.types.cidr
    import aws_sdk_evs.types.eip_association_list
    import aws_sdk_evs.types.network_acl_id
    import aws_sdk_evs.types.state_details
    import aws_sdk_evs.types.subnet_id
    import aws_sdk_evs.types.vlan_id
    import aws_sdk_evs.types.vlan_state


class Vlan(TypedDict, closed=True):
    vlan_id: NotRequired["aws_sdk_evs.types.vlan_id.VlanId"]
    """<p>The unique ID of the VLAN.</p>"""
    cidr: NotRequired["aws_sdk_evs.types.cidr.Cidr"]
    """<p>The CIDR block of the VLAN. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The availability zone of the VLAN.</p>"""
    function_name: NotRequired["str"]
    """<p>The VMware VCF traffic type that is carried over the VLAN. For example, a VLAN with a <code>functionName</code> of <code>hcx</code> is being used to carry VMware HCX traffic.</p>"""
    subnet_id: NotRequired["aws_sdk_evs.types.subnet_id.SubnetId"]
    """<p> The unique ID of the VLAN subnet.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the VLAN was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p> The date and time that the VLAN was modified.</p>"""
    vlan_state: NotRequired["aws_sdk_evs.types.vlan_state.VlanState"]
    """<p> The state of the VLAN.</p>"""
    state_details: NotRequired["aws_sdk_evs.types.state_details.StateDetails"]
    """<p>The state details of the VLAN.</p>"""
    eip_associations: NotRequired[
        "aws_sdk_evs.types.eip_association_list.EipAssociationList"
    ]
    """<p>An array of Elastic IP address associations.</p>"""
    is_public: NotRequired["bool"]
    """<p>Determines if the VLAN that Amazon EVS provisions is public or private.</p>"""
    network_acl_id: NotRequired["aws_sdk_evs.types.network_acl_id.NetworkAclId"]
    """<p>A unique ID for a network access control list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Vlan) -> dict:
    out: dict = {}
    if "vlan_id" in value:
        out["vlanId"] = value["vlan_id"]
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "function_name" in value:
        out["functionName"] = value["function_name"]
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "created_at" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["createdAt"] = aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "modified_at" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["modifiedAt"] = aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["modified_at"]
        )
    if "vlan_state" in value:
        import aws_sdk_evs.types.vlan_state

        out["vlanState"] = aws_sdk_evs.types.vlan_state.serialize_aws_json_1_0(
            value["vlan_state"]
        )
    if "state_details" in value:
        out["stateDetails"] = value["state_details"]
    if "eip_associations" in value:
        import aws_sdk_evs.types.eip_association_list

        out["eipAssociations"] = (
            aws_sdk_evs.types.eip_association_list.serialize_aws_json_1_0(
                value["eip_associations"]
            )
        )
    if "is_public" in value:
        out["isPublic"] = value["is_public"]
    if "network_acl_id" in value:
        out["networkAclId"] = value["network_acl_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Vlan:
    out: Vlan = {}  # type: ignore[typeddict-item]
    if "vlanId" in data:
        out["vlan_id"] = data["vlanId"]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "functionName" in data:
        out["function_name"] = data["functionName"]
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    if "createdAt" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "modifiedAt" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["modifiedAt"]
            )
        )
    if "vlanState" in data:
        import aws_sdk_evs.types.vlan_state

        out["vlan_state"] = aws_sdk_evs.types.vlan_state.deserialize_aws_json_1_0(
            data["vlanState"]
        )
    if "stateDetails" in data:
        out["state_details"] = data["stateDetails"]
    if "eipAssociations" in data:
        import aws_sdk_evs.types.eip_association_list

        out["eip_associations"] = (
            aws_sdk_evs.types.eip_association_list.deserialize_aws_json_1_0(
                data["eipAssociations"]
            )
        )
    if "isPublic" in data:
        out["is_public"] = data["isPublic"]
    if "networkAclId" in data:
        out["network_acl_id"] = data["networkAclId"]
    return out
