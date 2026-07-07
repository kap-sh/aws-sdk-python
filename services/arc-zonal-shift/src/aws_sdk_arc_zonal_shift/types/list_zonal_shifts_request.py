"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ListZonalShiftsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.max_results
    import aws_sdk_arc_zonal_shift.types.resource_identifier
    import aws_sdk_arc_zonal_shift.types.zonal_shift_status


class ListZonalShiftsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""
    status: NotRequired[
        "aws_sdk_arc_zonal_shift.types.zonal_shift_status.ZonalShiftStatus"
    ]
    """<p>A status for a zonal shift.</p> <p>The <code>Status</code> for a zonal shift can have one of the following values:</p> <ul> <li> <p> <b>ACTIVE</b>: The zonal shift has been started and is active.</p> </li> <li> <p> <b>EXPIRED</b>: The zonal shift has expired (the expiry time was exceeded).</p> </li> <li> <p> <b>CANCELED</b>: The zonal shift was canceled.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_arc_zonal_shift.types.max_results.MaxResults"]
    """<p>The number of objects that you want to return with this call.</p>"""
    resource_identifier: NotRequired[
        "aws_sdk_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>The identifier for the resource that you want to list zonal shifts for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListZonalShiftsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListZonalShiftsRequest:
    out: ListZonalShiftsRequest = {}  # type: ignore[typeddict-item]
    return out
