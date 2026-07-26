"""Generated from Smithy shape ``com.amazonaws.pinpoint#PushNotificationTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.android_push_notification_template
    import capo_pinpoint.types.apns_push_notification_template
    import capo_pinpoint.types.default_push_notification_template
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.template_type


class PushNotificationTemplateResponse(TypedDict, closed=True):
    adm: NotRequired[
        "capo_pinpoint.types.android_push_notification_template.AndroidPushNotificationTemplate"
    ]
    """<p>The message template that's used for the ADM (Amazon Device Messaging) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    apns: NotRequired[
        "capo_pinpoint.types.apns_push_notification_template.APNSPushNotificationTemplate"
    ]
    """<p>The message template that's used for the APNs (Apple Push Notification service) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the message template.</p>"""
    baidu: NotRequired[
        "capo_pinpoint.types.android_push_notification_template.AndroidPushNotificationTemplate"
    ]
    """<p>The message template that's used for the Baidu (Baidu Cloud Push) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was created.</p>"""
    default: NotRequired[
        "capo_pinpoint.types.default_push_notification_template.DefaultPushNotificationTemplate"
    ]
    """<p>The default message template that's used for push notification channels.</p>"""
    default_substitutions: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The JSON object that specifies the default values that are used for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable.</p>"""
    gcm: NotRequired[
        "capo_pinpoint.types.android_push_notification_template.AndroidPushNotificationTemplate"
    ]
    """<p>The message template that's used for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was last modified.</p>"""
    recommender_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the recommender model that's used by the message template.</p>"""
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A string-to-string map of key-value pairs that identifies the tags that are associated with the message template. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The custom description of the message template.</p>"""
    template_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the message template.</p>"""
    template_type: NotRequired["capo_pinpoint.types.template_type.TemplateType"]
    """<p>The type of channel that the message template is designed for. For a push notification template, this value is PUSH.</p>"""
    version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier, as an integer, for the active version of the message template, or the version of the template that you specified by using the version parameter in your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushNotificationTemplateResponse) -> dict:
    out: dict = {}
    if "adm" in value:
        import capo_pinpoint.types.android_push_notification_template

        out["ADM"] = (
            capo_pinpoint.types.android_push_notification_template.serialize_json(
                value["adm"]
            )
        )
    if "apns" in value:
        import capo_pinpoint.types.apns_push_notification_template

        out["APNS"] = (
            capo_pinpoint.types.apns_push_notification_template.serialize_json(
                value["apns"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "baidu" in value:
        import capo_pinpoint.types.android_push_notification_template

        out["Baidu"] = (
            capo_pinpoint.types.android_push_notification_template.serialize_json(
                value["baidu"]
            )
        )
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "default" in value:
        import capo_pinpoint.types.default_push_notification_template

        out["Default"] = (
            capo_pinpoint.types.default_push_notification_template.serialize_json(
                value["default"]
            )
        )
    if "default_substitutions" in value:
        out["DefaultSubstitutions"] = value["default_substitutions"]
    if "gcm" in value:
        import capo_pinpoint.types.android_push_notification_template

        out["GCM"] = (
            capo_pinpoint.types.android_push_notification_template.serialize_json(
                value["gcm"]
            )
        )
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "recommender_id" in value:
        out["RecommenderId"] = value["recommender_id"]
    if "tags" in value:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.serialize_json(value["tags"])
    if "template_description" in value:
        out["TemplateDescription"] = value["template_description"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_type" in value:
        import capo_pinpoint.types.template_type

        out["TemplateType"] = capo_pinpoint.types.template_type.serialize_json(
            value["template_type"]
        )
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> PushNotificationTemplateResponse:
    out: PushNotificationTemplateResponse = {}  # type: ignore[typeddict-item]
    if "ADM" in data:
        import capo_pinpoint.types.android_push_notification_template

        out["adm"] = (
            capo_pinpoint.types.android_push_notification_template.deserialize_json(
                data["ADM"]
            )
        )
    if "APNS" in data:
        import capo_pinpoint.types.apns_push_notification_template

        out["apns"] = (
            capo_pinpoint.types.apns_push_notification_template.deserialize_json(
                data["APNS"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Baidu" in data:
        import capo_pinpoint.types.android_push_notification_template

        out["baidu"] = (
            capo_pinpoint.types.android_push_notification_template.deserialize_json(
                data["Baidu"]
            )
        )
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "Default" in data:
        import capo_pinpoint.types.default_push_notification_template

        out["default"] = (
            capo_pinpoint.types.default_push_notification_template.deserialize_json(
                data["Default"]
            )
        )
    if "DefaultSubstitutions" in data:
        out["default_substitutions"] = data["DefaultSubstitutions"]
    if "GCM" in data:
        import capo_pinpoint.types.android_push_notification_template

        out["gcm"] = (
            capo_pinpoint.types.android_push_notification_template.deserialize_json(
                data["GCM"]
            )
        )
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "RecommenderId" in data:
        out["recommender_id"] = data["RecommenderId"]
    if "tags" in data:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.deserialize_json(data["tags"])
    if "TemplateDescription" in data:
        out["template_description"] = data["TemplateDescription"]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateType" in data:
        import capo_pinpoint.types.template_type

        out["template_type"] = capo_pinpoint.types.template_type.deserialize_json(
            data["TemplateType"]
        )
    if "Version" in data:
        out["version"] = data["Version"]
    return out
