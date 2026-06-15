"""Generated from Smithy shape ``com.amazonaws.pinpoint#EmailTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.list_of_message_header
    import aws_sdk_pinpoint.types.map_of__string


class EmailTemplateRequest(TypedDict):
    default_substitutions: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.</p>"""
    html_part: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message body, in HTML format, to use in email messages that are based on the message template. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.</p>"""
    recommender_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the recommender model to use for the message template. Amazon Pinpoint uses this value to determine how to retrieve and process data from a recommender model when it sends messages that use the template, if the template contains message variables for recommendation data.</p>"""
    subject: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The subject line, or title, to use in email messages that are based on the message template.</p>"""
    headers: NotRequired[
        "aws_sdk_pinpoint.types.list_of_message_header.ListOfMessageHeader"
    ]
    r"""<p>The list of <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-email.html#templates-template-name-email-model-messageheader\">MessageHeaders</a> for the email. You can have up to 15 Headers.</p>"""
    tags: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    r"""<note><p>As of <b>22-05-2023</b> tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html\">Tags</a> in the <i>API Reference for Amazon Pinpoint</i>, <a href=\"https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html\">resourcegroupstaggingapi</a> commands in the <i>AWS Command Line Interface Documentation</i> or <a href=\"https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html\">resourcegroupstaggingapi</a> in the <i>AWS SDK</i>.</p></note> <p>(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>A custom description of the message template.</p>"""
    text_part: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message body, in plain text format, to use in email messages that are based on the message template. We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailTemplateRequest) -> dict:
    out: dict = {}
    if "default_substitutions" in value:
        out["DefaultSubstitutions"] = value["default_substitutions"]
    if "html_part" in value:
        out["HtmlPart"] = value["html_part"]
    if "recommender_id" in value:
        out["RecommenderId"] = value["recommender_id"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "headers" in value:
        import aws_sdk_pinpoint.types.list_of_message_header

        out["Headers"] = aws_sdk_pinpoint.types.list_of_message_header.serialize_json(
            value["headers"]
        )
    if "tags" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["tags"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["tags"]
        )
    if "template_description" in value:
        out["TemplateDescription"] = value["template_description"]
    if "text_part" in value:
        out["TextPart"] = value["text_part"]
    return out


def deserialize_json(data: dict) -> EmailTemplateRequest:
    out: EmailTemplateRequest = {}  # type: ignore[typeddict-item]
    if "DefaultSubstitutions" in data:
        out["default_substitutions"] = data["DefaultSubstitutions"]
    if "HtmlPart" in data:
        out["html_part"] = data["HtmlPart"]
    if "RecommenderId" in data:
        out["recommender_id"] = data["RecommenderId"]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    if "Headers" in data:
        import aws_sdk_pinpoint.types.list_of_message_header

        out["headers"] = aws_sdk_pinpoint.types.list_of_message_header.deserialize_json(
            data["Headers"]
        )
    if "tags" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["tags"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["tags"]
        )
    if "TemplateDescription" in data:
        out["template_description"] = data["TemplateDescription"]
    if "TextPart" in data:
        out["text_part"] = data["TextPart"]
    return out
