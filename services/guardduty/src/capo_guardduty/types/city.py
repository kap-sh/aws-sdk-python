"""Generated from Smithy shape ``com.amazonaws.guardduty#City``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class City(TypedDict, closed=True):
    city_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The city name of the remote IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: City) -> dict:
    out: dict = {}
    if "city_name" in value:
        out["cityName"] = value["city_name"]
    return out


def deserialize_json(data: dict) -> City:
    out: City = {}  # type: ignore[typeddict-item]
    if "cityName" in data:
        out["city_name"] = data["cityName"]
    return out
