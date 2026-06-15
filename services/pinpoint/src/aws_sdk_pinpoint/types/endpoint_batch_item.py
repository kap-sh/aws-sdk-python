"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointBatchItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.channel_type
    import aws_sdk_pinpoint.types.endpoint_demographic
    import aws_sdk_pinpoint.types.endpoint_location
    import aws_sdk_pinpoint.types.endpoint_user
    import aws_sdk_pinpoint.types.map_of__double
    import aws_sdk_pinpoint.types.map_of_list_of__string


class EndpointBatchItem(TypedDict):
    address: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The destination address for messages or push notifications that you send to the endpoint. The address varies by channel. For a push-notification channel, use the token provided by the push notification service, such as an Apple Push Notification service (APNs) device token or a Firebase Cloud Messaging (FCM) registration token. For the SMS channel, use a phone number in E.164 format, such as +12065550100. For the email channel, use an email address.</p>"""
    attributes: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    r"""<p>One or more custom attributes that describe the endpoint by associating a name with an array of values. For example, the value of a custom attribute named Interests might be: [\"Science\", \"Music\", \"Travel\"]. You can use these attributes as filter criteria when you create segments. Attribute names are case sensitive.</p> <p>An attribute name can contain up to 50 characters. An attribute value can contain up to 100 characters. When you define the name of a custom attribute, avoid using the following characters: number sign (#), colon (:), question mark (?), backslash (\), and slash (/). The Amazon Pinpoint console can't display attribute names that contain these characters. This restriction doesn't apply to attribute values.</p>"""
    channel_type: NotRequired["aws_sdk_pinpoint.types.channel_type.ChannelType"]
    """<p>The channel to use when sending messages or push notifications to the endpoint.</p>"""
    demographic: NotRequired[
        "aws_sdk_pinpoint.types.endpoint_demographic.EndpointDemographic"
    ]
    """<p>The demographic information for the endpoint, such as the time zone and platform.</p>"""
    effective_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the endpoint was created or updated.</p>"""
    endpoint_status: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>Specifies whether to send messages or push notifications to the endpoint. Valid values are: ACTIVE, messages are sent to the endpoint; and, INACTIVE, messages aren’t sent to the endpoint.</p> <p>Amazon Pinpoint automatically sets this value to ACTIVE when you create an endpoint or update an existing endpoint. Amazon Pinpoint automatically sets this value to INACTIVE if you update another endpoint that has the same address specified by the Address property.</p>"""
    id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the endpoint in the context of the batch.</p>"""
    location: NotRequired["aws_sdk_pinpoint.types.endpoint_location.EndpointLocation"]
    """<p>The geographic information for the endpoint.</p>"""
    metrics: NotRequired["aws_sdk_pinpoint.types.map_of__double.MapOf__double"]
    """<p>One or more custom metrics that your app reports to Amazon Pinpoint for the endpoint.</p>"""
    opt_out: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>Specifies whether the user who's associated with the endpoint has opted out of receiving messages and push notifications from you. Possible values are: ALL, the user has opted out and doesn't want to receive any messages or push notifications; and, NONE, the user hasn't opted out and wants to receive all messages and push notifications.</p>"""
    request_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the request to create or update the endpoint.</p>"""
    user: NotRequired["aws_sdk_pinpoint.types.endpoint_user.EndpointUser"]
    """<p>One or more custom attributes that describe the user who's associated with the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointBatchItem) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    if "attributes" in value:
        import aws_sdk_pinpoint.types.map_of_list_of__string

        out["Attributes"] = (
            aws_sdk_pinpoint.types.map_of_list_of__string.serialize_json(
                value["attributes"]
            )
        )
    if "channel_type" in value:
        import aws_sdk_pinpoint.types.channel_type

        out["ChannelType"] = aws_sdk_pinpoint.types.channel_type.serialize_json(
            value["channel_type"]
        )
    if "demographic" in value:
        import aws_sdk_pinpoint.types.endpoint_demographic

        out["Demographic"] = aws_sdk_pinpoint.types.endpoint_demographic.serialize_json(
            value["demographic"]
        )
    if "effective_date" in value:
        out["EffectiveDate"] = value["effective_date"]
    if "endpoint_status" in value:
        out["EndpointStatus"] = value["endpoint_status"]
    if "id" in value:
        out["Id"] = value["id"]
    if "location" in value:
        import aws_sdk_pinpoint.types.endpoint_location

        out["Location"] = aws_sdk_pinpoint.types.endpoint_location.serialize_json(
            value["location"]
        )
    if "metrics" in value:
        import aws_sdk_pinpoint.types.map_of__double

        out["Metrics"] = aws_sdk_pinpoint.types.map_of__double.serialize_json(
            value["metrics"]
        )
    if "opt_out" in value:
        out["OptOut"] = value["opt_out"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "user" in value:
        import aws_sdk_pinpoint.types.endpoint_user

        out["User"] = aws_sdk_pinpoint.types.endpoint_user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> EndpointBatchItem:
    out: EndpointBatchItem = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "Attributes" in data:
        import aws_sdk_pinpoint.types.map_of_list_of__string

        out["attributes"] = (
            aws_sdk_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Attributes"]
            )
        )
    if "ChannelType" in data:
        import aws_sdk_pinpoint.types.channel_type

        out["channel_type"] = aws_sdk_pinpoint.types.channel_type.deserialize_json(
            data["ChannelType"]
        )
    if "Demographic" in data:
        import aws_sdk_pinpoint.types.endpoint_demographic

        out["demographic"] = (
            aws_sdk_pinpoint.types.endpoint_demographic.deserialize_json(
                data["Demographic"]
            )
        )
    if "EffectiveDate" in data:
        out["effective_date"] = data["EffectiveDate"]
    if "EndpointStatus" in data:
        out["endpoint_status"] = data["EndpointStatus"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Location" in data:
        import aws_sdk_pinpoint.types.endpoint_location

        out["location"] = aws_sdk_pinpoint.types.endpoint_location.deserialize_json(
            data["Location"]
        )
    if "Metrics" in data:
        import aws_sdk_pinpoint.types.map_of__double

        out["metrics"] = aws_sdk_pinpoint.types.map_of__double.deserialize_json(
            data["Metrics"]
        )
    if "OptOut" in data:
        out["opt_out"] = data["OptOut"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "User" in data:
        import aws_sdk_pinpoint.types.endpoint_user

        out["user"] = aws_sdk_pinpoint.types.endpoint_user.deserialize_json(
            data["User"]
        )
    return out
