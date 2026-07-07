"""Generated from Smithy shape ``com.amazonaws.guardduty#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.security_groups
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.subnet_ids


class VpcConfig(TypedDict, closed=True):
    subnet_ids: NotRequired["aws_sdk_guardduty.types.subnet_ids.SubnetIds"]
    """<p>The identifiers of the subnets that are associated with your Lambda function.</p>"""
    vpc_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The identifier of the Amazon Virtual Private Cloud.</p>"""
    security_groups: NotRequired[
        "aws_sdk_guardduty.types.security_groups.SecurityGroups"
    ]
    """<p>The identifier of the security group attached to the Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfig) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_guardduty.types.subnet_ids

        out["subnetIds"] = aws_sdk_guardduty.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "security_groups" in value:
        import aws_sdk_guardduty.types.security_groups

        out["securityGroups"] = aws_sdk_guardduty.types.security_groups.serialize_json(
            value["security_groups"]
        )
    return out


def deserialize_json(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_guardduty.types.subnet_ids

        out["subnet_ids"] = aws_sdk_guardduty.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "securityGroups" in data:
        import aws_sdk_guardduty.types.security_groups

        out["security_groups"] = (
            aws_sdk_guardduty.types.security_groups.deserialize_json(
                data["securityGroups"]
            )
        )
    return out
