"""Generated from Smithy shape ``com.amazonaws.sesv2#Template``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name
    import aws_sdk_sesv2.types.attachment_list
    import aws_sdk_sesv2.types.email_template_content
    import aws_sdk_sesv2.types.email_template_data
    import aws_sdk_sesv2.types.email_template_name
    import aws_sdk_sesv2.types.message_header_list


class Template(TypedDict):
    template_name: NotRequired[
        "aws_sdk_sesv2.types.email_template_name.EmailTemplateName"
    ]
    """<p>The name of the template. You will refer to this name when you send email using the <code>SendEmail</code> or <code>SendBulkEmail</code> operations. </p>"""
    template_arn: NotRequired[
        "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    template_content: NotRequired[
        "aws_sdk_sesv2.types.email_template_content.EmailTemplateContent"
    ]
    """<p>The content of the template.</p> <note> <p>Amazon SES supports only simple substitions when you send email using the <code>SendEmail</code> or <code>SendBulkEmail</code> operations and you provide the full template content in the request.</p> </note>"""
    template_data: NotRequired[
        "aws_sdk_sesv2.types.email_template_data.EmailTemplateData"
    ]
    """<p>An object that defines the values to use for message variables in the template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the value to use for that variable.</p>"""
    headers: NotRequired["aws_sdk_sesv2.types.message_header_list.MessageHeaderList"]
    """<p>The list of message headers that will be added to the email message.</p>"""
    attachments: NotRequired["aws_sdk_sesv2.types.attachment_list.AttachmentList"]
    """<p> The List of attachments to include in your email. All recipients will receive the same attachments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Template) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "template_content" in value:
        import aws_sdk_sesv2.types.email_template_content

        out["TemplateContent"] = (
            aws_sdk_sesv2.types.email_template_content.serialize_json(
                value["template_content"]
            )
        )
    if "template_data" in value:
        out["TemplateData"] = value["template_data"]
    if "headers" in value:
        import aws_sdk_sesv2.types.message_header_list

        out["Headers"] = aws_sdk_sesv2.types.message_header_list.serialize_json(
            value["headers"]
        )
    if "attachments" in value:
        import aws_sdk_sesv2.types.attachment_list

        out["Attachments"] = aws_sdk_sesv2.types.attachment_list.serialize_json(
            value["attachments"]
        )
    return out


def deserialize_json(data: dict) -> Template:
    out: Template = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "TemplateContent" in data:
        import aws_sdk_sesv2.types.email_template_content

        out["template_content"] = (
            aws_sdk_sesv2.types.email_template_content.deserialize_json(
                data["TemplateContent"]
            )
        )
    if "TemplateData" in data:
        out["template_data"] = data["TemplateData"]
    if "Headers" in data:
        import aws_sdk_sesv2.types.message_header_list

        out["headers"] = aws_sdk_sesv2.types.message_header_list.deserialize_json(
            data["Headers"]
        )
    if "Attachments" in data:
        import aws_sdk_sesv2.types.attachment_list

        out["attachments"] = aws_sdk_sesv2.types.attachment_list.deserialize_json(
            data["Attachments"]
        )
    return out
