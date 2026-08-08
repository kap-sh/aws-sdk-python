"""Generated from Smithy shape ``com.amazonaws.ec2#GetImageAncestryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_ancestry_entry_list


class GetImageAncestryResult(TypedDict, closed=True):
    image_ancestry_entries: NotRequired[
        "capo_ec2.types.image_ancestry_entry_list.ImageAncestryEntryList"
    ]
    """<p>A list of entries in the AMI ancestry chain, from the specified AMI to the root AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetImageAncestryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_ancestry_entries" in value:
        import capo_ec2.types.image_ancestry_entry_list

        capo_ec2.types.image_ancestry_entry_list.serialize_ec2_query(
            value["image_ancestry_entries"], pairs, f"{key_prefix}ImageAncestryEntrySet"
        )


def deserialize_ec2_query(el: Element) -> GetImageAncestryResult:
    out: GetImageAncestryResult = {}  # type: ignore[typeddict-item]
    if el.find("imageAncestryEntrySet") is not None:
        import capo_ec2.types.image_ancestry_entry_list

        out["image_ancestry_entries"] = (
            capo_ec2.types.image_ancestry_entry_list.deserialize_ec2_query(
                el, "imageAncestryEntrySet"
            )
        )
    return out
