"""Generated from Smithy shape ``com.amazonaws.fms#ReplaceNetworkAclAssociationAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.action_target
    import aws_sdk_fms.types.boolean
    import aws_sdk_fms.types.length_bounded_string


class ReplaceNetworkAclAssociationAction(TypedDict):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>Brief description of this remediation action. </p>"""
    association_id: NotRequired["aws_sdk_fms.types.action_target.ActionTarget"]
    network_acl_id: NotRequired["aws_sdk_fms.types.action_target.ActionTarget"]
    """<p>The network ACL that's associated with the remediation action.</p>"""
    fms_can_remediate: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplaceNetworkAclAssociationAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "association_id" in value:
        import aws_sdk_fms.types.action_target

        out["AssociationId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
            value["association_id"]
        )
    if "network_acl_id" in value:
        import aws_sdk_fms.types.action_target

        out["NetworkAclId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
            value["network_acl_id"]
        )
    out["FMSCanRemediate"] = value.get("fms_can_remediate", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplaceNetworkAclAssociationAction:
    out: ReplaceNetworkAclAssociationAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "AssociationId" in data:
        import aws_sdk_fms.types.action_target

        out["association_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["AssociationId"]
            )
        )
    if "NetworkAclId" in data:
        import aws_sdk_fms.types.action_target

        out["network_acl_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["NetworkAclId"]
            )
        )
    if "FMSCanRemediate" in data:
        out["fms_can_remediate"] = data["FMSCanRemediate"]
    else:
        out["fms_can_remediate"] = False
    return out
