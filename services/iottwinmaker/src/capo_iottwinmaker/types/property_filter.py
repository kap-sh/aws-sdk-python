"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.data_value
    import capo_iottwinmaker.types.string


class PropertyFilter(TypedDict, closed=True):
    property_name: NotRequired["capo_iottwinmaker.types.string.String"]
    """<p>The property name associated with this property filter.</p>"""
    operator: NotRequired["capo_iottwinmaker.types.string.String"]
    """<p>The operator associated with this property filter.</p>"""
    value: NotRequired["capo_iottwinmaker.types.data_value.DataValue"]
    """<p>The value associated with this property filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyFilter) -> dict:
    out: dict = {}
    if "property_name" in value:
        out["propertyName"] = value["property_name"]
    if "operator" in value:
        out["operator"] = value["operator"]
    if "value" in value:
        import capo_iottwinmaker.types.data_value

        out["value"] = capo_iottwinmaker.types.data_value.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> PropertyFilter:
    out: PropertyFilter = {}  # type: ignore[typeddict-item]
    if "propertyName" in data:
        out["property_name"] = data["propertyName"]
    if "operator" in data:
        out["operator"] = data["operator"]
    if "value" in data:
        import capo_iottwinmaker.types.data_value

        out["value"] = capo_iottwinmaker.types.data_value.deserialize_json(
            data["value"]
        )
    return out
