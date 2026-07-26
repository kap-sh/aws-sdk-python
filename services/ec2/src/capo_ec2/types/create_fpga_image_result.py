"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFpgaImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class CreateFpgaImageResult(TypedDict, closed=True):
    fpga_image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The FPGA image identifier (AFI ID).</p>"""
    fpga_image_global_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The global FPGA image identifier (AGFI ID).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFpgaImageResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "fpga_image_id" in value:
        pairs.append((f"{prefix}.FpgaImageId", str(value["fpga_image_id"])))
    if "fpga_image_global_id" in value:
        pairs.append(
            (f"{prefix}.FpgaImageGlobalId", str(value["fpga_image_global_id"]))
        )


def deserialize_ec2_query(el: Element) -> CreateFpgaImageResult:
    out: CreateFpgaImageResult = {}  # type: ignore[typeddict-item]
    child_fpga_image_id = el.find("FpgaImageId")
    if child_fpga_image_id is not None:
        out["fpga_image_id"] = str(child_fpga_image_id.text or "")
    child_fpga_image_global_id = el.find("FpgaImageGlobalId")
    if child_fpga_image_global_id is not None:
        out["fpga_image_global_id"] = str(child_fpga_image_global_id.text or "")
    return out
