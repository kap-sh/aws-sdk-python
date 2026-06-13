"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateRequesterGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.security_group_id_list
    import aws_sdk_rtbfabric.types.subnet_id_list
    import aws_sdk_rtbfabric.types.tags_map
    import aws_sdk_rtbfabric.types.vpc_id


class CreateRequesterGatewayRequest(TypedDict):
    vpc_id: "aws_sdk_rtbfabric.types.vpc_id.VpcId"
    """<p>The unique identifier of the Virtual Private Cloud (VPC).</p>"""
    subnet_ids: "aws_sdk_rtbfabric.types.subnet_id_list.SubnetIdList"
    """<p>The unique identifiers of the subnets.</p>"""
    security_group_ids: (
        "aws_sdk_rtbfabric.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The unique identifiers of the security groups.</p>"""
    client_token: "str"
    """<p>The unique client token.</p>"""
    description: NotRequired["str"]
    """<p>An optional description for the requester gateway.</p>"""
    tags: NotRequired["aws_sdk_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRequesterGatewayRequest) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import aws_sdk_rtbfabric.types.subnet_id_list

    out["subnetIds"] = aws_sdk_rtbfabric.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import aws_sdk_rtbfabric.types.security_group_id_list

    out["securityGroupIds"] = (
        aws_sdk_rtbfabric.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRequesterGatewayRequest:
    out: CreateRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("CreateRequesterGatewayRequest.vpc_id required")
    if "subnetIds" in data:
        import aws_sdk_rtbfabric.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_rtbfabric.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("CreateRequesterGatewayRequest.subnet_ids required")
    if "securityGroupIds" in data:
        import aws_sdk_rtbfabric.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_rtbfabric.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRequesterGatewayRequest.security_group_ids required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateRequesterGatewayRequest.client_token required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    return out
