"""Generated from Smithy shape ``com.amazonaws.securityhub#City``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class City(TypedDict, closed=True):
    city_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the city.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: City) -> dict:
    out: dict = {}
    if "city_name" in value:
        out["CityName"] = value["city_name"]
    return out


def deserialize_json(data: dict) -> City:
    out: City = {}  # type: ignore[typeddict-item]
    if "CityName" in data:
        out["city_name"] = data["CityName"]
    return out
