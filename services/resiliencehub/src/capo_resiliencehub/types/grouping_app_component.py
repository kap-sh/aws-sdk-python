"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingAppComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.entity_name255
    import capo_resiliencehub.types.string255


class GroupingAppComponent(TypedDict, closed=True):
    app_component_id: "capo_resiliencehub.types.entity_name255.EntityName255"
    """<p>Indicates the identifier of an AppComponent.</p>"""
    app_component_type: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates the type of an AppComponent.</p>"""
    app_component_name: "capo_resiliencehub.types.entity_name255.EntityName255"
    """<p>Indicates the name of an AppComponent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupingAppComponent) -> dict:
    out: dict = {}
    out["appComponentId"] = value["app_component_id"]
    out["appComponentType"] = value["app_component_type"]
    out["appComponentName"] = value["app_component_name"]
    return out


def deserialize_json(data: dict) -> GroupingAppComponent:
    out: GroupingAppComponent = {}  # type: ignore[typeddict-item]
    if "appComponentId" in data:
        out["app_component_id"] = data["appComponentId"]
    else:
        raise DeserializationError("GroupingAppComponent.app_component_id required")
    if "appComponentType" in data:
        out["app_component_type"] = data["appComponentType"]
    else:
        raise DeserializationError("GroupingAppComponent.app_component_type required")
    if "appComponentName" in data:
        out["app_component_name"] = data["appComponentName"]
    else:
        raise DeserializationError("GroupingAppComponent.app_component_name required")
    return out
