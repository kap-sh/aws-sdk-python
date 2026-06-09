"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFpgaImagesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_image_list
    import aws_sdk_ec2.types.next_token


class DescribeFpgaImagesResult(TypedDict):
    fpga_images: NotRequired["aws_sdk_ec2.types.fpga_image_list.FpgaImageList"]
    """<p>Information about the FPGA images.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFpgaImagesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "fpga_images" in value:
        import aws_sdk_ec2.types.fpga_image_list

        aws_sdk_ec2.types.fpga_image_list.serialize_ec2_query(
            value["fpga_images"], pairs, f"{prefix}.FpgaImageSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeFpgaImagesResult:
    out: DescribeFpgaImagesResult = {}  # type: ignore[typeddict-item]
    if el.find("FpgaImageSet") is not None:
        import aws_sdk_ec2.types.fpga_image_list

        out["fpga_images"] = aws_sdk_ec2.types.fpga_image_list.deserialize_ec2_query(
            el, "FpgaImageSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
