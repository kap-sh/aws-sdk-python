"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySnapshotAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.create_volume_permission_modifications
    import capo_ec2.types.group_name_string_list
    import capo_ec2.types.operation_type
    import capo_ec2.types.snapshot_attribute_name
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.user_id_string_list


class ModifySnapshotAttributeRequest(TypedDict, closed=True):
    attribute: NotRequired[
        "capo_ec2.types.snapshot_attribute_name.SnapshotAttributeName"
    ]
    """<p>The snapshot attribute to modify. Only volume creation permissions can be modified.</p>"""
    create_volume_permission: NotRequired[
        "capo_ec2.types.create_volume_permission_modifications.CreateVolumePermissionModifications"
    ]
    """<p>A JSON representation of the snapshot attribute modification.</p>"""
    group_names: NotRequired[
        "capo_ec2.types.group_name_string_list.GroupNameStringList"
    ]
    """<p>The group to modify for the snapshot.</p>"""
    operation_type: NotRequired["capo_ec2.types.operation_type.OperationType"]
    """<p>The type of operation to perform to the attribute.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    user_ids: NotRequired["capo_ec2.types.user_id_string_list.UserIdStringList"]
    """<p>The account ID to modify for the snapshot.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifySnapshotAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute" in value:
        import capo_ec2.types.snapshot_attribute_name

        capo_ec2.types.snapshot_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{key_prefix}Attribute"
        )
    if "create_volume_permission" in value:
        import capo_ec2.types.create_volume_permission_modifications

        capo_ec2.types.create_volume_permission_modifications.serialize_ec2_query(
            value["create_volume_permission"],
            pairs,
            f"{key_prefix}CreateVolumePermission",
        )
    if "group_names" in value:
        import capo_ec2.types.group_name_string_list

        capo_ec2.types.group_name_string_list.serialize_ec2_query(
            value["group_names"], pairs, f"{key_prefix}UserGroup"
        )
    if "operation_type" in value:
        import capo_ec2.types.operation_type

        capo_ec2.types.operation_type.serialize_ec2_query(
            value["operation_type"], pairs, f"{key_prefix}OperationType"
        )
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "user_ids" in value:
        import capo_ec2.types.user_id_string_list

        capo_ec2.types.user_id_string_list.serialize_ec2_query(
            value["user_ids"], pairs, f"{key_prefix}UserId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifySnapshotAttributeRequest:
    out: ModifySnapshotAttributeRequest = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import capo_ec2.types.snapshot_attribute_name

        out["attribute"] = capo_ec2.types.snapshot_attribute_name.deserialize_ec2_query(
            child_attribute
        )
    child_create_volume_permission = el.find("CreateVolumePermission")
    if child_create_volume_permission is not None:
        import capo_ec2.types.create_volume_permission_modifications

        out["create_volume_permission"] = (
            capo_ec2.types.create_volume_permission_modifications.deserialize_ec2_query(
                child_create_volume_permission
            )
        )
    if el.find("UserGroup") is not None:
        import capo_ec2.types.group_name_string_list

        out["group_names"] = (
            capo_ec2.types.group_name_string_list.deserialize_ec2_query(el, "UserGroup")
        )
    child_operation_type = el.find("OperationType")
    if child_operation_type is not None:
        import capo_ec2.types.operation_type

        out["operation_type"] = capo_ec2.types.operation_type.deserialize_ec2_query(
            child_operation_type
        )
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    if el.find("UserId") is not None:
        import capo_ec2.types.user_id_string_list

        out["user_ids"] = capo_ec2.types.user_id_string_list.deserialize_ec2_query(
            el, "UserId"
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
