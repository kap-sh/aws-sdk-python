"""Generated from Smithy shape ``com.amazonaws.datazone#ResourceTagParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.tag_key
    import capo_datazone.types.tag_value


class ResourceTagParameter(TypedDict, closed=True):
    key: "capo_datazone.types.tag_key.TagKey"
    """<p>The key of the resource tag parameter of the project profile.</p>"""
    value: "capo_datazone.types.tag_value.TagValue"
    """<p>The value of the resource tag parameter key of the project profile.</p>"""
    is_value_editable: "bool"
    """<p>Specifies whether the value of the resource tag parameter of the project profile is editable at the project level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTagParameter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    out["isValueEditable"] = value["is_value_editable"]
    return out


def deserialize_json(data: dict) -> ResourceTagParameter:
    out: ResourceTagParameter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ResourceTagParameter.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("ResourceTagParameter.value required")
    if "isValueEditable" in data:
        out["is_value_editable"] = data["isValueEditable"]
    else:
        raise DeserializationError("ResourceTagParameter.is_value_editable required")
    return out
