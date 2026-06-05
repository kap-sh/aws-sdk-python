"""Generated from Smithy shape ``com.amazonaws.ec2#GetImageAncestryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_ancestry_entry_list


class GetImageAncestryResult(TypedDict):
    image_ancestry_entries: NotRequired[
        "aws_sdk_ec2.types.image_ancestry_entry_list.ImageAncestryEntryList"
    ]
    """<p>A list of entries in the AMI ancestry chain, from the specified AMI to the root AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetImageAncestryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_ancestry_entries" in value:
        import aws_sdk_ec2.types.image_ancestry_entry_list

        aws_sdk_ec2.types.image_ancestry_entry_list.serialize_ec2_query(
            value["image_ancestry_entries"], pairs, f"{prefix}.ImageAncestryEntrySet"
        )


def deserialize_ec2_query(el: Element) -> GetImageAncestryResult:
    out: GetImageAncestryResult = {}  # type: ignore[typeddict-item]
    if el.find("ImageAncestryEntrySet") is not None:
        import aws_sdk_ec2.types.image_ancestry_entry_list

        out["image_ancestry_entries"] = (
            aws_sdk_ec2.types.image_ancestry_entry_list.deserialize_ec2_query(
                el, "ImageAncestryEntrySet"
            )
        )
    return out
