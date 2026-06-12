"""Generated from Smithy shape ``com.amazonaws.geoplaces#Country``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.country_code2
    import aws_sdk_geo_places.types.country_code3
    import aws_sdk_geo_places.types.sensitive_string


class Country(TypedDict):
    code2: NotRequired["aws_sdk_geo_places.types.country_code2.CountryCode2"]
    """<p>Country, represented by its alpha 2-character code. </p>"""
    code3: NotRequired["aws_sdk_geo_places.types.country_code3.CountryCode3"]
    """<p>Country, represented by its alpha t-character code. </p>"""
    name: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Name of the country.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Country) -> dict:
    out: dict = {}
    if "code2" in value:
        out["Code2"] = value["code2"]
    if "code3" in value:
        out["Code3"] = value["code3"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Country:
    out: Country = {}  # type: ignore[typeddict-item]
    if "Code2" in data:
        out["code2"] = data["Code2"]
    if "Code3" in data:
        out["code3"] = data["Code3"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
