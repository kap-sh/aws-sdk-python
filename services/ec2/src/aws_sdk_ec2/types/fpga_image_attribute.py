"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageAttribute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.load_permission_list
    import aws_sdk_ec2.types.product_code_list
    import aws_sdk_ec2.types.string


class FpgaImageAttribute(TypedDict):
    fpga_image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AFI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the AFI.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the AFI.</p>"""
    load_permissions: NotRequired[
        "aws_sdk_ec2.types.load_permission_list.LoadPermissionList"
    ]
    """<p>The load permissions.</p>"""
    product_codes: NotRequired["aws_sdk_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FpgaImageAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "fpga_image_id" in value:
        pairs.append((f"{prefix}.FpgaImageId", str(value["fpga_image_id"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "load_permissions" in value:
        import aws_sdk_ec2.types.load_permission_list

        aws_sdk_ec2.types.load_permission_list.serialize_ec2_query(
            value["load_permissions"], pairs, f"{prefix}.LoadPermissions"
        )
    if "product_codes" in value:
        import aws_sdk_ec2.types.product_code_list

        aws_sdk_ec2.types.product_code_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{prefix}.ProductCodes"
        )


def deserialize_ec2_query(el: Element) -> FpgaImageAttribute:
    out: FpgaImageAttribute = {}  # type: ignore[typeddict-item]
    child_fpga_image_id = el.find("FpgaImageId")
    if child_fpga_image_id is not None:
        out["fpga_image_id"] = str(child_fpga_image_id.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("LoadPermissions") is not None:
        import aws_sdk_ec2.types.load_permission_list

        out["load_permissions"] = (
            aws_sdk_ec2.types.load_permission_list.deserialize_ec2_query(
                el, "LoadPermissions"
            )
        )
    if el.find("ProductCodes") is not None:
        import aws_sdk_ec2.types.product_code_list

        out["product_codes"] = (
            aws_sdk_ec2.types.product_code_list.deserialize_ec2_query(
                el, "ProductCodes"
            )
        )
    return out
