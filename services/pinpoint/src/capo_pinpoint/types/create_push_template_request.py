"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreatePushTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.push_notification_template_request


class CreatePushTemplateRequest(TypedDict, closed=True):
    push_notification_template_request: NotRequired[
        "capo_pinpoint.types.push_notification_template_request.PushNotificationTemplateRequest"
    ]
    template_name: "capo_pinpoint.types.__string.__string"
    """<p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePushTemplateRequest) -> dict:
    out: dict = {}
    if "push_notification_template_request" in value:
        import capo_pinpoint.types.push_notification_template_request

        out["PushNotificationTemplateRequest"] = (
            capo_pinpoint.types.push_notification_template_request.serialize_json(
                value["push_notification_template_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreatePushTemplateRequest:
    out: CreatePushTemplateRequest = {}  # type: ignore[typeddict-item]
    if "PushNotificationTemplateRequest" in data:
        import capo_pinpoint.types.push_notification_template_request

        out["push_notification_template_request"] = (
            capo_pinpoint.types.push_notification_template_request.deserialize_json(
                data["PushNotificationTemplateRequest"]
            )
        )
    return out
