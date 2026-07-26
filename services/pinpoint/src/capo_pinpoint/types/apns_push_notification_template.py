"""Generated from Smithy shape ``com.amazonaws.pinpoint#APNSPushNotificationTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.action


class APNSPushNotificationTemplate(TypedDict, closed=True):
    action: NotRequired["capo_pinpoint.types.action.Action"]
    """<p>The action to occur if a recipient taps a push notification that's based on the message template. Valid values are:</p> <ul><li><p>OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.</p></li> <li><p>DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS platform.</p></li> <li><p>URL - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.</p></li></ul>"""
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The message body to use in push notifications that are based on the message template.</p>"""
    media_url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The URL of an image or video to display in push notifications that are based on the message template.</p>"""
    raw_content: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The raw, JSON-formatted string to use as the payload for push notifications that are based on the message template. If specified, this value overrides all other content for the message template.</p>"""
    sound: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The key for the sound to play when the recipient receives a push notification that's based on the message template. The value for this key is the name of a sound file in your app's main bundle or the Library/Sounds folder in your app's data container. If the sound file can't be found or you specify default for the value, the system plays the default alert sound.</p>"""
    title: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The title to use in push notifications that are based on the message template. This title appears above the notification message on a recipient's device.</p>"""
    url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The URL to open in the recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the Action property is URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: APNSPushNotificationTemplate) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_pinpoint.types.action

        out["Action"] = capo_pinpoint.types.action.serialize_json(value["action"])
    if "body" in value:
        out["Body"] = value["body"]
    if "media_url" in value:
        out["MediaUrl"] = value["media_url"]
    if "raw_content" in value:
        out["RawContent"] = value["raw_content"]
    if "sound" in value:
        out["Sound"] = value["sound"]
    if "title" in value:
        out["Title"] = value["title"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> APNSPushNotificationTemplate:
    out: APNSPushNotificationTemplate = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_pinpoint.types.action

        out["action"] = capo_pinpoint.types.action.deserialize_json(data["Action"])
    if "Body" in data:
        out["body"] = data["Body"]
    if "MediaUrl" in data:
        out["media_url"] = data["MediaUrl"]
    if "RawContent" in data:
        out["raw_content"] = data["RawContent"]
    if "Sound" in data:
        out["sound"] = data["Sound"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
