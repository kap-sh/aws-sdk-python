"""Generated from Smithy shape ``com.amazonaws.fms#AwsEc2NetworkInterfaceViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.resource_id_list
    import aws_sdk_fms.types.violation_target


class AwsEc2NetworkInterfaceViolation(TypedDict, closed=True):
    violation_target: NotRequired["aws_sdk_fms.types.violation_target.ViolationTarget"]
    """<p>The resource ID of the network interface.</p>"""
    violating_security_groups: NotRequired[
        "aws_sdk_fms.types.resource_id_list.ResourceIdList"
    ]
    """<p>List of security groups that violate the rules specified in the primary security group of the Firewall Manager policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsEc2NetworkInterfaceViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "violating_security_groups" in value:
        import aws_sdk_fms.types.resource_id_list

        out["ViolatingSecurityGroups"] = (
            aws_sdk_fms.types.resource_id_list.serialize_aws_json_1_1(
                value["violating_security_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AwsEc2NetworkInterfaceViolation:
    out: AwsEc2NetworkInterfaceViolation = {}  # type: ignore[typeddict-item]
    if "ViolationTarget" in data:
        out["violation_target"] = data["ViolationTarget"]
    if "ViolatingSecurityGroups" in data:
        import aws_sdk_fms.types.resource_id_list

        out["violating_security_groups"] = (
            aws_sdk_fms.types.resource_id_list.deserialize_aws_json_1_1(
                data["ViolatingSecurityGroups"]
            )
        )
    return out
