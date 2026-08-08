"""Generated from Smithy shape ``com.amazonaws.ec2#ImageAncestryEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_id
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class ImageAncestryEntry(TypedDict, closed=True):
    creation_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when this AMI was created.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of this AMI.</p>"""
    image_owner_alias: NotRequired["capo_ec2.types.string.String"]
    """<p>The owner alias (<code>amazon</code> | <code>aws-backup-vault</code> | <code>aws-marketplace</code> ) of this AMI, if one is assigned. Otherwise, the value is <code>null</code>.</p>"""
    source_image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the parent AMI.</p>"""
    source_image_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the parent AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageAncestryEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "creation_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_date"], pairs, f"{key_prefix}CreationDate"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "image_owner_alias" in value:
        pairs.append((f"{key_prefix}ImageOwnerAlias", str(value["image_owner_alias"])))
    if "source_image_id" in value:
        pairs.append((f"{key_prefix}SourceImageId", str(value["source_image_id"])))
    if "source_image_region" in value:
        pairs.append(
            (f"{key_prefix}SourceImageRegion", str(value["source_image_region"]))
        )


def deserialize_ec2_query(el: Element) -> ImageAncestryEntry:
    out: ImageAncestryEntry = {}  # type: ignore[typeddict-item]
    child_creation_date = el.find("creationDate")
    if child_creation_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["creation_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_date
            )
        )
    child_image_id = el.find("imageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_image_owner_alias = el.find("imageOwnerAlias")
    if child_image_owner_alias is not None:
        out["image_owner_alias"] = str(child_image_owner_alias.text or "")
    child_source_image_id = el.find("sourceImageId")
    if child_source_image_id is not None:
        out["source_image_id"] = str(child_source_image_id.text or "")
    child_source_image_region = el.find("sourceImageRegion")
    if child_source_image_region is not None:
        out["source_image_region"] = str(child_source_image_region.text or "")
    return out
