"""Generated from Smithy shape ``com.amazonaws.deadline#CreateLicenseEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.security_group_id_list
    import aws_sdk_deadline.types.subnet_id_list
    import aws_sdk_deadline.types.tags
    import aws_sdk_deadline.types.vpc_id


class CreateLicenseEndpointRequest(TypedDict):
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    vpc_id: "aws_sdk_deadline.types.vpc_id.VpcId"
    """<p>The VPC (virtual private cloud) ID to use with the license endpoint.</p>"""
    subnet_ids: "aws_sdk_deadline.types.subnet_id_list.SubnetIdList"
    """<p>The subnet IDs.</p>"""
    security_group_ids: (
        "aws_sdk_deadline.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The security group IDs.</p>"""
    tags: NotRequired["aws_sdk_deadline.types.tags.Tags"]
    """<p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLicenseEndpointRequest) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import aws_sdk_deadline.types.subnet_id_list

    out["subnetIds"] = aws_sdk_deadline.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import aws_sdk_deadline.types.security_group_id_list

    out["securityGroupIds"] = (
        aws_sdk_deadline.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    if "tags" in value:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateLicenseEndpointRequest:
    out: CreateLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("CreateLicenseEndpointRequest.vpc_id required")
    if "subnetIds" in data:
        import aws_sdk_deadline.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_deadline.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("CreateLicenseEndpointRequest.subnet_ids required")
    if "securityGroupIds" in data:
        import aws_sdk_deadline.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_deadline.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseEndpointRequest.security_group_ids required"
        )
    if "tags" in data:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.deserialize_json(data["tags"])
    return out
