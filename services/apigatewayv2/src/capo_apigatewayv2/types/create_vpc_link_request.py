"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateVpcLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.security_group_id_list
    import capo_apigatewayv2.types.string_with_length_between1_and128
    import capo_apigatewayv2.types.subnet_id_list
    import capo_apigatewayv2.types.tags


class CreateVpcLinkRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The name of the VPC link.</p>"""
    security_group_ids: NotRequired[
        "capo_apigatewayv2.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>A list of security group IDs for the VPC link.</p>"""
    subnet_ids: NotRequired["capo_apigatewayv2.types.subnet_id_list.SubnetIdList"]
    """<p>A list of subnet IDs to include in the VPC link.</p>"""
    tags: NotRequired["capo_apigatewayv2.types.tags.Tags"]
    """<p>A list of tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcLinkRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "security_group_ids" in value:
        import capo_apigatewayv2.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_apigatewayv2.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import capo_apigatewayv2.types.subnet_id_list

        out["subnetIds"] = capo_apigatewayv2.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "tags" in value:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateVpcLinkRequest:
    out: CreateVpcLinkRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "securityGroupIds" in data:
        import capo_apigatewayv2.types.security_group_id_list

        out["security_group_ids"] = (
            capo_apigatewayv2.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetIds" in data:
        import capo_apigatewayv2.types.subnet_id_list

        out["subnet_ids"] = capo_apigatewayv2.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if "tags" in data:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.deserialize_json(data["tags"])
    return out
