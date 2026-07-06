"""Generated from Smithy shape ``com.amazonaws.pinpoint#SMSTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.map_of__string
    import aws_sdk_pinpoint.types.template_type


class SMSTemplateResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the message template.</p>"""
    body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message body that's used in text messages that are based on the message template.</p>"""
    creation_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was created.</p>"""
    default_substitutions: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The JSON object that specifies the default values that are used for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable.</p>"""
    last_modified_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was last modified.</p>"""
    recommender_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the recommender model that's used by the message template.</p>"""
    tags: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A string-to-string map of key-value pairs that identifies the tags that are associated with the message template. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The custom description of the message template.</p>"""
    template_name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the message template.</p>"""
    template_type: NotRequired["aws_sdk_pinpoint.types.template_type.TemplateType"]
    """<p>The type of channel that the message template is designed for. For an SMS template, this value is SMS.</p>"""
    version: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier, as an integer, for the active version of the message template, or the version of the template that you specified by using the version parameter in your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSTemplateResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "body" in value:
        out["Body"] = value["body"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "default_substitutions" in value:
        out["DefaultSubstitutions"] = value["default_substitutions"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "recommender_id" in value:
        out["RecommenderId"] = value["recommender_id"]
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


def deserialize_json(data: dict) -> SMSTemplateResponse:
    out: SMSTemplateResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Body" in data:
        out["body"] = data["Body"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "DefaultSubstitutions" in data:
        out["default_substitutions"] = data["DefaultSubstitutions"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "RecommenderId" in data:
        out["recommender_id"] = data["RecommenderId"]
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
