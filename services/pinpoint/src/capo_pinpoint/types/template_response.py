"""Generated from Smithy shape ``com.amazonaws.pinpoint#TemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.template_type


class TemplateResponse(TypedDict, closed=True):
    arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the message template. This value isn't included in a TemplateResponse object. To retrieve the ARN of a template, use the GetEmailTemplate, GetPushTemplate, GetSmsTemplate, or GetVoiceTemplate operation, depending on the type of template that you want to retrieve the ARN for.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was created.</p>"""
    default_substitutions: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The JSON object that specifies the default values that are used for message variables in the message template. This object isn't included in a TemplateResponse object. To retrieve this object for a template, use the GetEmailTemplate, GetPushTemplate, GetSmsTemplate, or GetVoiceTemplate operation, depending on the type of template that you want to retrieve the object for.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was last modified.</p>"""
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A map of key-value pairs that identifies the tags that are associated with the message template. This object isn't included in a TemplateResponse object. To retrieve this object for a template, use the GetEmailTemplate, GetPushTemplate, GetSmsTemplate, or GetVoiceTemplate operation, depending on the type of template that you want to retrieve the object for.</p>"""
    template_description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The custom description of the message template. This value isn't included in a TemplateResponse object. To retrieve the description of a template, use the GetEmailTemplate, GetPushTemplate, GetSmsTemplate, or GetVoiceTemplate operation, depending on the type of template that you want to retrieve the description for.</p>"""
    template_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the message template.</p>"""
    template_type: NotRequired["capo_pinpoint.types.template_type.TemplateType"]
    """<p>The type of channel that the message template is designed for. Possible values are: EMAIL, PUSH, SMS, INAPP, and VOICE.</p>"""
    version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier, as an integer, for the active version of the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "default_substitutions" in value:
        out["DefaultSubstitutions"] = value["default_substitutions"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "tags" in value:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.serialize_json(value["tags"])
    if "template_description" in value:
        out["TemplateDescription"] = value["template_description"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_type" in value:
        import capo_pinpoint.types.template_type

        out["TemplateType"] = capo_pinpoint.types.template_type.serialize_json(
            value["template_type"]
        )
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> TemplateResponse:
    out: TemplateResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "DefaultSubstitutions" in data:
        out["default_substitutions"] = data["DefaultSubstitutions"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "tags" in data:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.deserialize_json(data["tags"])
    if "TemplateDescription" in data:
        out["template_description"] = data["TemplateDescription"]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateType" in data:
        import capo_pinpoint.types.template_type

        out["template_type"] = capo_pinpoint.types.template_type.deserialize_json(
            data["TemplateType"]
        )
    if "Version" in data:
        out["version"] = data["Version"]
    return out
