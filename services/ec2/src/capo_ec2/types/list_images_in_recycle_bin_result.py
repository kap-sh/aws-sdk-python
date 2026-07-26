"""Generated from Smithy shape ``com.amazonaws.ec2#ListImagesInRecycleBinResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_recycle_bin_info_list
    import capo_ec2.types.string


class ListImagesInRecycleBinResult(TypedDict, closed=True):
    images: NotRequired[
        "capo_ec2.types.image_recycle_bin_info_list.ImageRecycleBinInfoList"
    ]
    """<p>Information about the AMIs.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ListImagesInRecycleBinResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "images" in value:
        import capo_ec2.types.image_recycle_bin_info_list

        capo_ec2.types.image_recycle_bin_info_list.serialize_ec2_query(
            value["images"], pairs, f"{prefix}.ImageSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> ListImagesInRecycleBinResult:
    out: ListImagesInRecycleBinResult = {}  # type: ignore[typeddict-item]
    if el.find("ImageSet") is not None:
        import capo_ec2.types.image_recycle_bin_info_list

        out["images"] = (
            capo_ec2.types.image_recycle_bin_info_list.deserialize_ec2_query(
                el, "ImageSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
