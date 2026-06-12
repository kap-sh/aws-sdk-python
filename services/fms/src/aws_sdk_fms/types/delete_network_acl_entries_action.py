"""Generated from Smithy shape ``com.amazonaws.fms#DeleteNetworkAclEntriesAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.action_target
    import aws_sdk_fms.types.boolean
    import aws_sdk_fms.types.entries_description
    import aws_sdk_fms.types.length_bounded_string


class DeleteNetworkAclEntriesAction(TypedDict):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>Brief description of this remediation action. </p>"""
    network_acl_id: NotRequired["aws_sdk_fms.types.action_target.ActionTarget"]
    """<p>The network ACL that's associated with the remediation action.</p>"""
    network_acl_entries_to_be_deleted: NotRequired[
        "aws_sdk_fms.types.entries_description.EntriesDescription"
    ]
    """<p>Lists the entries that the remediation action would delete.</p>"""
    fms_can_remediate: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNetworkAclEntriesAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "network_acl_id" in value:
        import aws_sdk_fms.types.action_target

        out["NetworkAclId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
            value["network_acl_id"]
        )
    if "network_acl_entries_to_be_deleted" in value:
        import aws_sdk_fms.types.entries_description

        out["NetworkAclEntriesToBeDeleted"] = (
            aws_sdk_fms.types.entries_description.serialize_aws_json_1_1(
                value["network_acl_entries_to_be_deleted"]
            )
        )
    out["FMSCanRemediate"] = value.get("fms_can_remediate", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNetworkAclEntriesAction:
    out: DeleteNetworkAclEntriesAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "NetworkAclId" in data:
        import aws_sdk_fms.types.action_target

        out["network_acl_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["NetworkAclId"]
            )
        )
    if "NetworkAclEntriesToBeDeleted" in data:
        import aws_sdk_fms.types.entries_description

        out["network_acl_entries_to_be_deleted"] = (
            aws_sdk_fms.types.entries_description.deserialize_aws_json_1_1(
                data["NetworkAclEntriesToBeDeleted"]
            )
        )
    if "FMSCanRemediate" in data:
        out["fms_can_remediate"] = data["FMSCanRemediate"]
    else:
        out["fms_can_remediate"] = False
    return out
