"""Generated from Smithy shape ``com.amazonaws.fms#CreateNetworkAclAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.action_target
    import aws_sdk_fms.types.boolean
    import aws_sdk_fms.types.length_bounded_string


class CreateNetworkAclAction(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>Brief description of this remediation action. </p>"""
    vpc: NotRequired["aws_sdk_fms.types.action_target.ActionTarget"]
    """<p>The VPC that's associated with the remediation action.</p>"""
    fms_can_remediate: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNetworkAclAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc" in value:
        import aws_sdk_fms.types.action_target

        out["Vpc"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
            value["vpc"]
        )
    out["FMSCanRemediate"] = value.get("fms_can_remediate", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNetworkAclAction:
    out: CreateNetworkAclAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Vpc" in data:
        import aws_sdk_fms.types.action_target

        out["vpc"] = aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
            data["Vpc"]
        )
    if "FMSCanRemediate" in data:
        out["fms_can_remediate"] = data["FMSCanRemediate"]
    else:
        out["fms_can_remediate"] = False
    return out
