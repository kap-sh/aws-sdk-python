"""Generated from Smithy shape ``com.amazonaws.taxsettings#Authority``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.country_code
    import capo_taxsettings.types.state


class Authority(TypedDict, closed=True):
    country: "capo_taxsettings.types.country_code.CountryCode"
    """<p> The country code for the country that the address is in. </p>"""
    state: NotRequired["capo_taxsettings.types.state.State"]
    """<p> The state that the address is located. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Authority) -> dict:
    out: dict = {}
    out["country"] = value["country"]
    if "state" in value:
        out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> Authority:
    out: Authority = {}  # type: ignore[typeddict-item]
    if "country" in data:
        out["country"] = data["country"]
    else:
        raise DeserializationError("Authority.country required")
    if "state" in data:
        out["state"] = data["state"]
    return out
