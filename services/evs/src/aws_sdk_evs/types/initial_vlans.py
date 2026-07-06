"""Generated from Smithy shape ``com.amazonaws.evs#InitialVlans``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_evs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_evs.types.initial_vlan_info
    import aws_sdk_evs.types.network_acl_id


class InitialVlans(TypedDict, closed=True):
    vmk_management: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p> The host VMkernel management VLAN subnet. This VLAN subnet carries traffic for managing ESX hosts and communicating with VMware vCenter Server.</p>"""
    vm_management: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p>The VM management VLAN subnet. This VLAN subnet carries traffic for vSphere virtual machines.</p>"""
    v_motion: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p> The vMotion VLAN subnet. This VLAN subnet carries traffic for vSphere vMotion.</p>"""
    v_san: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p> The vSAN VLAN subnet. This VLAN subnet carries the communication between ESX hosts to implement a vSAN shared storage pool.</p>"""
    v_tep: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p> The VTEP VLAN subnet. This VLAN subnet handles internal network traffic between virtual machines within a VCF instance.</p>"""
    edge_v_tep: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p>The edge VTEP VLAN subnet. This VLAN subnet manages traffic flowing between the internal network and external networks, including internet access and other site connections.</p>"""
    nsx_uplink: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p> The NSX uplink VLAN subnet. This VLAN subnet allows connectivity to the NSX overlay network.</p>"""
    hcx: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p>The HCX VLAN subnet. This VLAN subnet allows the HCX Interconnnect (IX) and HCX Network Extension (NE) to reach their peers and enable HCX Service Mesh creation.</p> <p>If you plan to use a public HCX VLAN subnet, the following requirements must be met:</p> <ul> <li> <p>Must have a /28 netmask and be allocated from the IPAM public pool. Required for HCX internet access configuration.</p> </li> <li> <p>The HCX public VLAN CIDR block must be added to the VPC as a secondary CIDR block.</p> </li> <li> <p>Must have at least two Elastic IP addresses to be allocated from the public IPAM pool for HCX components.</p> </li> </ul>"""
    expansion_vlan1: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p>An additional VLAN subnet that can be used to extend VCF capabilities once configured. For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.</p>"""
    expansion_vlan2: "aws_sdk_evs.types.initial_vlan_info.InitialVlanInfo"
    """<p>An additional VLAN subnet that can be used to extend VCF capabilities once configured. For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.</p>"""
    is_hcx_public: "bool"
    """<p>Determines if the HCX VLAN that Amazon EVS provisions is public or private.</p>"""
    hcx_network_acl_id: NotRequired["aws_sdk_evs.types.network_acl_id.NetworkAclId"]
    """<p>A unique ID for a network access control list that the HCX VLAN uses. Required when <code>isHcxPublic</code> is set to <code>true</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InitialVlans) -> dict:
    out: dict = {}
    import aws_sdk_evs.types.initial_vlan_info

    out["vmkManagement"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["vmk_management"]
    )
    import aws_sdk_evs.types.initial_vlan_info

    out["vmManagement"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["vm_management"]
    )
    import aws_sdk_evs.types.initial_vlan_info

    out["vMotion"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["v_motion"]
    )
    import aws_sdk_evs.types.initial_vlan_info

    out["vSan"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["v_san"]
    )
    import aws_sdk_evs.types.initial_vlan_info

    out["vTep"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["v_tep"]
    )
    import aws_sdk_evs.types.initial_vlan_info

    out["edgeVTep"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["edge_v_tep"]
    )
    import aws_sdk_evs.types.initial_vlan_info

    out["nsxUplink"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["nsx_uplink"]
    )
    import aws_sdk_evs.types.initial_vlan_info

    out["hcx"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["hcx"]
    )
    import aws_sdk_evs.types.initial_vlan_info

    out["expansionVlan1"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["expansion_vlan1"]
    )
    import aws_sdk_evs.types.initial_vlan_info

    out["expansionVlan2"] = aws_sdk_evs.types.initial_vlan_info.serialize_aws_json_1_0(
        value["expansion_vlan2"]
    )
    out["isHcxPublic"] = value.get("is_hcx_public", False)
    if "hcx_network_acl_id" in value:
        out["hcxNetworkAclId"] = value["hcx_network_acl_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InitialVlans:
    out: InitialVlans = {}  # type: ignore[typeddict-item]
    if "vmkManagement" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["vmk_management"] = (
            aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
                data["vmkManagement"]
            )
        )
    else:
        raise DeserializationError("InitialVlans.vmk_management required")
    if "vmManagement" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["vm_management"] = (
            aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
                data["vmManagement"]
            )
        )
    else:
        raise DeserializationError("InitialVlans.vm_management required")
    if "vMotion" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["v_motion"] = aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
            data["vMotion"]
        )
    else:
        raise DeserializationError("InitialVlans.v_motion required")
    if "vSan" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["v_san"] = aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
            data["vSan"]
        )
    else:
        raise DeserializationError("InitialVlans.v_san required")
    if "vTep" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["v_tep"] = aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
            data["vTep"]
        )
    else:
        raise DeserializationError("InitialVlans.v_tep required")
    if "edgeVTep" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["edge_v_tep"] = (
            aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
                data["edgeVTep"]
            )
        )
    else:
        raise DeserializationError("InitialVlans.edge_v_tep required")
    if "nsxUplink" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["nsx_uplink"] = (
            aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
                data["nsxUplink"]
            )
        )
    else:
        raise DeserializationError("InitialVlans.nsx_uplink required")
    if "hcx" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["hcx"] = aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
            data["hcx"]
        )
    else:
        raise DeserializationError("InitialVlans.hcx required")
    if "expansionVlan1" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["expansion_vlan1"] = (
            aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
                data["expansionVlan1"]
            )
        )
    else:
        raise DeserializationError("InitialVlans.expansion_vlan1 required")
    if "expansionVlan2" in data:
        import aws_sdk_evs.types.initial_vlan_info

        out["expansion_vlan2"] = (
            aws_sdk_evs.types.initial_vlan_info.deserialize_aws_json_1_0(
                data["expansionVlan2"]
            )
        )
    else:
        raise DeserializationError("InitialVlans.expansion_vlan2 required")
    if "isHcxPublic" in data:
        out["is_hcx_public"] = data["isHcxPublic"]
    else:
        out["is_hcx_public"] = False
    if "hcxNetworkAclId" in data:
        out["hcx_network_acl_id"] = data["hcxNetworkAclId"]
    return out
