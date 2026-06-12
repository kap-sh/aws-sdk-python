"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateEmailTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_template_content
    import aws_sdk_sesv2.types.email_template_name
    import aws_sdk_sesv2.types.tag_list


class CreateEmailTemplateRequest(TypedDict):
    template_name: "aws_sdk_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the template.</p>"""
    template_content: "aws_sdk_sesv2.types.email_template_content.EmailTemplateContent"
    """<p>The content of the email template, composed of a subject line, an HTML part, and a text-only part.</p>"""
    tags: NotRequired["aws_sdk_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) to associate with the email template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailTemplateRequest) -> dict:
    out: dict = {}
    out["TemplateName"] = value["template_name"]
    import aws_sdk_sesv2.types.email_template_content

    out["TemplateContent"] = aws_sdk_sesv2.types.email_template_content.serialize_json(
        value["template_content"]
    )
    if "tags" in value:
        import aws_sdk_sesv2.types.tag_list

        out["Tags"] = aws_sdk_sesv2.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEmailTemplateRequest:
    out: CreateEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    else:
        raise DeserializationError("CreateEmailTemplateRequest.template_name required")
    if "TemplateContent" in data:
        import aws_sdk_sesv2.types.email_template_content

        out["template_content"] = (
            aws_sdk_sesv2.types.email_template_content.deserialize_json(
                data["TemplateContent"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEmailTemplateRequest.template_content required"
        )
    if "Tags" in data:
        import aws_sdk_sesv2.types.tag_list

        out["tags"] = aws_sdk_sesv2.types.tag_list.deserialize_json(data["Tags"])
    return out
