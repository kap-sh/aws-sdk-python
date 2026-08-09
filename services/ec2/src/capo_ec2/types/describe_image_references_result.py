"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageReferencesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_reference_list
    import capo_ec2.types.string


class DescribeImageReferencesResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    image_references: NotRequired[
        "capo_ec2.types.image_reference_list.ImageReferenceList"
    ]
    """<p>The resources that are referencing the specified images.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImageReferencesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "image_references" in value:
        import capo_ec2.types.image_reference_list

        capo_ec2.types.image_reference_list.serialize_ec2_query(
            value["image_references"], pairs, f"{key_prefix}ImageReferenceSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeImageReferencesResult:
    out: DescribeImageReferencesResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_image_references = el.find("imageReferenceSet")
    if child_image_references is not None:
        import capo_ec2.types.image_reference_list

        out["image_references"] = (
            capo_ec2.types.image_reference_list.deserialize_ec2_query(
                child_image_references
            )
        )
    return out
