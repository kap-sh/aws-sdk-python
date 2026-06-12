"""Generated from Smithy shape ``com.amazonaws.fms#AwsEc2NetworkInterfaceViolations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_ec2_network_interface_violation

AwsEc2NetworkInterfaceViolations: TypeAlias = list[
    "aws_sdk_fms.types.aws_ec2_network_interface_violation.AwsEc2NetworkInterfaceViolation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsEc2NetworkInterfaceViolations) -> list:
    import aws_sdk_fms.types.aws_ec2_network_interface_violation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fms.types.aws_ec2_network_interface_violation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AwsEc2NetworkInterfaceViolations:
    import aws_sdk_fms.types.aws_ec2_network_interface_violation

    out: AwsEc2NetworkInterfaceViolations = []
    for item in data:
        out.append(
            aws_sdk_fms.types.aws_ec2_network_interface_violation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
