"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailTemplateMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_template_name
    import aws_sdk_sesv2.types.timestamp


class EmailTemplateMetadata(TypedDict):
    template_name: NotRequired[
        "aws_sdk_sesv2.types.email_template_name.EmailTemplateName"
    ]
    """<p>The name of the template.</p>"""
    created_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The time and date the template was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailTemplateMetadata) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "created_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["CreatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> EmailTemplateMetadata:
    out: EmailTemplateMetadata = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "CreatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["created_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    return out
