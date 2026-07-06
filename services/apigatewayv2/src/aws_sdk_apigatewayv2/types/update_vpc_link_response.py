"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateVpcLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__timestamp_iso8601
    import aws_sdk_apigatewayv2.types.id
    import aws_sdk_apigatewayv2.types.security_group_id_list
    import aws_sdk_apigatewayv2.types.string_with_length_between0_and1024
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and128
    import aws_sdk_apigatewayv2.types.subnet_id_list
    import aws_sdk_apigatewayv2.types.tags
    import aws_sdk_apigatewayv2.types.vpc_link_status
    import aws_sdk_apigatewayv2.types.vpc_link_version


class UpdateVpcLinkResponse(TypedDict, closed=True):
    created_date: NotRequired[
        "aws_sdk_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the VPC link was created.</p>"""
    name: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The name of the VPC link.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_apigatewayv2.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>A list of security group IDs for the VPC link.</p>"""
    subnet_ids: NotRequired["aws_sdk_apigatewayv2.types.subnet_id_list.SubnetIdList"]
    """<p>A list of subnet IDs to include in the VPC link.</p>"""
    tags: NotRequired["aws_sdk_apigatewayv2.types.tags.Tags"]
    """<p>Tags for the VPC link.</p>"""
    vpc_link_id: NotRequired["aws_sdk_apigatewayv2.types.id.Id"]
    """<p>The ID of the VPC link.</p>"""
    vpc_link_status: NotRequired[
        "aws_sdk_apigatewayv2.types.vpc_link_status.VpcLinkStatus"
    ]
    """<p>The status of the VPC link.</p>"""
    vpc_link_status_message: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>A message summarizing the cause of the status of the VPC link.</p>"""
    vpc_link_version: NotRequired[
        "aws_sdk_apigatewayv2.types.vpc_link_version.VpcLinkVersion"
    ]
    """<p>The version of the VPC link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVpcLinkResponse) -> dict:
    out: dict = {}
    if "created_date" in value:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["createdDate"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["created_date"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "security_group_ids" in value:
        import aws_sdk_apigatewayv2.types.security_group_id_list

        out["securityGroupIds"] = (
            aws_sdk_apigatewayv2.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import aws_sdk_apigatewayv2.types.subnet_id_list

        out["subnetIds"] = aws_sdk_apigatewayv2.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "tags" in value:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.serialize_json(value["tags"])
    if "vpc_link_id" in value:
        out["vpcLinkId"] = value["vpc_link_id"]
    if "vpc_link_status" in value:
        import aws_sdk_apigatewayv2.types.vpc_link_status

        out["vpcLinkStatus"] = (
            aws_sdk_apigatewayv2.types.vpc_link_status.serialize_json(
                value["vpc_link_status"]
            )
        )
    if "vpc_link_status_message" in value:
        out["vpcLinkStatusMessage"] = value["vpc_link_status_message"]
    if "vpc_link_version" in value:
        import aws_sdk_apigatewayv2.types.vpc_link_version

        out["vpcLinkVersion"] = (
            aws_sdk_apigatewayv2.types.vpc_link_version.serialize_json(
                value["vpc_link_version"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateVpcLinkResponse:
    out: UpdateVpcLinkResponse = {}  # type: ignore[typeddict-item]
    if "createdDate" in data:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["created_date"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["createdDate"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "securityGroupIds" in data:
        import aws_sdk_apigatewayv2.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_apigatewayv2.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetIds" in data:
        import aws_sdk_apigatewayv2.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_apigatewayv2.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if "tags" in data:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.deserialize_json(data["tags"])
    if "vpcLinkId" in data:
        out["vpc_link_id"] = data["vpcLinkId"]
    if "vpcLinkStatus" in data:
        import aws_sdk_apigatewayv2.types.vpc_link_status

        out["vpc_link_status"] = (
            aws_sdk_apigatewayv2.types.vpc_link_status.deserialize_json(
                data["vpcLinkStatus"]
            )
        )
    if "vpcLinkStatusMessage" in data:
        out["vpc_link_status_message"] = data["vpcLinkStatusMessage"]
    if "vpcLinkVersion" in data:
        import aws_sdk_apigatewayv2.types.vpc_link_version

        out["vpc_link_version"] = (
            aws_sdk_apigatewayv2.types.vpc_link_version.deserialize_json(
                data["vpcLinkVersion"]
            )
        )
    return out
