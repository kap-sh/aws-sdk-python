"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#IncludedProperty``."""

from typing_extensions import TypedDict

from capo_resource_explorer_2.errors import DeserializationError


class IncludedProperty(TypedDict, closed=True):
    name: "str"
    """<p>The name of the property that is included in this view.</p> <p>You can specify the following property names for this field:</p> <ul> <li> <p> <code>tags</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncludedProperty) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> IncludedProperty:
    out: IncludedProperty = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("IncludedProperty.name required")
    return out
