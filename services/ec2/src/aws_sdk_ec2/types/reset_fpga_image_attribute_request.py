"""Generated from Smithy shape ``com.amazonaws.ec2#ResetFpgaImageAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fpga_image_id
    import aws_sdk_ec2.types.reset_fpga_image_attribute_name


class ResetFpgaImageAttributeRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fpga_image_id: NotRequired["aws_sdk_ec2.types.fpga_image_id.FpgaImageId"]
    """<p>The ID of the AFI.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.reset_fpga_image_attribute_name.ResetFpgaImageAttributeName"
    ]
    """<p>The attribute.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResetFpgaImageAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "fpga_image_id" in value:
        pairs.append((f"{prefix}.FpgaImageId", str(value["fpga_image_id"])))
    if "attribute" in value:
        import aws_sdk_ec2.types.reset_fpga_image_attribute_name

        aws_sdk_ec2.types.reset_fpga_image_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{prefix}.Attribute"
        )


def deserialize_ec2_query(el: Element) -> ResetFpgaImageAttributeRequest:
    out: ResetFpgaImageAttributeRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_fpga_image_id = el.find("FpgaImageId")
    if child_fpga_image_id is not None:
        out["fpga_image_id"] = str(child_fpga_image_id.text or "")
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import aws_sdk_ec2.types.reset_fpga_image_attribute_name

        out["attribute"] = (
            aws_sdk_ec2.types.reset_fpga_image_attribute_name.deserialize_ec2_query(
                child_attribute
            )
        )
    return out
