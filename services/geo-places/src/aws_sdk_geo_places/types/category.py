"""Generated from Smithy shape ``com.amazonaws.geoplaces#Category``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.sensitive_boolean
    import aws_sdk_geo_places.types.sensitive_string


class Category(TypedDict, closed=True):
    id: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The category ID.</p>"""
    name: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The category name.</p>"""
    localized_name: NotRequired[
        "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    ]
    """<p>Localized name of the category type.</p>"""
    primary: NotRequired["aws_sdk_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Boolean which indicates if this category is the primary offered by the place.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Category) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    if "localized_name" in value:
        out["LocalizedName"] = value["localized_name"]
    if "primary" in value:
        out["Primary"] = value["primary"]
    return out


def deserialize_json(data: dict) -> Category:
    out: Category = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Category.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Category.name required")
    if "LocalizedName" in data:
        out["localized_name"] = data["LocalizedName"]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    return out
