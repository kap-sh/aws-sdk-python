"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetRequesterGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.requester_gateway_status
    import capo_rtbfabric.types.security_group_id_list
    import capo_rtbfabric.types.subnet_id_list
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.vpc_id


class GetRequesterGatewayResponse(TypedDict, closed=True):
    status: "capo_rtbfabric.types.requester_gateway_status.RequesterGatewayStatus"
    """<p>The status of the request.</p>"""
    domain_name: "capo_rtbfabric.types.domain_name.DomainName"
    """<p>The domain name of the requester gateway.</p>"""
    description: NotRequired["str"]
    """<p>The description of the requester gateway.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the requester gateway was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the requester gateway was updated.</p>"""
    vpc_id: "capo_rtbfabric.types.vpc_id.VpcId"
    """<p>The unique identifier of the Virtual Private Cloud (VPC).</p>"""
    subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList"
    """<p>The unique identifiers of the subnets.</p>"""
    security_group_ids: (
        "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The unique identifiers of the security groups.</p>"""
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    tags: NotRequired["capo_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""
    active_links_count: NotRequired["int"]
    """<p>The count of active links for the requester gateway.</p>"""
    total_links_count: NotRequired["int"]
    """<p>The total count of links for the requester gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRequesterGatewayResponse) -> dict:
    out: dict = {}
    import capo_rtbfabric.types.requester_gateway_status

    out["status"] = capo_rtbfabric.types.requester_gateway_status.serialize_json(
        value["status"]
    )
    out["domainName"] = value["domain_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["createdAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["updatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    out["vpcId"] = value["vpc_id"]
    import capo_rtbfabric.types.subnet_id_list

    out["subnetIds"] = capo_rtbfabric.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import capo_rtbfabric.types.security_group_id_list

    out["securityGroupIds"] = (
        capo_rtbfabric.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    out["gatewayId"] = value["gateway_id"]
    if "tags" in value:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.serialize_json(value["tags"])
    if "active_links_count" in value:
        out["activeLinksCount"] = value["active_links_count"]
    if "total_links_count" in value:
        out["totalLinksCount"] = value["total_links_count"]
    return out


def deserialize_json(data: dict) -> GetRequesterGatewayResponse:
    out: GetRequesterGatewayResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_rtbfabric.types.requester_gateway_status

        out["status"] = capo_rtbfabric.types.requester_gateway_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetRequesterGatewayResponse.status required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("GetRequesterGatewayResponse.domain_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import capo_rtbfabric.types._prelude.timestamp

        out["created_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("GetRequesterGatewayResponse.vpc_id required")
    if "subnetIds" in data:
        import capo_rtbfabric.types.subnet_id_list

        out["subnet_ids"] = capo_rtbfabric.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("GetRequesterGatewayResponse.subnet_ids required")
    if "securityGroupIds" in data:
        import capo_rtbfabric.types.security_group_id_list

        out["security_group_ids"] = (
            capo_rtbfabric.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "GetRequesterGatewayResponse.security_group_ids required"
        )
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("GetRequesterGatewayResponse.gateway_id required")
    if "tags" in data:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    if "activeLinksCount" in data:
        out["active_links_count"] = data["activeLinksCount"]
    if "totalLinksCount" in data:
        out["total_links_count"] = data["totalLinksCount"]
    return out
