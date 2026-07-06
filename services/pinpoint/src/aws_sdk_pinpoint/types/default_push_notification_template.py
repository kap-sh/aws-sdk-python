"""Generated from Smithy shape ``com.amazonaws.pinpoint#DefaultPushNotificationTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.action


class DefaultPushNotificationTemplate(TypedDict, closed=True):
    action: NotRequired["aws_sdk_pinpoint.types.action.Action"]
    """<p>The action to occur if a recipient taps a push notification that's based on the message template. Valid values are:</p> <ul><li><p>OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.</p></li> <li><p>DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS and Android platforms.</p></li> <li><p>URL - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.</p></li></ul>"""
    body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message body to use in push notifications that are based on the message template.</p>"""
    sound: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The sound to play when a recipient receives a push notification that's based on the message template. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in /res/raw/.</p> <p>For an iOS platform, this value is the key for the name of a sound file in your app's main bundle or the Library/Sounds folder in your app's data container. If the sound file can't be found or you specify default for the value, the system plays the default alert sound.</p>"""
    title: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The title to use in push notifications that are based on the message template. This title appears above the notification message on a recipient's device.</p>"""
    url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the Action property is URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultPushNotificationTemplate) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_pinpoint.types.action

        out["Action"] = aws_sdk_pinpoint.types.action.serialize_json(value["action"])
    if "body" in value:
        out["Body"] = value["body"]
    if "sound" in value:
        out["Sound"] = value["sound"]
    if "title" in value:
        out["Title"] = value["title"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> DefaultPushNotificationTemplate:
    out: DefaultPushNotificationTemplate = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_pinpoint.types.action

        out["action"] = aws_sdk_pinpoint.types.action.deserialize_json(data["Action"])
    if "Body" in data:
        out["body"] = data["Body"]
    if "Sound" in data:
        out["sound"] = data["Sound"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
