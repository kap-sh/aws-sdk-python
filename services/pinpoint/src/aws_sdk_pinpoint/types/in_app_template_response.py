"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.layout
    import aws_sdk_pinpoint.types.list_of_in_app_message_content
    import aws_sdk_pinpoint.types.map_of__string
    import aws_sdk_pinpoint.types.template_type


class InAppTemplateResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The resource arn of the template.</p>"""
    content: NotRequired[
        "aws_sdk_pinpoint.types.list_of_in_app_message_content.ListOfInAppMessageContent"
    ]
    """<p>The content of the message, can include up to 5 modals. Each modal must contain a message, a header, and background color. ImageUrl and buttons are optional.</p>"""
    creation_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The creation date of the template.</p>"""
    custom_config: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>Custom config to be sent to client.</p>"""
    last_modified_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The last modified date of the template.</p>"""
    layout: NotRequired["aws_sdk_pinpoint.types.layout.Layout"]
    """<p>The layout of the message.</p>"""
    tags: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The description of the template.</p>"""
    template_name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the template.</p>"""
    template_type: NotRequired["aws_sdk_pinpoint.types.template_type.TemplateType"]
    """<p>The type of the template.</p>"""
    version: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The version id of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppTemplateResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "content" in value:
        import aws_sdk_pinpoint.types.list_of_in_app_message_content

        out["Content"] = (
            aws_sdk_pinpoint.types.list_of_in_app_message_content.serialize_json(
                value["content"]
            )
        )
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "custom_config" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["CustomConfig"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["custom_config"]
        )
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "layout" in value:
        import aws_sdk_pinpoint.types.layout

        out["Layout"] = aws_sdk_pinpoint.types.layout.serialize_json(value["layout"])
    if "tags" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["tags"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["tags"]
        )
    if "template_description" in value:
        out["TemplateDescription"] = value["template_description"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_type" in value:
        import aws_sdk_pinpoint.types.template_type

        out["TemplateType"] = aws_sdk_pinpoint.types.template_type.serialize_json(
            value["template_type"]
        )
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> InAppTemplateResponse:
    out: InAppTemplateResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Content" in data:
        import aws_sdk_pinpoint.types.list_of_in_app_message_content

        out["content"] = (
            aws_sdk_pinpoint.types.list_of_in_app_message_content.deserialize_json(
                data["Content"]
            )
        )
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "CustomConfig" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["custom_config"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["CustomConfig"]
        )
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "Layout" in data:
        import aws_sdk_pinpoint.types.layout

        out["layout"] = aws_sdk_pinpoint.types.layout.deserialize_json(data["Layout"])
    if "tags" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["tags"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["tags"]
        )
    if "TemplateDescription" in data:
        out["template_description"] = data["TemplateDescription"]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateType" in data:
        import aws_sdk_pinpoint.types.template_type

        out["template_type"] = aws_sdk_pinpoint.types.template_type.deserialize_json(
            data["TemplateType"]
        )
    if "Version" in data:
        out["version"] = data["Version"]
    return out
