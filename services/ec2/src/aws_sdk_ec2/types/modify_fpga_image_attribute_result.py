"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyFpgaImageAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_image_attribute


class ModifyFpgaImageAttributeResult(TypedDict):
    fpga_image_attribute: NotRequired[
        "aws_sdk_ec2.types.fpga_image_attribute.FpgaImageAttribute"
    ]
    """<p>Information about the attribute.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyFpgaImageAttributeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "fpga_image_attribute" in value:
        import aws_sdk_ec2.types.fpga_image_attribute

        aws_sdk_ec2.types.fpga_image_attribute.serialize_ec2_query(
            value["fpga_image_attribute"], pairs, f"{prefix}.FpgaImageAttribute"
        )


def deserialize_ec2_query(el: Element) -> ModifyFpgaImageAttributeResult:
    out: ModifyFpgaImageAttributeResult = {}  # type: ignore[typeddict-item]
    child_fpga_image_attribute = el.find("FpgaImageAttribute")
    if child_fpga_image_attribute is not None:
        import aws_sdk_ec2.types.fpga_image_attribute

        out["fpga_image_attribute"] = (
            aws_sdk_ec2.types.fpga_image_attribute.deserialize_ec2_query(
                child_fpga_image_attribute
            )
        )
    return out
