"""Generated from Smithy shape ``com.amazonaws.geoplaces#FoodType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.sensitive_boolean
    import aws_sdk_geo_places.types.sensitive_string


class FoodType(TypedDict, closed=True):
    localized_name: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>Localized name of the food type.</p>"""
    id: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The Food Type Id.</p>"""
    primary: NotRequired["aws_sdk_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Boolean which indicates if this food type is the primary offered by the place. For example, if a location serves fast food, but also dessert, he primary would likely be fast food.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FoodType) -> dict:
    out: dict = {}
    out["LocalizedName"] = value["localized_name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "primary" in value:
        out["Primary"] = value["primary"]
    return out


def deserialize_json(data: dict) -> FoodType:
    out: FoodType = {}  # type: ignore[typeddict-item]
    if "LocalizedName" in data:
        out["localized_name"] = data["LocalizedName"]
    else:
        raise DeserializationError("FoodType.localized_name required")
    if "Id" in data:
        out["id"] = data["Id"]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    return out
