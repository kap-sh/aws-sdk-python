"""Generated from Smithy shape ``com.amazonaws.guardduty#Country``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class Country(TypedDict, closed=True):
    country_code: NotRequired["capo_guardduty.types.string.String"]
    """<p>The country code of the remote IP address.</p>"""
    country_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The country name of the remote IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Country) -> dict:
    out: dict = {}
    if "country_code" in value:
        out["countryCode"] = value["country_code"]
    if "country_name" in value:
        out["countryName"] = value["country_name"]
    return out


def deserialize_json(data: dict) -> Country:
    out: Country = {}  # type: ignore[typeddict-item]
    if "countryCode" in data:
        out["country_code"] = data["countryCode"]
    if "countryName" in data:
        out["country_name"] = data["countryName"]
    return out
