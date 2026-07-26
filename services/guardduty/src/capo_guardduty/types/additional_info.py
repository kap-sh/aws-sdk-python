"""Generated from Smithy shape ``com.amazonaws.guardduty#AdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.non_empty_string


class AdditionalInfo(TypedDict, closed=True):
    version_id: NotRequired["capo_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>The version ID of the S3 object, if applicable.</p>"""
    device_name: NotRequired["capo_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>The device name of the EBS volume, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalInfo) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    return out


def deserialize_json(data: dict) -> AdditionalInfo:
    out: AdditionalInfo = {}  # type: ignore[typeddict-item]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    return out
