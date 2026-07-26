"""Generated from Smithy shape ``com.amazonaws.geoplaces#SecondaryAddressComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class SecondaryAddressComponent(TypedDict, closed=True):
    number: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>Number that uniquely identifies a secondary address.</p>"""
    designator: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The designator of the secondary address component.</p> <p>Example: <code>Apt</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecondaryAddressComponent) -> dict:
    out: dict = {}
    out["Number"] = value["number"]
    if "designator" in value:
        out["Designator"] = value["designator"]
    return out


def deserialize_json(data: dict) -> SecondaryAddressComponent:
    out: SecondaryAddressComponent = {}  # type: ignore[typeddict-item]
    if "Number" in data:
        out["number"] = data["Number"]
    else:
        raise DeserializationError("SecondaryAddressComponent.number required")
    if "Designator" in data:
        out["designator"] = data["Designator"]
    return out
