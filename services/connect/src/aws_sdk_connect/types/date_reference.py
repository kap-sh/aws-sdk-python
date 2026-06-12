"""Generated from Smithy shape ``com.amazonaws.connect#DateReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.reference_key
    import aws_sdk_connect.types.reference_value


class DateReference(TypedDict):
    name: NotRequired["aws_sdk_connect.types.reference_key.ReferenceKey"]
    """<p>Identifier of the date reference.</p>"""
    value: NotRequired["aws_sdk_connect.types.reference_value.ReferenceValue"]
    """<p>A valid date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateReference) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> DateReference:
    out: DateReference = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
