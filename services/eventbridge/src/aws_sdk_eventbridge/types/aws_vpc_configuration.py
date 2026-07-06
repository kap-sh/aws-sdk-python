"""Generated from Smithy shape ``com.amazonaws.eventbridge#AwsVpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.assign_public_ip
    import aws_sdk_eventbridge.types.string_list


class AwsVpcConfiguration(TypedDict, closed=True):
    subnets: "aws_sdk_eventbridge.types.string_list.StringList"
    """<p>Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.</p>"""
    security_groups: NotRequired["aws_sdk_eventbridge.types.string_list.StringList"]
    """<p>Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.</p>"""
    assign_public_ip: NotRequired[
        "aws_sdk_eventbridge.types.assign_public_ip.AssignPublicIp"
    ]
    """<p>Specifies whether the task's elastic network interface receives a public IP address. You can specify <code>ENABLED</code> only when <code>LaunchType</code> in <code>EcsParameters</code> is set to <code>FARGATE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsVpcConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_eventbridge.types.string_list

    out["Subnets"] = aws_sdk_eventbridge.types.string_list.serialize_aws_json_1_1(
        value["subnets"]
    )
    if "security_groups" in value:
        import aws_sdk_eventbridge.types.string_list

        out["SecurityGroups"] = (
            aws_sdk_eventbridge.types.string_list.serialize_aws_json_1_1(
                value["security_groups"]
            )
        )
    if "assign_public_ip" in value:
        import aws_sdk_eventbridge.types.assign_public_ip

        out["AssignPublicIp"] = (
            aws_sdk_eventbridge.types.assign_public_ip.serialize_aws_json_1_1(
                value["assign_public_ip"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AwsVpcConfiguration:
    out: AwsVpcConfiguration = {}  # type: ignore[typeddict-item]
    if "Subnets" in data:
        import aws_sdk_eventbridge.types.string_list

        out["subnets"] = aws_sdk_eventbridge.types.string_list.deserialize_aws_json_1_1(
            data["Subnets"]
        )
    else:
        raise DeserializationError("AwsVpcConfiguration.subnets required")
    if "SecurityGroups" in data:
        import aws_sdk_eventbridge.types.string_list

        out["security_groups"] = (
            aws_sdk_eventbridge.types.string_list.deserialize_aws_json_1_1(
                data["SecurityGroups"]
            )
        )
    if "AssignPublicIp" in data:
        import aws_sdk_eventbridge.types.assign_public_ip

        out["assign_public_ip"] = (
            aws_sdk_eventbridge.types.assign_public_ip.deserialize_aws_json_1_1(
                data["AssignPublicIp"]
            )
        )
    return out
