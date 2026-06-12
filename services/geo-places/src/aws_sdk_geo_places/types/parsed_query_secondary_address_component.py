"""Generated from Smithy shape ``com.amazonaws.geoplaces#ParsedQuerySecondaryAddressComponent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.sensitive_string


class ParsedQuerySecondaryAddressComponent(TypedDict):
    start_index: "int"
    """<p>Start index of the parsed secondary address component in the query text.</p>"""
    end_index: "int"
    """<p>End index of the parsed secondary address component in the query text.</p>"""
    value: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>Value of the parsed secondary address component.</p>"""
    number: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>Secondary address number provided in the query.</p>"""
    designator: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>Secondary address designator provided in the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParsedQuerySecondaryAddressComponent) -> dict:
    out: dict = {}
    out["StartIndex"] = value["start_index"]
    out["EndIndex"] = value["end_index"]
    out["Value"] = value["value"]
    out["Number"] = value["number"]
    out["Designator"] = value["designator"]
    return out


def deserialize_json(data: dict) -> ParsedQuerySecondaryAddressComponent:
    out: ParsedQuerySecondaryAddressComponent = {}  # type: ignore[typeddict-item]
    if "StartIndex" in data:
        out["start_index"] = data["StartIndex"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.start_index required"
        )
    if "EndIndex" in data:
        out["end_index"] = data["EndIndex"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.end_index required"
        )
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.value required"
        )
    if "Number" in data:
        out["number"] = data["Number"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.number required"
        )
    if "Designator" in data:
        out["designator"] = data["Designator"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.designator required"
        )
    return out
