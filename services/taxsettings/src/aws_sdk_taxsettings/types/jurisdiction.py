"""Generated from Smithy shape ``com.amazonaws.taxsettings#Jurisdiction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.country_code
    import aws_sdk_taxsettings.types.state


class Jurisdiction(TypedDict, closed=True):
    state_or_region: NotRequired["aws_sdk_taxsettings.types.state.State"]
    """<p> The state, region, or province associated with the country of the jurisdiction, if applicable. </p>"""
    country_code: "aws_sdk_taxsettings.types.country_code.CountryCode"
    """<p> The country code of the jurisdiction. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Jurisdiction) -> dict:
    out: dict = {}
    if "state_or_region" in value:
        out["stateOrRegion"] = value["state_or_region"]
    out["countryCode"] = value["country_code"]
    return out


def deserialize_json(data: dict) -> Jurisdiction:
    out: Jurisdiction = {}  # type: ignore[typeddict-item]
    if "stateOrRegion" in data:
        out["state_or_region"] = data["stateOrRegion"]
    if "countryCode" in data:
        out["country_code"] = data["countryCode"]
    else:
        raise DeserializationError("Jurisdiction.country_code required")
    return out
