"""Generated from Smithy shape ``com.amazonaws.bedrock#FilterAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.filter_key
    import capo_bedrock.types.filter_value


class FilterAttribute(TypedDict, closed=True):
    key: "capo_bedrock.types.filter_key.FilterKey"
    """<p>The name of metadata attribute/field, which must match the name in your data source/document metadata.</p>"""
    value: "capo_bedrock.types.filter_value.FilterValue"
    """<p>The value of the metadata attribute/field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> FilterAttribute:
    out: FilterAttribute = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("FilterAttribute.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("FilterAttribute.value required")
    return out
