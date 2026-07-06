"""Generated from Smithy shape ``com.amazonaws.scheduler#AwsVpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.assign_public_ip
    import aws_sdk_scheduler.types.security_groups
    import aws_sdk_scheduler.types.subnets


class AwsVpcConfiguration(TypedDict, closed=True):
    subnets: "aws_sdk_scheduler.types.subnets.Subnets"
    """<p>Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.</p>"""
    security_groups: NotRequired[
        "aws_sdk_scheduler.types.security_groups.SecurityGroups"
    ]
    """<p>Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.</p>"""
    assign_public_ip: NotRequired[
        "aws_sdk_scheduler.types.assign_public_ip.AssignPublicIp"
    ]
    """<p>Specifies whether the task's elastic network interface receives a public IP address. You can specify <code>ENABLED</code> only when <code>LaunchType</code> in <code>EcsParameters</code> is set to <code>FARGATE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsVpcConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_scheduler.types.subnets

    out["Subnets"] = aws_sdk_scheduler.types.subnets.serialize_json(value["subnets"])
    if "security_groups" in value:
        import aws_sdk_scheduler.types.security_groups

        out["SecurityGroups"] = aws_sdk_scheduler.types.security_groups.serialize_json(
            value["security_groups"]
        )
    if "assign_public_ip" in value:
        out["AssignPublicIp"] = value["assign_public_ip"]
    return out


def deserialize_json(data: dict) -> AwsVpcConfiguration:
    out: AwsVpcConfiguration = {}  # type: ignore[typeddict-item]
    if "Subnets" in data:
        import aws_sdk_scheduler.types.subnets

        out["subnets"] = aws_sdk_scheduler.types.subnets.deserialize_json(
            data["Subnets"]
        )
    else:
        raise DeserializationError("AwsVpcConfiguration.subnets required")
    if "SecurityGroups" in data:
        import aws_sdk_scheduler.types.security_groups

        out["security_groups"] = (
            aws_sdk_scheduler.types.security_groups.deserialize_json(
                data["SecurityGroups"]
            )
        )
    if "AssignPublicIp" in data:
        out["assign_public_ip"] = data["AssignPublicIp"]
    return out
