"""Generated from Smithy shape ``com.amazonaws.connect#UrlReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.reference_key
    import capo_connect.types.reference_value


class UrlReference(TypedDict, closed=True):
    name: NotRequired["capo_connect.types.reference_key.ReferenceKey"]
    """<p>Identifier of the URL reference.</p>"""
    value: NotRequired["capo_connect.types.reference_value.ReferenceValue"]
    """<p>A valid URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UrlReference) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> UrlReference:
    out: UrlReference = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
