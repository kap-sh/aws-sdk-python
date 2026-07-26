"""Generated from Smithy shape ``com.amazonaws.appmesh#JsonFormatRef``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.json_key
    import capo_app_mesh.types.json_value


class JsonFormatRef(TypedDict, closed=True):
    key: "capo_app_mesh.types.json_key.JsonKey"
    """<p>The specified key for the JSON.</p>"""
    value: "capo_app_mesh.types.json_value.JsonValue"
    """<p>The specified value for the JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JsonFormatRef) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> JsonFormatRef:
    out: JsonFormatRef = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("JsonFormatRef.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("JsonFormatRef.value required")
    return out
