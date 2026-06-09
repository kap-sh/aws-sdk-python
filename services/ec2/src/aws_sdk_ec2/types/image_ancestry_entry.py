"""Generated from Smithy shape ``com.amazonaws.ec2#ImageAncestryEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class ImageAncestryEntry(TypedDict):
    creation_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when this AMI was created.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of this AMI.</p>"""
    image_owner_alias: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The owner alias (<code>amazon</code> | <code>aws-backup-vault</code> | <code>aws-marketplace</code> ) of this AMI, if one is assigned. Otherwise, the value is <code>null</code>.</p>"""
    source_image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the parent AMI.</p>"""
    source_image_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the parent AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageAncestryEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "creation_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_date"], pairs, f"{prefix}.CreationDate"
        )
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "image_owner_alias" in value:
        pairs.append((f"{prefix}.ImageOwnerAlias", str(value["image_owner_alias"])))
    if "source_image_id" in value:
        pairs.append((f"{prefix}.SourceImageId", str(value["source_image_id"])))
    if "source_image_region" in value:
        pairs.append((f"{prefix}.SourceImageRegion", str(value["source_image_region"])))


def deserialize_ec2_query(el: Element) -> ImageAncestryEntry:
    out: ImageAncestryEntry = {}  # type: ignore[typeddict-item]
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["creation_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_date
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_image_owner_alias = el.find("ImageOwnerAlias")
    if child_image_owner_alias is not None:
        out["image_owner_alias"] = str(child_image_owner_alias.text or "")
    child_source_image_id = el.find("SourceImageId")
    if child_source_image_id is not None:
        out["source_image_id"] = str(child_source_image_id.text or "")
    child_source_image_region = el.find("SourceImageRegion")
    if child_source_image_region is not None:
        out["source_image_region"] = str(child_source_image_region.text or "")
    return out
