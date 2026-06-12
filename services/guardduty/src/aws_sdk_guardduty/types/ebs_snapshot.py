"""Generated from Smithy shape ``com.amazonaws.guardduty#EbsSnapshot``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.non_empty_string


class EbsSnapshot(TypedDict):
    device_name: NotRequired["aws_sdk_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>The device name of the EBS snapshot that was scanned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsSnapshot) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    return out


def deserialize_json(data: dict) -> EbsSnapshot:
    out: EbsSnapshot = {}  # type: ignore[typeddict-item]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    return out
