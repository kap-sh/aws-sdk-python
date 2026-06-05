"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyFpgaImageAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fpga_image_attribute_name
    import aws_sdk_ec2.types.fpga_image_id
    import aws_sdk_ec2.types.load_permission_modifications
    import aws_sdk_ec2.types.operation_type
    import aws_sdk_ec2.types.product_code_string_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_group_string_list
    import aws_sdk_ec2.types.user_id_string_list


class ModifyFpgaImageAttributeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fpga_image_id: NotRequired["aws_sdk_ec2.types.fpga_image_id.FpgaImageId"]
    """<p>The ID of the AFI.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.fpga_image_attribute_name.FpgaImageAttributeName"
    ]
    """<p>The name of the attribute.</p>"""
    operation_type: NotRequired["aws_sdk_ec2.types.operation_type.OperationType"]
    """<p>The operation type.</p>"""
    user_ids: NotRequired["aws_sdk_ec2.types.user_id_string_list.UserIdStringList"]
    """<p>The Amazon Web Services account IDs. This parameter is valid only when modifying the <code>loadPermission</code> attribute.</p>"""
    user_groups: NotRequired[
        "aws_sdk_ec2.types.user_group_string_list.UserGroupStringList"
    ]
    """<p>The user groups. This parameter is valid only when modifying the <code>loadPermission</code> attribute.</p>"""
    product_codes: NotRequired[
        "aws_sdk_ec2.types.product_code_string_list.ProductCodeStringList"
    ]
    """<p>The product codes. After you add a product code to an AFI, it can't be removed. This parameter is valid only when modifying the <code>productCodes</code> attribute.</p>"""
    load_permission: NotRequired[
        "aws_sdk_ec2.types.load_permission_modifications.LoadPermissionModifications"
    ]
    """<p>The load permission for the AFI.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the AFI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the AFI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyFpgaImageAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "fpga_image_id" in value:
        pairs.append((f"{prefix}.FpgaImageId", str(value["fpga_image_id"])))
    if "attribute" in value:
        import aws_sdk_ec2.types.fpga_image_attribute_name

        aws_sdk_ec2.types.fpga_image_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{prefix}.Attribute"
        )
    if "operation_type" in value:
        import aws_sdk_ec2.types.operation_type

        aws_sdk_ec2.types.operation_type.serialize_ec2_query(
            value["operation_type"], pairs, f"{prefix}.OperationType"
        )
    if "user_ids" in value:
        import aws_sdk_ec2.types.user_id_string_list

        aws_sdk_ec2.types.user_id_string_list.serialize_ec2_query(
            value["user_ids"], pairs, f"{prefix}.UserIds"
        )
    if "user_groups" in value:
        import aws_sdk_ec2.types.user_group_string_list

        aws_sdk_ec2.types.user_group_string_list.serialize_ec2_query(
            value["user_groups"], pairs, f"{prefix}.UserGroups"
        )
    if "product_codes" in value:
        import aws_sdk_ec2.types.product_code_string_list

        aws_sdk_ec2.types.product_code_string_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{prefix}.ProductCodes"
        )
    if "load_permission" in value:
        import aws_sdk_ec2.types.load_permission_modifications

        aws_sdk_ec2.types.load_permission_modifications.serialize_ec2_query(
            value["load_permission"], pairs, f"{prefix}.LoadPermission"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


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
        import aws_sdk_ec2.types.fpga_image_attribute_name

        out["attribute"] = (
            aws_sdk_ec2.types.fpga_image_attribute_name.deserialize_ec2_query(
                child_attribute
            )
        )
    child_operation_type = el.find("OperationType")
    if child_operation_type is not None:
        import aws_sdk_ec2.types.operation_type

        out["operation_type"] = aws_sdk_ec2.types.operation_type.deserialize_ec2_query(
            child_operation_type
        )
    if el.find("UserIds") is not None:
        import aws_sdk_ec2.types.user_id_string_list

        out["user_ids"] = aws_sdk_ec2.types.user_id_string_list.deserialize_ec2_query(
            el, "UserIds"
        )
    if el.find("UserGroups") is not None:
        import aws_sdk_ec2.types.user_group_string_list

        out["user_groups"] = (
            aws_sdk_ec2.types.user_group_string_list.deserialize_ec2_query(
                el, "UserGroups"
            )
        )
    if el.find("ProductCodes") is not None:
        import aws_sdk_ec2.types.product_code_string_list

        out["product_codes"] = (
            aws_sdk_ec2.types.product_code_string_list.deserialize_ec2_query(
                el, "ProductCodes"
            )
        )
    child_load_permission = el.find("LoadPermission")
    if child_load_permission is not None:
        import aws_sdk_ec2.types.load_permission_modifications

        out["load_permission"] = (
            aws_sdk_ec2.types.load_permission_modifications.deserialize_ec2_query(
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
