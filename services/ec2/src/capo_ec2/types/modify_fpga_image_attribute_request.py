"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyFpgaImageAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.fpga_image_attribute_name
    import capo_ec2.types.fpga_image_id
    import capo_ec2.types.load_permission_modifications
    import capo_ec2.types.operation_type
    import capo_ec2.types.product_code_string_list
    import capo_ec2.types.string
    import capo_ec2.types.user_group_string_list
    import capo_ec2.types.user_id_string_list


class ModifyFpgaImageAttributeRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fpga_image_id: NotRequired["capo_ec2.types.fpga_image_id.FpgaImageId"]
    """<p>The ID of the AFI.</p>"""
    attribute: NotRequired[
        "capo_ec2.types.fpga_image_attribute_name.FpgaImageAttributeName"
    ]
    """<p>The name of the attribute.</p>"""
    operation_type: NotRequired["capo_ec2.types.operation_type.OperationType"]
    """<p>The operation type.</p>"""
    user_ids: NotRequired["capo_ec2.types.user_id_string_list.UserIdStringList"]
    """<p>The Amazon Web Services account IDs. This parameter is valid only when modifying the <code>loadPermission</code> attribute.</p>"""
    user_groups: NotRequired[
        "capo_ec2.types.user_group_string_list.UserGroupStringList"
    ]
    """<p>The user groups. This parameter is valid only when modifying the <code>loadPermission</code> attribute.</p>"""
    product_codes: NotRequired[
        "capo_ec2.types.product_code_string_list.ProductCodeStringList"
    ]
    """<p>The product codes. After you add a product code to an AFI, it can't be removed. This parameter is valid only when modifying the <code>productCodes</code> attribute.</p>"""
    load_permission: NotRequired[
        "capo_ec2.types.load_permission_modifications.LoadPermissionModifications"
    ]
    """<p>The load permission for the AFI.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the AFI.</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>A name for the AFI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyFpgaImageAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "fpga_image_id" in value:
        pairs.append((f"{key_prefix}FpgaImageId", str(value["fpga_image_id"])))
    if "attribute" in value:
        import capo_ec2.types.fpga_image_attribute_name

        capo_ec2.types.fpga_image_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{key_prefix}Attribute"
        )
    if "operation_type" in value:
        import capo_ec2.types.operation_type

        capo_ec2.types.operation_type.serialize_ec2_query(
            value["operation_type"], pairs, f"{key_prefix}OperationType"
        )
    if "user_ids" in value:
        import capo_ec2.types.user_id_string_list

        capo_ec2.types.user_id_string_list.serialize_ec2_query(
            value["user_ids"], pairs, f"{key_prefix}UserId"
        )
    if "user_groups" in value:
        import capo_ec2.types.user_group_string_list

        capo_ec2.types.user_group_string_list.serialize_ec2_query(
            value["user_groups"], pairs, f"{key_prefix}UserGroup"
        )
    if "product_codes" in value:
        import capo_ec2.types.product_code_string_list

        capo_ec2.types.product_code_string_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{key_prefix}ProductCode"
        )
    if "load_permission" in value:
        import capo_ec2.types.load_permission_modifications

        capo_ec2.types.load_permission_modifications.serialize_ec2_query(
            value["load_permission"], pairs, f"{key_prefix}LoadPermission"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))


def deserialize_ec2_query(el: Element) -> ModifyFpgaImageAttributeRequest:
    out: ModifyFpgaImageAttributeRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_fpga_image_id = el.find("FpgaImageId")
    if child_fpga_image_id is not None:
        out["fpga_image_id"] = str(child_fpga_image_id.text or "")
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import capo_ec2.types.fpga_image_attribute_name

        out["attribute"] = (
            capo_ec2.types.fpga_image_attribute_name.deserialize_ec2_query(
                child_attribute
            )
        )
    child_operation_type = el.find("OperationType")
    if child_operation_type is not None:
        import capo_ec2.types.operation_type

        out["operation_type"] = capo_ec2.types.operation_type.deserialize_ec2_query(
            child_operation_type
        )
    if el.find("UserId") is not None:
        import capo_ec2.types.user_id_string_list

        out["user_ids"] = capo_ec2.types.user_id_string_list.deserialize_ec2_query(
            el, "UserId"
        )
    if el.find("UserGroup") is not None:
        import capo_ec2.types.user_group_string_list

        out["user_groups"] = (
            capo_ec2.types.user_group_string_list.deserialize_ec2_query(el, "UserGroup")
        )
    if el.find("ProductCode") is not None:
        import capo_ec2.types.product_code_string_list

        out["product_codes"] = (
            capo_ec2.types.product_code_string_list.deserialize_ec2_query(
                el, "ProductCode"
            )
        )
    child_load_permission = el.find("LoadPermission")
    if child_load_permission is not None:
        import capo_ec2.types.load_permission_modifications

        out["load_permission"] = (
            capo_ec2.types.load_permission_modifications.deserialize_ec2_query(
                child_load_permission
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
