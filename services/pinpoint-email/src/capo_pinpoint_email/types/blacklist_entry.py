"""Generated from Smithy shape ``com.amazonaws.pinpointemail#BlacklistEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.blacklisting_description
    import capo_pinpoint_email.types.rbl_name
    import capo_pinpoint_email.types.timestamp


class BlacklistEntry(TypedDict, closed=True):
    rbl_name: NotRequired["capo_pinpoint_email.types.rbl_name.RblName"]
    """<p>The name of the blacklist that the IP address appears on.</p>"""
    listing_time: NotRequired["capo_pinpoint_email.types.timestamp.Timestamp"]
    """<p>The time when the blacklisting event occurred, shown in Unix time format.</p>"""
    description: NotRequired[
        "capo_pinpoint_email.types.blacklisting_description.BlacklistingDescription"
    ]
    """<p>Additional information about the blacklisting event, as provided by the blacklist maintainer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlacklistEntry) -> dict:
    out: dict = {}
    if "rbl_name" in value:
        out["RblName"] = value["rbl_name"]
    if "listing_time" in value:
        import capo_pinpoint_email.types.timestamp

        out["ListingTime"] = capo_pinpoint_email.types.timestamp.serialize_json(
            value["listing_time"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BlacklistEntry:
    out: BlacklistEntry = {}  # type: ignore[typeddict-item]
    if "RblName" in data:
        out["rbl_name"] = data["RblName"]
    if "ListingTime" in data:
        import capo_pinpoint_email.types.timestamp

        out["listing_time"] = capo_pinpoint_email.types.timestamp.deserialize_json(
            data["ListingTime"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
