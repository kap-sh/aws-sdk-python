"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetPushTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.push_notification_template_response


class GetPushTemplateResponse(TypedDict, closed=True):
    push_notification_template_response: NotRequired[
        "aws_sdk_pinpoint.types.push_notification_template_response.PushNotificationTemplateResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetPushTemplateResponse) -> dict:
    out: dict = {}
    if "push_notification_template_response" in value:
        import aws_sdk_pinpoint.types.push_notification_template_response

        out["PushNotificationTemplateResponse"] = (
            aws_sdk_pinpoint.types.push_notification_template_response.serialize_json(
                value["push_notification_template_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPushTemplateResponse:
    out: GetPushTemplateResponse = {}  # type: ignore[typeddict-item]
    if "PushNotificationTemplateResponse" in data:
        import aws_sdk_pinpoint.types.push_notification_template_response

        out["push_notification_template_response"] = (
            aws_sdk_pinpoint.types.push_notification_template_response.deserialize_json(
                data["PushNotificationTemplateResponse"]
            )
        )
    return out
