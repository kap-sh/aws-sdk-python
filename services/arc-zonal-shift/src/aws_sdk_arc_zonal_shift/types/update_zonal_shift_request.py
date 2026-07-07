"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdateZonalShiftRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.expires_in
    import aws_sdk_arc_zonal_shift.types.zonal_shift_comment
    import aws_sdk_arc_zonal_shift.types.zonal_shift_id


class UpdateZonalShiftRequest(TypedDict, closed=True):
    zonal_shift_id: "aws_sdk_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId"
    """<p>The identifier of a zonal shift.</p>"""
    comment: NotRequired[
        "aws_sdk_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
    ]
    """<p>A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.</p>"""
    expires_in: NotRequired["aws_sdk_arc_zonal_shift.types.expires_in.ExpiresIn"]
    """<p>The length of time that you want a zonal shift to be active, which ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).</p> <p>If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you're ready to restore traffic to the Availability Zone.</p> <p>To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:</p> <ul> <li> <p> <b>A lowercase letter m:</b> To specify that the value is in minutes.</p> </li> <li> <p> <b>A lowercase letter h:</b> To specify that the value is in hours.</p> </li> </ul> <p>For example: <code>20h</code> means the zonal shift expires in 20 hours. <code>120m</code> means the zonal shift expires in 120 minutes (2 hours).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateZonalShiftRequest) -> dict:
    out: dict = {}
    if "comment" in value:
        out["comment"] = value["comment"]
    if "expires_in" in value:
        out["expiresIn"] = value["expires_in"]
    return out


def deserialize_json(data: dict) -> UpdateZonalShiftRequest:
    out: UpdateZonalShiftRequest = {}  # type: ignore[typeddict-item]
    if "comment" in data:
        out["comment"] = data["comment"]
    if "expiresIn" in data:
        out["expires_in"] = data["expiresIn"]
    return out
