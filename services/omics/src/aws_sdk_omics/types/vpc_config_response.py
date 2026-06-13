"""Generated from Smithy shape ``com.amazonaws.omics#VpcConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.security_group_ids
    import aws_sdk_omics.types.subnet_ids
    import aws_sdk_omics.types.vpc_id


class VpcConfigResponse(TypedDict):
    security_group_ids: NotRequired[
        "aws_sdk_omics.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>List of security group IDs.</p>"""
    subnet_ids: NotRequired["aws_sdk_omics.types.subnet_ids.SubnetIds"]
    """<p>List of subnet IDs.</p>"""
    vpc_id: NotRequired["aws_sdk_omics.types.vpc_id.VpcId"]
    """<p>VPC ID computed from the provided subnet IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfigResponse) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import aws_sdk_omics.types.security_group_ids

        out["securityGroupIds"] = aws_sdk_omics.types.security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    if "subnet_ids" in value:
        import aws_sdk_omics.types.subnet_ids

        out["subnetIds"] = aws_sdk_omics.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> VpcConfigResponse:
    out: VpcConfigResponse = {}  # type: ignore[typeddict-item]
    if "securityGroupIds" in data:
        import aws_sdk_omics.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_omics.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetIds" in data:
        import aws_sdk_omics.types.subnet_ids

        out["subnet_ids"] = aws_sdk_omics.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    return out
