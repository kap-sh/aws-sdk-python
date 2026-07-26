"""Generated from Smithy shape ``com.amazonaws.pinpoint#DefaultPushNotificationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.action
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.map_of_list_of__string


class DefaultPushNotificationMessage(TypedDict, closed=True):
    action: NotRequired["capo_pinpoint.types.action.Action"]
    """<p>The default action to occur if a recipient taps the push notification. Valid values are:</p> <ul><li><p>OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.</p></li> <li><p>DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS and Android platforms.</p></li> <li><p>URL - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.</p></li></ul>"""
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The default body of the notification message.</p>"""
    data: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>The JSON data payload to use for the default push notification, if the notification is a silent push notification. This payload is added to the data.pinpoint.jsonBody object of the notification.</p>"""
    silent_push: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the default notification is a silent push notification, which is a push notification that doesn't display on a recipient's device. Silent push notifications can be used for cases such as updating an app's configuration or delivering messages to an in-app notification center.</p>"""
    substitutions: NotRequired[
        "capo_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>The default message variables to use in the notification message. You can override the default variables with individual address variables.</p>"""
    title: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The default title to display above the notification message on a recipient's device.</p>"""
    url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The default URL to open in a recipient's default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultPushNotificationMessage) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_pinpoint.types.action

        out["Action"] = capo_pinpoint.types.action.serialize_json(value["action"])
    if "body" in value:
        out["Body"] = value["body"]
    if "data" in value:
        import capo_pinpoint.types.map_of__string

        out["Data"] = capo_pinpoint.types.map_of__string.serialize_json(value["data"])
    if "silent_push" in value:
        out["SilentPush"] = value["silent_push"]
    if "substitutions" in value:
        import capo_pinpoint.types.map_of_list_of__string

        out["Substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.serialize_json(
                value["substitutions"]
            )
        )
    if "title" in value:
        out["Title"] = value["title"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> DefaultPushNotificationMessage:
    out: DefaultPushNotificationMessage = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_pinpoint.types.action

        out["action"] = capo_pinpoint.types.action.deserialize_json(data["Action"])
    if "Body" in data:
        out["body"] = data["Body"]
    if "Data" in data:
        import capo_pinpoint.types.map_of__string

        out["data"] = capo_pinpoint.types.map_of__string.deserialize_json(data["Data"])
    if "SilentPush" in data:
        out["silent_push"] = data["SilentPush"]
    if "Substitutions" in data:
        import capo_pinpoint.types.map_of_list_of__string

        out["substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Substitutions"]
            )
        )
    if "Title" in data:
        out["title"] = data["Title"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
