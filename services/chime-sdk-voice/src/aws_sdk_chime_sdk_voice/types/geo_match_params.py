"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GeoMatchParams``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.area_code
    import aws_sdk_chime_sdk_voice.types.country


class GeoMatchParams(TypedDict, closed=True):
    country: "aws_sdk_chime_sdk_voice.types.country.Country"
    """<p>The country.</p>"""
    area_code: "aws_sdk_chime_sdk_voice.types.area_code.AreaCode"
    """<p>The area code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoMatchParams) -> dict:
    out: dict = {}
    out["Country"] = value["country"]
    out["AreaCode"] = value["area_code"]
    return out


def deserialize_json(data: dict) -> GeoMatchParams:
    out: GeoMatchParams = {}  # type: ignore[typeddict-item]
    if "Country" in data:
        out["country"] = data["Country"]
    else:
        raise DeserializationError("GeoMatchParams.country required")
    if "AreaCode" in data:
        out["area_code"] = data["AreaCode"]
    else:
        raise DeserializationError("GeoMatchParams.area_code required")
    return out
