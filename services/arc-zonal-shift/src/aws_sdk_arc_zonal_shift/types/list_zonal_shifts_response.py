"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ListZonalShiftsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.zonal_shift_summaries


class ListZonalShiftsResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_arc_zonal_shift.types.zonal_shift_summaries.ZonalShiftSummaries"
    ]
    """<p>The items in the response list.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListZonalShiftsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_arc_zonal_shift.types.zonal_shift_summaries

        out["items"] = (
            aws_sdk_arc_zonal_shift.types.zonal_shift_summaries.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListZonalShiftsResponse:
    out: ListZonalShiftsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_arc_zonal_shift.types.zonal_shift_summaries

        out["items"] = (
            aws_sdk_arc_zonal_shift.types.zonal_shift_summaries.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
