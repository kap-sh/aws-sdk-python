"""Generated from Smithy shape ``com.amazonaws.pinpoint#Message``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.action


class Message(TypedDict):
    action: NotRequired["aws_sdk_pinpoint.types.action.Action"]
    """<p>The action to occur if a recipient taps the push notification. Valid values are:</p> <ul><li><p>OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.</p></li> <li><p>DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.</p></li> <li><p>URL - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.</p></li></ul>"""
    body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The body of the notification message. The maximum number of characters is 200.</p>"""
    image_icon_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL of the image to display as the push-notification icon, such as the icon for the app.</p>"""
    image_small_icon_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.</p>"""
    image_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL of an image to display in the push notification.</p>"""
    json_body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The JSON payload to use for a silent push notification.</p>"""
    media_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL of the image or video to display in the push notification.</p>"""
    raw_content: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.</p>"""
    silent_push: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the notification is a silent push notification, which is a push notification that doesn't display on a recipient's device. Silent push notifications can be used for cases such as updating an app's configuration, displaying messages in an in-app message center, or supporting phone home functionality.</p>"""
    time_to_live: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when it's sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesn't store or try to deliver the notification again.</p> <p>This value doesn't apply to messages that are sent through the Amazon Device Messaging (ADM) service.</p>"""
    title: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The title to display above the notification message on a recipient's device.</p>"""
    url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL to open in a recipient's default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_pinpoint.types.action

        out["Action"] = aws_sdk_pinpoint.types.action.serialize_json(value["action"])
    if "body" in value:
        out["Body"] = value["body"]
    if "image_icon_url" in value:
        out["ImageIconUrl"] = value["image_icon_url"]
    if "image_small_icon_url" in value:
        out["ImageSmallIconUrl"] = value["image_small_icon_url"]
    if "image_url" in value:
        out["ImageUrl"] = value["image_url"]
    if "json_body" in value:
        out["JsonBody"] = value["json_body"]
    if "media_url" in value:
        out["MediaUrl"] = value["media_url"]
    if "raw_content" in value:
        out["RawContent"] = value["raw_content"]
    if "silent_push" in value:
        out["SilentPush"] = value["silent_push"]
    if "time_to_live" in value:
        out["TimeToLive"] = value["time_to_live"]
    if "title" in value:
        out["Title"] = value["title"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_pinpoint.types.action

        out["action"] = aws_sdk_pinpoint.types.action.deserialize_json(data["Action"])
    if "Body" in data:
        out["body"] = data["Body"]
    if "ImageIconUrl" in data:
        out["image_icon_url"] = data["ImageIconUrl"]
    if "ImageSmallIconUrl" in data:
        out["image_small_icon_url"] = data["ImageSmallIconUrl"]
    if "ImageUrl" in data:
        out["image_url"] = data["ImageUrl"]
    if "JsonBody" in data:
        out["json_body"] = data["JsonBody"]
    if "MediaUrl" in data:
        out["media_url"] = data["MediaUrl"]
    if "RawContent" in data:
        out["raw_content"] = data["RawContent"]
    if "SilentPush" in data:
        out["silent_push"] = data["SilentPush"]
    if "TimeToLive" in data:
        out["time_to_live"] = data["TimeToLive"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
