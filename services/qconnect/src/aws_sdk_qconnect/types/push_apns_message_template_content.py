"""Generated from Smithy shape ``com.amazonaws.qconnect#PushAPNSMessageTemplateContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_body_content_provider
    import aws_sdk_qconnect.types.non_empty_unlimited_string
    import aws_sdk_qconnect.types.push_message_action


class PushAPNSMessageTemplateContent(TypedDict, closed=True):
    title: NotRequired[
        "aws_sdk_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The title to use in a push notification that's based on the message template. This title appears above the notification message on a recipient's device.</p>"""
    body: NotRequired[
        "aws_sdk_qconnect.types.message_template_body_content_provider.MessageTemplateBodyContentProvider"
    ]
    """<p>The message body to use in a push notification that is based on the message template.</p>"""
    action: NotRequired["aws_sdk_qconnect.types.push_message_action.PushMessageAction"]
    """<p>The action to occur if a recipient taps a push notification that is based on the message template. Valid values are:</p> <ul> <li> <p> <code>OPEN_APP</code> - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.</p> </li> <li> <p> <code>DEEP_LINK</code> - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the iOS platform.</p> </li> <li> <p> <code>URL</code> - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.</p> </li> </ul>"""
    sound: NotRequired[
        "aws_sdk_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The key for the sound to play when the recipient receives a push notification that's based on the message template. The value for this key is the name of a sound file in your app's main bundle or the <code>Library/Sounds</code> folder in your app's data container. If the sound file can't be found or you specify <code>default</code> for the value, the system plays the default alert sound.</p>"""
    url: NotRequired[
        "aws_sdk_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the <code>action</code> property is <code>URL</code>.</p>"""
    media_url: NotRequired[
        "aws_sdk_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The URL of an image or video to display in push notifications that are based on the message template.</p>"""
    raw_content: NotRequired[
        "aws_sdk_qconnect.types.message_template_body_content_provider.MessageTemplateBodyContentProvider"
    ]
    """<p>The raw, JSON-formatted string to use as the payload for a push notification that's based on the message template. If specified, this value overrides all other content for the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushAPNSMessageTemplateContent) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "body" in value:
        import aws_sdk_qconnect.types.message_template_body_content_provider

        out["body"] = (
            aws_sdk_qconnect.types.message_template_body_content_provider.serialize_json(
                value["body"]
            )
        )
    if "action" in value:
        out["action"] = value["action"]
    if "sound" in value:
        out["sound"] = value["sound"]
    if "url" in value:
        out["url"] = value["url"]
    if "media_url" in value:
        out["mediaUrl"] = value["media_url"]
    if "raw_content" in value:
        import aws_sdk_qconnect.types.message_template_body_content_provider

        out["rawContent"] = (
            aws_sdk_qconnect.types.message_template_body_content_provider.serialize_json(
                value["raw_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> PushAPNSMessageTemplateContent:
    out: PushAPNSMessageTemplateContent = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    if "body" in data:
        import aws_sdk_qconnect.types.message_template_body_content_provider

        out["body"] = (
            aws_sdk_qconnect.types.message_template_body_content_provider.deserialize_json(
                data["body"]
            )
        )
    if "action" in data:
        out["action"] = data["action"]
    if "sound" in data:
        out["sound"] = data["sound"]
    if "url" in data:
        out["url"] = data["url"]
    if "mediaUrl" in data:
        out["media_url"] = data["mediaUrl"]
    if "rawContent" in data:
        import aws_sdk_qconnect.types.message_template_body_content_provider

        out["raw_content"] = (
            aws_sdk_qconnect.types.message_template_body_content_provider.deserialize_json(
                data["rawContent"]
            )
        )
    return out
