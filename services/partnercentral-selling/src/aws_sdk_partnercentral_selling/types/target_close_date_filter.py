"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TargetCloseDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.date


class TargetCloseDateFilter(TypedDict, closed=True):
    after_target_close_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.date.Date"
    ]
    """<p>Filters opportunities with a target close date after this date. Use the <code>YYYY-MM-DD</code> format.</p>"""
    before_target_close_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.date.Date"
    ]
    """<p>Filters opportunities with a target close date before this date. Use the <code>YYYY-MM-DD</code> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TargetCloseDateFilter) -> dict:
    out: dict = {}
    if "after_target_close_date" in value:
        out["AfterTargetCloseDate"] = value["after_target_close_date"]
    if "before_target_close_date" in value:
        out["BeforeTargetCloseDate"] = value["before_target_close_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TargetCloseDateFilter:
    out: TargetCloseDateFilter = {}  # type: ignore[typeddict-item]
    if "AfterTargetCloseDate" in data:
        out["after_target_close_date"] = data["AfterTargetCloseDate"]
    if "BeforeTargetCloseDate" in data:
        out["before_target_close_date"] = data["BeforeTargetCloseDate"]
    return out
