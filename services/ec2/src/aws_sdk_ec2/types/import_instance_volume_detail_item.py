"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceVolumeDetailItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_image_description
    import aws_sdk_ec2.types.disk_image_volume_description
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string


class ImportInstanceVolumeDetailItem(TypedDict, closed=True):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone where the resulting instance will reside.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone where the resulting instance will reside.</p>"""
    bytes_converted: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The number of bytes converted so far.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the task.</p>"""
    image: NotRequired["aws_sdk_ec2.types.disk_image_description.DiskImageDescription"]
    """<p>The image.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the import of this particular disk image.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status information or errors related to the disk image.</p>"""
    volume: NotRequired[
        "aws_sdk_ec2.types.disk_image_volume_description.DiskImageVolumeDescription"
    ]
    """<p>The volume.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportInstanceVolumeDetailItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "bytes_converted" in value:
        pairs.append((f"{prefix}.BytesConverted", str(value["bytes_converted"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "image" in value:
        import aws_sdk_ec2.types.disk_image_description

        aws_sdk_ec2.types.disk_image_description.serialize_ec2_query(
            value["image"], pairs, f"{prefix}.Image"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "volume" in value:
        import aws_sdk_ec2.types.disk_image_volume_description

        aws_sdk_ec2.types.disk_image_volume_description.serialize_ec2_query(
            value["volume"], pairs, f"{prefix}.Volume"
        )


def deserialize_ec2_query(el: Element) -> ImportInstanceVolumeDetailItem:
    out: ImportInstanceVolumeDetailItem = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_bytes_converted = el.find("BytesConverted")
    if child_bytes_converted is not None:
        out["bytes_converted"] = int(child_bytes_converted.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_image = el.find("Image")
    if child_image is not None:
        import aws_sdk_ec2.types.disk_image_description

        out["image"] = aws_sdk_ec2.types.disk_image_description.deserialize_ec2_query(
            child_image
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_volume = el.find("Volume")
    if child_volume is not None:
        import aws_sdk_ec2.types.disk_image_volume_description

        out["volume"] = (
            aws_sdk_ec2.types.disk_image_volume_description.deserialize_ec2_query(
                child_volume
            )
        )
    return out
