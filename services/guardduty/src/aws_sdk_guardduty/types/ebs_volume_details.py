"""Generated from Smithy shape ``com.amazonaws.guardduty#EbsVolumeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.volume_details


class EbsVolumeDetails(TypedDict):
    scanned_volume_details: NotRequired[
        "aws_sdk_guardduty.types.volume_details.VolumeDetails"
    ]
    """<p>List of EBS volumes that were scanned.</p>"""
    skipped_volume_details: NotRequired[
        "aws_sdk_guardduty.types.volume_details.VolumeDetails"
    ]
    """<p>List of EBS volumes that were skipped from the malware scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsVolumeDetails) -> dict:
    out: dict = {}
    if "scanned_volume_details" in value:
        import aws_sdk_guardduty.types.volume_details

        out["scannedVolumeDetails"] = (
            aws_sdk_guardduty.types.volume_details.serialize_json(
                value["scanned_volume_details"]
            )
        )
    if "skipped_volume_details" in value:
        import aws_sdk_guardduty.types.volume_details

        out["skippedVolumeDetails"] = (
            aws_sdk_guardduty.types.volume_details.serialize_json(
                value["skipped_volume_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> EbsVolumeDetails:
    out: EbsVolumeDetails = {}  # type: ignore[typeddict-item]
    if "scannedVolumeDetails" in data:
        import aws_sdk_guardduty.types.volume_details

        out["scanned_volume_details"] = (
            aws_sdk_guardduty.types.volume_details.deserialize_json(
                data["scannedVolumeDetails"]
            )
        )
    if "skippedVolumeDetails" in data:
        import aws_sdk_guardduty.types.volume_details

        out["skipped_volume_details"] = (
            aws_sdk_guardduty.types.volume_details.deserialize_json(
                data["skippedVolumeDetails"]
            )
        )
    return out
