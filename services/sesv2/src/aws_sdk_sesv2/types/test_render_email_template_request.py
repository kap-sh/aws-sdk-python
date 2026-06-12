"""Generated from Smithy shape ``com.amazonaws.sesv2#TestRenderEmailTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_template_data
    import aws_sdk_sesv2.types.email_template_name


class TestRenderEmailTemplateRequest(TypedDict):
    template_name: "aws_sdk_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the template.</p>"""
    template_data: "aws_sdk_sesv2.types.email_template_data.EmailTemplateData"
    """<p>A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRenderEmailTemplateRequest) -> dict:
    out: dict = {}
    out["TemplateData"] = value["template_data"]
    return out


def deserialize_json(data: dict) -> TestRenderEmailTemplateRequest:
    out: TestRenderEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    if "TemplateData" in data:
        out["template_data"] = data["TemplateData"]
    else:
        raise DeserializationError(
            "TestRenderEmailTemplateRequest.template_data required"
        )
    return out
