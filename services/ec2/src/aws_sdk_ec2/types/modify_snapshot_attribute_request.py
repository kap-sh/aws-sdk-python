"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySnapshotAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_volume_permission_modifications
    import aws_sdk_ec2.types.group_name_string_list
    import aws_sdk_ec2.types.operation_type
    import aws_sdk_ec2.types.snapshot_attribute_name
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.user_id_string_list


class ModifySnapshotAttributeRequest(TypedDict):
    attribute: NotRequired[
        "aws_sdk_ec2.types.snapshot_attribute_name.SnapshotAttributeName"
    ]
    """<p>The snapshot attribute to modify. Only volume creation permissions can be modified.</p>"""
    create_volume_permission: NotRequired[
        "aws_sdk_ec2.types.create_volume_permission_modifications.CreateVolumePermissionModifications"
    ]
    """<p>A JSON representation of the snapshot attribute modification.</p>"""
    group_names: NotRequired[
        "aws_sdk_ec2.types.group_name_string_list.GroupNameStringList"
    ]
    """<p>The group to modify for the snapshot.</p>"""
    operation_type: NotRequired["aws_sdk_ec2.types.operation_type.OperationType"]
    """<p>The type of operation to perform to the attribute.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    user_ids: NotRequired["aws_sdk_ec2.types.user_id_string_list.UserIdStringList"]
    """<p>The account ID to modify for the snapshot.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifySnapshotAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute" in value:
        import aws_sdk_ec2.types.snapshot_attribute_name

        aws_sdk_ec2.types.snapshot_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{prefix}.Attribute"
        )
    if "create_volume_permission" in value:
        import aws_sdk_ec2.types.create_volume_permission_modifications

        aws_sdk_ec2.types.create_volume_permission_modifications.serialize_ec2_query(
            value["create_volume_permission"], pairs, f"{prefix}.CreateVolumePermission"
        )
    if "group_names" in value:
        import aws_sdk_ec2.types.group_name_string_list

        aws_sdk_ec2.types.group_name_string_list.serialize_ec2_query(
            value["group_names"], pairs, f"{prefix}.GroupNames"
        )
    if "operation_type" in value:
        import aws_sdk_ec2.types.operation_type

        aws_sdk_ec2.types.operation_type.serialize_ec2_query(
            value["operation_type"], pairs, f"{prefix}.OperationType"
        )
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "user_ids" in value:
        import aws_sdk_ec2.types.user_id_string_list

        aws_sdk_ec2.types.user_id_string_list.serialize_ec2_query(
            value["user_ids"], pairs, f"{prefix}.UserIds"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifySnapshotAttributeRequest:
    out: ModifySnapshotAttributeRequest = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import aws_sdk_ec2.types.snapshot_attribute_name

        out["attribute"] = (
            aws_sdk_ec2.types.snapshot_attribute_name.deserialize_ec2_query(
                child_attribute
            )
        )
    child_create_volume_permission = el.find("CreateVolumePermission")
    if child_create_volume_permission is not None:
        import aws_sdk_ec2.types.create_volume_permission_modifications

        out["create_volume_permission"] = (
            aws_sdk_ec2.types.create_volume_permission_modifications.deserialize_ec2_query(
                child_create_volume_permission
            )
        )
    if el.find("GroupNames") is not None:
        import aws_sdk_ec2.types.group_name_string_list

        out["group_names"] = (
            aws_sdk_ec2.types.group_name_string_list.deserialize_ec2_query(
                el, "GroupNames"
            )
        )
    child_operation_type = el.find("OperationType")
    if child_operation_type is not None:
        import aws_sdk_ec2.types.operation_type

        out["operation_type"] = aws_sdk_ec2.types.operation_type.deserialize_ec2_query(
            child_operation_type
        )
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    if el.find("UserIds") is not None:
        import aws_sdk_ec2.types.user_id_string_list

        out["user_ids"] = aws_sdk_ec2.types.user_id_string_list.deserialize_ec2_query(
            el, "UserIds"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
