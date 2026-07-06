"""Generated from Smithy shape ``com.amazonaws.pinpointemail#Template``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.template_arn
    import aws_sdk_pinpoint_email.types.template_data


class Template(TypedDict, closed=True):
    template_arn: NotRequired["aws_sdk_pinpoint_email.types.template_arn.TemplateArn"]
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    template_data: NotRequired[
        "aws_sdk_pinpoint_email.types.template_data.TemplateData"
    ]
    """<p>An object that defines the values to use for message variables in the template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the value to use for that variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Template) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "template_data" in value:
        out["TemplateData"] = value["template_data"]
    return out


def deserialize_json(data: dict) -> Template:
    out: Template = {}  # type: ignore[typeddict-item]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "TemplateData" in data:
        out["template_data"] = data["TemplateData"]
    return out
