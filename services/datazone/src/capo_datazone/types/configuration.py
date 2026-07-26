"""Generated from Smithy shape ``com.amazonaws.datazone#Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.property_map


class Configuration(TypedDict, closed=True):
    classification: NotRequired["str"]
    """<p>The classification of the connection configuration.</p>"""
    properties: NotRequired["capo_datazone.types.property_map.PropertyMap"]
    """<p>The properties of the connection configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    out: dict = {}
    if "classification" in value:
        out["classification"] = value["classification"]
    if "properties" in value:
        import capo_datazone.types.property_map

        out["properties"] = capo_datazone.types.property_map.serialize_json(
            value["properties"]
        )
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if "classification" in data:
        out["classification"] = data["classification"]
    if "properties" in data:
        import capo_datazone.types.property_map

        out["properties"] = capo_datazone.types.property_map.deserialize_json(
            data["properties"]
        )
    return out
