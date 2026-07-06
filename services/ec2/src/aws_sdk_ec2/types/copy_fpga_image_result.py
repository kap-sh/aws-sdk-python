"""Generated from Smithy shape ``com.amazonaws.ec2#CopyFpgaImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CopyFpgaImageResult(TypedDict, closed=True):
    fpga_image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the new AFI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CopyFpgaImageResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "fpga_image_id" in value:
        pairs.append((f"{prefix}.FpgaImageId", str(value["fpga_image_id"])))


def deserialize_ec2_query(el: Element) -> CopyFpgaImageResult:
    out: CopyFpgaImageResult = {}  # type: ignore[typeddict-item]
    child_fpga_image_id = el.find("FpgaImageId")
    if child_fpga_image_id is not None:
        out["fpga_image_id"] = str(child_fpga_image_id.text or "")
    return out
