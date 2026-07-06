"""Generated from Smithy shape ``com.amazonaws.guardduty#ScannedResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.ebs_snapshot
    import aws_sdk_guardduty.types.volume_detail


class ScannedResourceDetails(TypedDict, closed=True):
    ebs_volume: NotRequired["aws_sdk_guardduty.types.volume_detail.VolumeDetail"]
    """<p>Contains information about the EBS volume that was scanned.</p>"""
    ebs_snapshot: NotRequired["aws_sdk_guardduty.types.ebs_snapshot.EbsSnapshot"]
    """<p>Contains information about the EBS snapshot that was scanned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScannedResourceDetails) -> dict:
    out: dict = {}
    if "ebs_volume" in value:
        import aws_sdk_guardduty.types.volume_detail

        out["ebsVolume"] = aws_sdk_guardduty.types.volume_detail.serialize_json(
            value["ebs_volume"]
        )
    if "ebs_snapshot" in value:
        import aws_sdk_guardduty.types.ebs_snapshot

        out["ebsSnapshot"] = aws_sdk_guardduty.types.ebs_snapshot.serialize_json(
            value["ebs_snapshot"]
        )
    return out


def deserialize_json(data: dict) -> ScannedResourceDetails:
    out: ScannedResourceDetails = {}  # type: ignore[typeddict-item]
    if "ebsVolume" in data:
        import aws_sdk_guardduty.types.volume_detail

        out["ebs_volume"] = aws_sdk_guardduty.types.volume_detail.deserialize_json(
            data["ebsVolume"]
        )
    if "ebsSnapshot" in data:
        import aws_sdk_guardduty.types.ebs_snapshot

        out["ebs_snapshot"] = aws_sdk_guardduty.types.ebs_snapshot.deserialize_json(
            data["ebsSnapshot"]
        )
    return out
