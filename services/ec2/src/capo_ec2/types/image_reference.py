"""Generated from Smithy shape ``com.amazonaws.ec2#ImageReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_id
    import capo_ec2.types.image_reference_resource_type
    import capo_ec2.types.string


class ImageReference(TypedDict, closed=True):
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the referenced image.</p>"""
    resource_type: NotRequired[
        "capo_ec2.types.image_reference_resource_type.ImageReferenceResourceType"
    ]
    """<p>The type of resource referencing the image.</p>"""
    arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource referencing the image.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageReference, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "resource_type" in value:
        import capo_ec2.types.image_reference_resource_type

        capo_ec2.types.image_reference_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))


def deserialize_ec2_query(el: Element) -> ImageReference:
    out: ImageReference = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.image_reference_resource_type

        out["resource_type"] = (
            capo_ec2.types.image_reference_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
