"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.notification_resource_type


class NotificationResource(TypedDict, closed=True):
    type: "capo_datazone.types.notification_resource_type.NotificationResourceType"
    """<p>The type of the resource mentioned in a notification.</p>"""
    id: "str"
    """<p>The ID of the resource mentioned in a notification.</p>"""
    name: NotRequired["str"]
    """<p>The name of the resource mentioned in a notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationResource) -> dict:
    out: dict = {}
    import capo_datazone.types.notification_resource_type

    out["type"] = capo_datazone.types.notification_resource_type.serialize_json(
        value["type"]
    )
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> NotificationResource:
    out: NotificationResource = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_datazone.types.notification_resource_type

        out["type"] = capo_datazone.types.notification_resource_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("NotificationResource.type required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("NotificationResource.id required")
    if "name" in data:
        out["name"] = data["name"]
    return out
