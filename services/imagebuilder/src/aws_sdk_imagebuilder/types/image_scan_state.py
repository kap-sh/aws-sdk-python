"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_scan_status
    import aws_sdk_imagebuilder.types.non_empty_string


class ImageScanState(TypedDict, closed=True):
    status: NotRequired["aws_sdk_imagebuilder.types.image_scan_status.ImageScanStatus"]
    """<p>The current state of vulnerability scans for the image.</p>"""
    reason: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The reason for the scan status for the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_imagebuilder.types.image_scan_status

        out["status"] = aws_sdk_imagebuilder.types.image_scan_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ImageScanState:
    out: ImageScanState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_imagebuilder.types.image_scan_status

        out["status"] = aws_sdk_imagebuilder.types.image_scan_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
