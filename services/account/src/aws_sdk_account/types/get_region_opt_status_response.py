"""Generated from Smithy shape ``com.amazonaws.account#GetRegionOptStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_account.types.region_name
    import aws_sdk_account.types.region_opt_status


class GetRegionOptStatusResponse(TypedDict, closed=True):
    region_name: NotRequired["aws_sdk_account.types.region_name.RegionName"]
    """<p>The Region code that was passed in.</p>"""
    region_opt_status: NotRequired[
        "aws_sdk_account.types.region_opt_status.RegionOptStatus"
    ]
    """<p>One of the potential statuses a Region can undergo (Enabled, Enabling, Disabled, Disabling, Enabled_By_Default).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRegionOptStatusResponse) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "region_opt_status" in value:
        out["RegionOptStatus"] = value["region_opt_status"]
    return out


def deserialize_json(data: dict) -> GetRegionOptStatusResponse:
    out: GetRegionOptStatusResponse = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    if "RegionOptStatus" in data:
        out["region_opt_status"] = data["RegionOptStatus"]
    return out
