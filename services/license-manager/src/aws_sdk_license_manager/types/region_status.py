"""Generated from Smithy shape ``com.amazonaws.licensemanager#RegionStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class RegionStatus(TypedDict):
    status: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Status value for the region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionStatus) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionStatus:
    out: RegionStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
