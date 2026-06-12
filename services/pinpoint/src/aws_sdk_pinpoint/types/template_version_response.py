"""Generated from Smithy shape ``com.amazonaws.pinpoint#TemplateVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class TemplateVersionResponse(TypedDict):
    creation_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the version of the message template was created.</p>"""
    default_substitutions: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>A JSON object that specifies the default values that are used for message variables in the version of the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable.</p>"""
    last_modified_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the version of the message template was last modified.</p>"""
    template_description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The custom description of the version of the message template.</p>"""
    template_name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the message template.</p>"""
    template_type: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The type of channel that the message template is designed for. Possible values are: EMAIL, PUSH, SMS, INAPP, and VOICE.</p>"""
    version: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the version of the message template. This value is an integer that Amazon Pinpoint automatically increments and assigns to each new version of a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateVersionResponse) -> dict:
    out: dict = {}
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "default_substitutions" in value:
        out["DefaultSubstitutions"] = value["default_substitutions"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "template_description" in value:
        out["TemplateDescription"] = value["template_description"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_type" in value:
        out["TemplateType"] = value["template_type"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> TemplateVersionResponse:
    out: TemplateVersionResponse = {}  # type: ignore[typeddict-item]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "DefaultSubstitutions" in data:
        out["default_substitutions"] = data["DefaultSubstitutions"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "TemplateDescription" in data:
        out["template_description"] = data["TemplateDescription"]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateType" in data:
        out["template_type"] = data["TemplateType"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
