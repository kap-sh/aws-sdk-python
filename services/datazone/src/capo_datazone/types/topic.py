"""Generated from Smithy shape ``com.amazonaws.datazone#Topic``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.notification_resource
    import capo_datazone.types.notification_role


class Topic(TypedDict, closed=True):
    subject: "str"
    """<p>The subject of the resource mentioned in a notification.</p>"""
    resource: "capo_datazone.types.notification_resource.NotificationResource"
    role: "capo_datazone.types.notification_role.NotificationRole"
    """<p>The role of the resource mentioned in a notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Topic) -> dict:
    out: dict = {}
    out["subject"] = value["subject"]
    import capo_datazone.types.notification_resource

    out["resource"] = capo_datazone.types.notification_resource.serialize_json(
        value["resource"]
    )
    import capo_datazone.types.notification_role

    out["role"] = capo_datazone.types.notification_role.serialize_json(value["role"])
    return out


def deserialize_json(data: dict) -> Topic:
    out: Topic = {}  # type: ignore[typeddict-item]
    if "subject" in data:
        out["subject"] = data["subject"]
    else:
        raise DeserializationError("Topic.subject required")
    if "resource" in data:
        import capo_datazone.types.notification_resource

        out["resource"] = capo_datazone.types.notification_resource.deserialize_json(
            data["resource"]
        )
    else:
        raise DeserializationError("Topic.resource required")
    if "role" in data:
        import capo_datazone.types.notification_role

        out["role"] = capo_datazone.types.notification_role.deserialize_json(
            data["role"]
        )
    else:
        raise DeserializationError("Topic.role required")
    return out
