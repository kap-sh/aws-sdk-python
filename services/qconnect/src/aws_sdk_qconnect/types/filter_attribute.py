"""Generated from Smithy shape ``com.amazonaws.qconnect#FilterAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.filter_attribute_key
    import aws_sdk_qconnect.types.json_document


class FilterAttribute(TypedDict, closed=True):
    key: "aws_sdk_qconnect.types.filter_attribute_key.FilterAttributeKey"
    """<p>The key of the filter attribute.</p>"""
    value: "aws_sdk_qconnect.types.json_document.JSONDocument"
    """<p>The value of the filter attribute.</p>"""


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
