"""Generated from Smithy shape ``com.amazonaws.securityhub#Country``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class Country(TypedDict, closed=True):
    country_code: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The 2-letter ISO 3166 country code for the country.</p>"""
    country_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the country.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Country) -> dict:
    out: dict = {}
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    if "country_name" in value:
        out["CountryName"] = value["country_name"]
    return out


def deserialize_json(data: dict) -> Country:
    out: Country = {}  # type: ignore[typeddict-item]
    if "CountryCode" in data:
        out["country_code"] = data["CountryCode"]
    if "CountryName" in data:
        out["country_name"] = data["CountryName"]
    return out
