"""Generated from Smithy shape ``com.amazonaws.pinpoint#PushNotificationTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.android_push_notification_template
    import aws_sdk_pinpoint.types.apns_push_notification_template
    import aws_sdk_pinpoint.types.default_push_notification_template
    import aws_sdk_pinpoint.types.map_of__string


class PushNotificationTemplateRequest(TypedDict):
    adm: NotRequired[
        "aws_sdk_pinpoint.types.android_push_notification_template.AndroidPushNotificationTemplate"
    ]
    """<p>The message template to use for the ADM (Amazon Device Messaging) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    apns: NotRequired[
        "aws_sdk_pinpoint.types.apns_push_notification_template.APNSPushNotificationTemplate"
    ]
    """<p>The message template to use for the APNs (Apple Push Notification service) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    baidu: NotRequired[
        "aws_sdk_pinpoint.types.android_push_notification_template.AndroidPushNotificationTemplate"
    ]
    """<p>The message template to use for the Baidu (Baidu Cloud Push) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    default: NotRequired[
        "aws_sdk_pinpoint.types.default_push_notification_template.DefaultPushNotificationTemplate"
    ]
    """<p>The default message template to use for push notification channels.</p>"""
    default_substitutions: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.</p>"""
    gcm: NotRequired[
        "aws_sdk_pinpoint.types.android_push_notification_template.AndroidPushNotificationTemplate"
    ]
    """<p>The message template to use for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    recommender_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the recommender model to use for the message template. Amazon Pinpoint uses this value to determine how to retrieve and process data from a recommender model when it sends messages that use the template, if the template contains message variables for recommendation data.</p>"""
    tags: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<note><p>As of <b>22-05-2023</b> tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html\">Tags</a> in the <i>API Reference for Amazon Pinpoint</i>, <a href=\"https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html\">resourcegroupstaggingapi</a> commands in the <i>AWS Command Line Interface Documentation</i> or <a href=\"https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html\">resourcegroupstaggingapi</a> in the <i>AWS SDK</i>.</p></note> <p>(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>A custom description of the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushNotificationTemplateRequest) -> dict:
    out: dict = {}
    if "adm" in value:
        import aws_sdk_pinpoint.types.android_push_notification_template

        out["ADM"] = (
            aws_sdk_pinpoint.types.android_push_notification_template.serialize_json(
                value["adm"]
            )
        )
    if "apns" in value:
        import aws_sdk_pinpoint.types.apns_push_notification_template

        out["APNS"] = (
            aws_sdk_pinpoint.types.apns_push_notification_template.serialize_json(
                value["apns"]
            )
        )
    if "baidu" in value:
        import aws_sdk_pinpoint.types.android_push_notification_template

        out["Baidu"] = (
            aws_sdk_pinpoint.types.android_push_notification_template.serialize_json(
                value["baidu"]
            )
        )
    if "default" in value:
        import aws_sdk_pinpoint.types.default_push_notification_template

        out["Default"] = (
            aws_sdk_pinpoint.types.default_push_notification_template.serialize_json(
                value["default"]
            )
        )
    if "default_substitutions" in value:
        out["DefaultSubstitutions"] = value["default_substitutions"]
    if "gcm" in value:
        import aws_sdk_pinpoint.types.android_push_notification_template

        out["GCM"] = (
            aws_sdk_pinpoint.types.android_push_notification_template.serialize_json(
                value["gcm"]
            )
        )
    if "recommender_id" in value:
        out["RecommenderId"] = value["recommender_id"]
    if "tags" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["tags"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["tags"]
        )
    if "template_description" in value:
        out["TemplateDescription"] = value["template_description"]
    return out


def deserialize_json(data: dict) -> PushNotificationTemplateRequest:
    out: PushNotificationTemplateRequest = {}  # type: ignore[typeddict-item]
    if "ADM" in data:
        import aws_sdk_pinpoint.types.android_push_notification_template

        out["adm"] = (
            aws_sdk_pinpoint.types.android_push_notification_template.deserialize_json(
                data["ADM"]
            )
        )
    if "APNS" in data:
        import aws_sdk_pinpoint.types.apns_push_notification_template

        out["apns"] = (
            aws_sdk_pinpoint.types.apns_push_notification_template.deserialize_json(
                data["APNS"]
            )
        )
    if "Baidu" in data:
        import aws_sdk_pinpoint.types.android_push_notification_template

        out["baidu"] = (
            aws_sdk_pinpoint.types.android_push_notification_template.deserialize_json(
                data["Baidu"]
            )
        )
    if "Default" in data:
        import aws_sdk_pinpoint.types.default_push_notification_template

        out["default"] = (
            aws_sdk_pinpoint.types.default_push_notification_template.deserialize_json(
                data["Default"]
            )
        )
    if "DefaultSubstitutions" in data:
        out["default_substitutions"] = data["DefaultSubstitutions"]
    if "GCM" in data:
        import aws_sdk_pinpoint.types.android_push_notification_template

        out["gcm"] = (
            aws_sdk_pinpoint.types.android_push_notification_template.deserialize_json(
                data["GCM"]
            )
        )
    if "RecommenderId" in data:
        out["recommender_id"] = data["RecommenderId"]
    if "tags" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["tags"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["tags"]
        )
    if "TemplateDescription" in data:
        out["template_description"] = data["TemplateDescription"]
    return out
