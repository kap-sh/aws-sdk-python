"""Generated from Smithy shape ``com.amazonaws.iot#RegistrationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.template_body
    import aws_sdk_iot.types.template_name


class RegistrationConfig(TypedDict, closed=True):
    template_body: NotRequired["aws_sdk_iot.types.template_body.TemplateBody"]
    """<p>The template body.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The ARN of the role.</p>"""
    template_name: NotRequired["aws_sdk_iot.types.template_name.TemplateName"]
    """<p>The name of the provisioning template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationConfig) -> dict:
    out: dict = {}
    if "template_body" in value:
        out["templateBody"] = value["template_body"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    return out


def deserialize_json(data: dict) -> RegistrationConfig:
    out: RegistrationConfig = {}  # type: ignore[typeddict-item]
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    return out
