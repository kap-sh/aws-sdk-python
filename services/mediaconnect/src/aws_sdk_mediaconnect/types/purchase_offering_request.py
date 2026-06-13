"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PurchaseOfferingRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class PurchaseOfferingRequest(TypedDict):
    offering_arn: "str"
    """<p> The Amazon Resource Name (ARN) of the offering.</p>"""
    reservation_name: NotRequired["str"]
    """<p> The name that you want to use for the reservation.</p>"""
    start: NotRequired["str"]
    """<p> The date and time that you want the reservation to begin, in Coordinated Universal Time (UTC). </p> <p>You can specify any date and time between 12:00am on the first day of the current month to the current time on today's date, inclusive. Specify the start in a 24-hour notation. Use the following format: <code>YYYY-MM-DDTHH:mm:SSZ</code>, where <code>T</code> and <code>Z</code> are literal characters. For example, to specify 11:30pm on March 5, 2020, enter <code>2020-03-05T23:30:00Z</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOfferingRequest) -> dict:
    out: dict = {}
    if "reservation_name" in value:
        out["reservationName"] = value["reservation_name"]
    if "start" in value:
        out["start"] = value["start"]
    return out


def deserialize_json(data: dict) -> PurchaseOfferingRequest:
    out: PurchaseOfferingRequest = {}  # type: ignore[typeddict-item]
    if "reservationName" in data:
        out["reservation_name"] = data["reservationName"]
    if "start" in data:
        out["start"] = data["start"]
    return out
