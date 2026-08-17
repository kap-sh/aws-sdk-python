"""Generated from Smithy shape ``com.amazonaws.ecr#ImageScanStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.scan_status
    import capo_ecr.types.scan_status_description


class ImageScanStatus(TypedDict, closed=True):
    status: NotRequired["capo_ecr.types.scan_status.ScanStatus"]
    """<p>The current state of an image scan.</p>"""
    description: NotRequired[
        "capo_ecr.types.scan_status_description.ScanStatusDescription"
    ]
    """<p>The description of the image scan status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageScanStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_ecr.types.scan_status

        out["status"] = capo_ecr.types.scan_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageScanStatus:
    out: ImageScanStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_ecr.types.scan_status

        out["status"] = capo_ecr.types.scan_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
