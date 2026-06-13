"""Generated from Smithy shape ``com.amazonaws.omics#VpcConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.security_group_ids
    import aws_sdk_omics.types.subnet_ids


class VpcConfig(TypedDict):
    security_group_ids: NotRequired[
        "aws_sdk_omics.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>List of security group IDs. Maximum of 5 security groups allowed.</p>"""
    subnet_ids: NotRequired["aws_sdk_omics.types.subnet_ids.SubnetIds"]
    """<p>List of subnet IDs. Maximum of 16 subnets allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfig) -> dict:
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
    return out


def deserialize_json(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
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
    return out
