"""Generated from Smithy shape ``com.amazonaws.sesv2#MessageInsightsFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address_filter_list
    import aws_sdk_sesv2.types.email_subject_filter_list
    import aws_sdk_sesv2.types.isp_filter_list
    import aws_sdk_sesv2.types.last_delivery_event_list
    import aws_sdk_sesv2.types.last_engagement_event_list


class MessageInsightsFilters(TypedDict):
    from_email_address: NotRequired[
        "aws_sdk_sesv2.types.email_address_filter_list.EmailAddressFilterList"
    ]
    """<p>The from address used to send the message.</p>"""
    destination: NotRequired[
        "aws_sdk_sesv2.types.email_address_filter_list.EmailAddressFilterList"
    ]
    """<p>The recipient's email address.</p>"""
    subject: NotRequired[
        "aws_sdk_sesv2.types.email_subject_filter_list.EmailSubjectFilterList"
    ]
    """<p>The subject line of the message.</p>"""
    isp: NotRequired["aws_sdk_sesv2.types.isp_filter_list.IspFilterList"]
    """<p>The recipient's ISP (e.g., <code>Gmail</code>, <code>Yahoo</code>, etc.).</p>"""
    last_delivery_event: NotRequired[
        "aws_sdk_sesv2.types.last_delivery_event_list.LastDeliveryEventList"
    ]
    """<p> The last delivery-related event for the email, where the ordering is as follows: <code>SEND</code> < <code>BOUNCE</code> < <code>DELIVERY</code> < <code>COMPLAINT</code>. </p>"""
    last_engagement_event: NotRequired[
        "aws_sdk_sesv2.types.last_engagement_event_list.LastEngagementEventList"
    ]
    """<p> The last engagement-related event for the email, where the ordering is as follows: <code>OPEN</code> < <code>CLICK</code>. </p> <p> Engagement events are only available if <a href=\"https://docs.aws.amazon.com/ses/latest/dg/vdm-settings.html\">Engagement tracking</a> is enabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageInsightsFilters) -> dict:
    out: dict = {}
    if "from_email_address" in value:
        import aws_sdk_sesv2.types.email_address_filter_list

        out["FromEmailAddress"] = (
            aws_sdk_sesv2.types.email_address_filter_list.serialize_json(
                value["from_email_address"]
            )
        )
    if "destination" in value:
        import aws_sdk_sesv2.types.email_address_filter_list

        out["Destination"] = (
            aws_sdk_sesv2.types.email_address_filter_list.serialize_json(
                value["destination"]
            )
        )
    if "subject" in value:
        import aws_sdk_sesv2.types.email_subject_filter_list

        out["Subject"] = aws_sdk_sesv2.types.email_subject_filter_list.serialize_json(
            value["subject"]
        )
    if "isp" in value:
        import aws_sdk_sesv2.types.isp_filter_list

        out["Isp"] = aws_sdk_sesv2.types.isp_filter_list.serialize_json(value["isp"])
    if "last_delivery_event" in value:
        import aws_sdk_sesv2.types.last_delivery_event_list

        out["LastDeliveryEvent"] = (
            aws_sdk_sesv2.types.last_delivery_event_list.serialize_json(
                value["last_delivery_event"]
            )
        )
    if "last_engagement_event" in value:
        import aws_sdk_sesv2.types.last_engagement_event_list

        out["LastEngagementEvent"] = (
            aws_sdk_sesv2.types.last_engagement_event_list.serialize_json(
                value["last_engagement_event"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageInsightsFilters:
    out: MessageInsightsFilters = {}  # type: ignore[typeddict-item]
    if "FromEmailAddress" in data:
        import aws_sdk_sesv2.types.email_address_filter_list

        out["from_email_address"] = (
            aws_sdk_sesv2.types.email_address_filter_list.deserialize_json(
                data["FromEmailAddress"]
            )
        )
    if "Destination" in data:
        import aws_sdk_sesv2.types.email_address_filter_list

        out["destination"] = (
            aws_sdk_sesv2.types.email_address_filter_list.deserialize_json(
                data["Destination"]
            )
        )
    if "Subject" in data:
        import aws_sdk_sesv2.types.email_subject_filter_list

        out["subject"] = aws_sdk_sesv2.types.email_subject_filter_list.deserialize_json(
            data["Subject"]
        )
    if "Isp" in data:
        import aws_sdk_sesv2.types.isp_filter_list

        out["isp"] = aws_sdk_sesv2.types.isp_filter_list.deserialize_json(data["Isp"])
    if "LastDeliveryEvent" in data:
        import aws_sdk_sesv2.types.last_delivery_event_list

        out["last_delivery_event"] = (
            aws_sdk_sesv2.types.last_delivery_event_list.deserialize_json(
                data["LastDeliveryEvent"]
            )
        )
    if "LastEngagementEvent" in data:
        import aws_sdk_sesv2.types.last_engagement_event_list

        out["last_engagement_event"] = (
            aws_sdk_sesv2.types.last_engagement_event_list.deserialize_json(
                data["LastEngagementEvent"]
            )
        )
    return out
