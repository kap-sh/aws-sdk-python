"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ListAutoshiftsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.autoshift_summaries


class ListAutoshiftsResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_arc_zonal_shift.types.autoshift_summaries.AutoshiftSummaries"
    ]
    """<p>The items in the response list.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutoshiftsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_arc_zonal_shift.types.autoshift_summaries

        out["items"] = aws_sdk_arc_zonal_shift.types.autoshift_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutoshiftsResponse:
    out: ListAutoshiftsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_arc_zonal_shift.types.autoshift_summaries

        out["items"] = (
            aws_sdk_arc_zonal_shift.types.autoshift_summaries.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
