"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFpgaImagesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fpga_image_list
    import capo_ec2.types.next_token


class DescribeFpgaImagesResult(TypedDict, closed=True):
    fpga_images: NotRequired["capo_ec2.types.fpga_image_list.FpgaImageList"]
    """<p>Information about the FPGA images.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFpgaImagesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fpga_images" in value:
        import capo_ec2.types.fpga_image_list

        capo_ec2.types.fpga_image_list.serialize_ec2_query(
            value["fpga_images"], pairs, f"{key_prefix}FpgaImageSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeFpgaImagesResult:
    out: DescribeFpgaImagesResult = {}  # type: ignore[typeddict-item]
    child_fpga_images = el.find("fpgaImageSet")
    if child_fpga_images is not None:
        import capo_ec2.types.fpga_image_list

        out["fpga_images"] = capo_ec2.types.fpga_image_list.deserialize_ec2_query(
            child_fpga_images
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
