"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CancelledChangeProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.string


class CancelledChangeProperty(TypedDict, closed=True):
    property_name: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>The name of the property whose change was cancelled.</p>"""
    cancelled_value: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>The pending value of the property that was cancelled. This would have been the eventual value of the property if the chance had not been cancelled.</p>"""
    active_value: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>The current value of the property, after the change was cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelledChangeProperty) -> dict:
    out: dict = {}
    if "property_name" in value:
        out["PropertyName"] = value["property_name"]
    if "cancelled_value" in value:
        out["CancelledValue"] = value["cancelled_value"]
    if "active_value" in value:
        out["ActiveValue"] = value["active_value"]
    return out


def deserialize_json(data: dict) -> CancelledChangeProperty:
    out: CancelledChangeProperty = {}  # type: ignore[typeddict-item]
    if "PropertyName" in data:
        out["property_name"] = data["PropertyName"]
    if "CancelledValue" in data:
        out["cancelled_value"] = data["CancelledValue"]
    if "ActiveValue" in data:
        out["active_value"] = data["ActiveValue"]
    return out
