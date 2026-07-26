"""Generated from Smithy shape ``com.amazonaws.opensearch#VPCDerivedInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.string
    import capo_opensearch.types.string_list


class VPCDerivedInfo(TypedDict, closed=True):
    vpc_id: NotRequired["capo_opensearch.types.string.String"]
    """<p>The ID for your VPC. Amazon VPC generates this value when you create a VPC.</p>"""
    subnet_ids: NotRequired["capo_opensearch.types.string_list.StringList"]
    """<p>A list of subnet IDs associated with the VPC endpoints for the domain.</p>"""
    availability_zones: NotRequired["capo_opensearch.types.string_list.StringList"]
    """<p>The list of Availability Zones associated with the VPC subnets.</p>"""
    security_group_ids: NotRequired["capo_opensearch.types.string_list.StringList"]
    """<p>The list of security group IDs associated with the VPC endpoints for the domain.</p>"""
    egress_enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether egress traffic from the domain is routed through the customer VPC. When <code>true</code>, outbound traffic flows through the VPC. When <code>false</code>, outbound traffic goes through the public internet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VPCDerivedInfo) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VPCId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_opensearch.types.string_list

        out["SubnetIds"] = capo_opensearch.types.string_list.serialize_json(
            value["subnet_ids"]
        )
    if "availability_zones" in value:
        import capo_opensearch.types.string_list

        out["AvailabilityZones"] = capo_opensearch.types.string_list.serialize_json(
            value["availability_zones"]
        )
    if "security_group_ids" in value:
        import capo_opensearch.types.string_list

        out["SecurityGroupIds"] = capo_opensearch.types.string_list.serialize_json(
            value["security_group_ids"]
        )
    if "egress_enabled" in value:
        out["EgressEnabled"] = value["egress_enabled"]
    return out


def deserialize_json(data: dict) -> VPCDerivedInfo:
    out: VPCDerivedInfo = {}  # type: ignore[typeddict-item]
    if "VPCId" in data:
        out["vpc_id"] = data["VPCId"]
    if "SubnetIds" in data:
        import capo_opensearch.types.string_list

        out["subnet_ids"] = capo_opensearch.types.string_list.deserialize_json(
            data["SubnetIds"]
        )
    if "AvailabilityZones" in data:
        import capo_opensearch.types.string_list

        out["availability_zones"] = capo_opensearch.types.string_list.deserialize_json(
            data["AvailabilityZones"]
        )
    if "SecurityGroupIds" in data:
        import capo_opensearch.types.string_list

        out["security_group_ids"] = capo_opensearch.types.string_list.deserialize_json(
            data["SecurityGroupIds"]
        )
    if "EgressEnabled" in data:
        out["egress_enabled"] = data["EgressEnabled"]
    return out
