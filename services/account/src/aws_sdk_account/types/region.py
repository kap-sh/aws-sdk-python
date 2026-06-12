"""Generated from Smithy shape ``com.amazonaws.account#Region``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_account.types.region_name
    import aws_sdk_account.types.region_opt_status


class Region(TypedDict):
    region_name: NotRequired["aws_sdk_account.types.region_name.RegionName"]
    """<p>The Region code of a given Region (for example, <code>us-east-1</code>).</p>"""
    region_opt_status: NotRequired[
        "aws_sdk_account.types.region_opt_status.RegionOptStatus"
    ]
    """<p>One of potential statuses a Region can undergo (Enabled, Enabling, Disabled, Disabling, Enabled_By_Default).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Region) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "region_opt_status" in value:
        out["RegionOptStatus"] = value["region_opt_status"]
    return out


def deserialize_json(data: dict) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    if "RegionOptStatus" in data:
        out["region_opt_status"] = data["RegionOptStatus"]
    return out
