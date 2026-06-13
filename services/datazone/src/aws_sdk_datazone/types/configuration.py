"""Generated from Smithy shape ``com.amazonaws.datazone#Configuration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.property_map


class Configuration(TypedDict):
    classification: NotRequired["str"]
    """<p>The classification of the connection configuration.</p>"""
    properties: NotRequired["aws_sdk_datazone.types.property_map.PropertyMap"]
    """<p>The properties of the connection configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    out: dict = {}
    if "classification" in value:
        out["classification"] = value["classification"]
    if "properties" in value:
        import aws_sdk_datazone.types.property_map

        out["properties"] = aws_sdk_datazone.types.property_map.serialize_json(
            value["properties"]
        )
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if "classification" in data:
        out["classification"] = data["classification"]
    if "properties" in data:
        import aws_sdk_datazone.types.property_map

        out["properties"] = aws_sdk_datazone.types.property_map.deserialize_json(
            data["properties"]
        )
    return out
