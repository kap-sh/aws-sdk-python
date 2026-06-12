"""Generated from Smithy shape ``com.amazonaws.fms#AwsEc2InstanceViolation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_ec2_network_interface_violations
    import aws_sdk_fms.types.violation_target


class AwsEc2InstanceViolation(TypedDict):
    violation_target: NotRequired["aws_sdk_fms.types.violation_target.ViolationTarget"]
    """<p>The resource ID of the EC2 instance.</p>"""
    aws_ec2_network_interface_violations: NotRequired[
        "aws_sdk_fms.types.aws_ec2_network_interface_violations.AwsEc2NetworkInterfaceViolations"
    ]
    """<p>Violation detail for network interfaces associated with the EC2 instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsEc2InstanceViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "aws_ec2_network_interface_violations" in value:
        import aws_sdk_fms.types.aws_ec2_network_interface_violations

        out["AwsEc2NetworkInterfaceViolations"] = (
            aws_sdk_fms.types.aws_ec2_network_interface_violations.serialize_aws_json_1_1(
                value["aws_ec2_network_interface_violations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AwsEc2InstanceViolation:
    out: AwsEc2InstanceViolation = {}  # type: ignore[typeddict-item]
    if "ViolationTarget" in data:
        out["violation_target"] = data["ViolationTarget"]
    if "AwsEc2NetworkInterfaceViolations" in data:
        import aws_sdk_fms.types.aws_ec2_network_interface_violations

        out["aws_ec2_network_interface_violations"] = (
            aws_sdk_fms.types.aws_ec2_network_interface_violations.deserialize_aws_json_1_1(
                data["AwsEc2NetworkInterfaceViolations"]
            )
        )
    return out
