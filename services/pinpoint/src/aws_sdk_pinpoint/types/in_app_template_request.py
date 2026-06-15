"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.layout
    import aws_sdk_pinpoint.types.list_of_in_app_message_content
    import aws_sdk_pinpoint.types.map_of__string


class InAppTemplateRequest(TypedDict):
    content: NotRequired[
        "aws_sdk_pinpoint.types.list_of_in_app_message_content.ListOfInAppMessageContent"
    ]
    """<p>The content of the message, can include up to 5 modals. Each modal must contain a message, a header, and background color. ImageUrl and buttons are optional.</p>"""
    custom_config: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>Custom config to be sent to client.</p>"""
    layout: NotRequired["aws_sdk_pinpoint.types.layout.Layout"]
    """<p>The layout of the message.</p>"""
    tags: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    r"""<note><p>As of <b>22-05-2023</b> tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html\">Tags</a> in the <i>API Reference for Amazon Pinpoint</i>, <a href=\"https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html\">resourcegroupstaggingapi</a> commands in the <i>AWS Command Line Interface Documentation</i> or <a href=\"https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html\">resourcegroupstaggingapi</a> in the <i>AWS SDK</i>.</p></note> <p>(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The description of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppTemplateRequest) -> dict:
    out: dict = {}
    if "content" in value:
        import aws_sdk_pinpoint.types.list_of_in_app_message_content

        out["Content"] = (
            aws_sdk_pinpoint.types.list_of_in_app_message_content.serialize_json(
                value["content"]
            )
        )
    if "custom_config" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["CustomConfig"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["custom_config"]
        )
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
    return out


def deserialize_json(data: dict) -> InAppTemplateRequest:
    out: InAppTemplateRequest = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        import aws_sdk_pinpoint.types.list_of_in_app_message_content

        out["content"] = (
            aws_sdk_pinpoint.types.list_of_in_app_message_content.deserialize_json(
                data["Content"]
            )
        )
    if "CustomConfig" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["custom_config"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["CustomConfig"]
        )
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
    return out
