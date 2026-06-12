"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteEmissionType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_string


class RouteEmissionType(TypedDict):
    co2_emission_class: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>The CO 2 emission classes.</p>"""
    type: "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    """<p>Type of the emission.</p> <p> <b>Valid values</b>: <code>Euro1, Euro2, Euro3, Euro4, Euro5, Euro6, EuroEev</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteEmissionType) -> dict:
    out: dict = {}
    if "co2_emission_class" in value:
        out["Co2EmissionClass"] = value["co2_emission_class"]
    out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> RouteEmissionType:
    out: RouteEmissionType = {}  # type: ignore[typeddict-item]
    if "Co2EmissionClass" in data:
        out["co2_emission_class"] = data["Co2EmissionClass"]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("RouteEmissionType.type required")
    return out
