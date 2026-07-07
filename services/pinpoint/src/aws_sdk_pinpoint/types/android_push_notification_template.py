"""Generated from Smithy shape ``com.amazonaws.pinpoint#AndroidPushNotificationTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.action


class AndroidPushNotificationTemplate(TypedDict, closed=True):
    action: NotRequired["aws_sdk_pinpoint.types.action.Action"]
    """<p>The action to occur if a recipient taps a push notification that's based on the message template. Valid values are:</p> <ul><li><p>OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.</p></li> <li><p>DEEP_LINK - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.</p></li> <li><p>URL - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.</p></li></ul>"""
    body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message body to use in a push notification that's based on the message template.</p>"""
    image_icon_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL of the large icon image to display in the content view of a push notification that's based on the message template.</p>"""
    image_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL of an image to display in a push notification that's based on the message template.</p>"""
    raw_content: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The raw, JSON-formatted string to use as the payload for a push notification that's based on the message template. If specified, this value overrides all other content for the message template.</p>"""
    small_image_icon_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL of the small icon image to display in the status bar and the content view of a push notification that's based on the message template.</p>"""
    sound: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The sound to play when a recipient receives a push notification that's based on the message template. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in /res/raw/.</p>"""
    title: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The title to use in a push notification that's based on the message template. This title appears above the notification message on a recipient's device.</p>"""
    url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the Action property is URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AndroidPushNotificationTemplate) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_pinpoint.types.action

        out["Action"] = aws_sdk_pinpoint.types.action.serialize_json(value["action"])
    if "body" in value:
        out["Body"] = value["body"]
    if "image_icon_url" in value:
        out["ImageIconUrl"] = value["image_icon_url"]
    if "image_url" in value:
        out["ImageUrl"] = value["image_url"]
    if "raw_content" in value:
        out["RawContent"] = value["raw_content"]
    if "small_image_icon_url" in value:
        out["SmallImageIconUrl"] = value["small_image_icon_url"]
    if "sound" in value:
        out["Sound"] = value["sound"]
    if "title" in value:
        out["Title"] = value["title"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> AndroidPushNotificationTemplate:
    out: AndroidPushNotificationTemplate = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_pinpoint.types.action

        out["action"] = aws_sdk_pinpoint.types.action.deserialize_json(data["Action"])
    if "Body" in data:
        out["body"] = data["Body"]
    if "ImageIconUrl" in data:
        out["image_icon_url"] = data["ImageIconUrl"]
    if "ImageUrl" in data:
        out["image_url"] = data["ImageUrl"]
    if "RawContent" in data:
        out["raw_content"] = data["RawContent"]
    if "SmallImageIconUrl" in data:
        out["small_image_icon_url"] = data["SmallImageIconUrl"]
    if "Sound" in data:
        out["sound"] = data["Sound"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
