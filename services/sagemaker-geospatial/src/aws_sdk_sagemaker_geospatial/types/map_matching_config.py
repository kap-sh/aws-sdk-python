"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#MapMatchingConfig``."""

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError


class MapMatchingConfig(TypedDict, closed=True):
    id_attribute_name: "str"
    """<p>The field name for the data that describes the identifier representing a collection of GPS points belonging to an individual trace.</p>"""
    y_attribute_name: "str"
    """<p>The name of the Y-attribute</p>"""
    x_attribute_name: "str"
    """<p>The name of the X-attribute</p>"""
    timestamp_attribute_name: "str"
    """<p>The name of the timestamp attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MapMatchingConfig) -> dict:
    out: dict = {}
    out["IdAttributeName"] = value["id_attribute_name"]
    out["YAttributeName"] = value["y_attribute_name"]
    out["XAttributeName"] = value["x_attribute_name"]
    out["TimestampAttributeName"] = value["timestamp_attribute_name"]
    return out


def deserialize_json(data: dict) -> MapMatchingConfig:
    out: MapMatchingConfig = {}  # type: ignore[typeddict-item]
    if "IdAttributeName" in data:
        out["id_attribute_name"] = data["IdAttributeName"]
    else:
        raise DeserializationError("MapMatchingConfig.id_attribute_name required")
    if "YAttributeName" in data:
        out["y_attribute_name"] = data["YAttributeName"]
    else:
        raise DeserializationError("MapMatchingConfig.y_attribute_name required")
    if "XAttributeName" in data:
        out["x_attribute_name"] = data["XAttributeName"]
    else:
        raise DeserializationError("MapMatchingConfig.x_attribute_name required")
    if "TimestampAttributeName" in data:
        out["timestamp_attribute_name"] = data["TimestampAttributeName"]
    else:
        raise DeserializationError(
            "MapMatchingConfig.timestamp_attribute_name required"
        )
    return out
