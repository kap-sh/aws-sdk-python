"""Generated from Smithy shape ``com.amazonaws.iot#DescribeProvisioningTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.enabled2
    import aws_sdk_iot.types.provisioning_hook
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.template_arn
    import aws_sdk_iot.types.template_body
    import aws_sdk_iot.types.template_description
    import aws_sdk_iot.types.template_name
    import aws_sdk_iot.types.template_type
    import aws_sdk_iot.types.template_version_id


class DescribeProvisioningTemplateResponse(TypedDict, closed=True):
    template_arn: NotRequired["aws_sdk_iot.types.template_arn.TemplateArn"]
    """<p>The ARN of the provisioning template.</p>"""
    template_name: NotRequired["aws_sdk_iot.types.template_name.TemplateName"]
    """<p>The name of the provisioning template.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.template_description.TemplateDescription"
    ]
    """<p>The description of the provisioning template.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date when the provisioning template was created.</p>"""
    last_modified_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date when the provisioning template was last modified.</p>"""
    default_version_id: NotRequired[
        "aws_sdk_iot.types.template_version_id.TemplateVersionId"
    ]
    """<p>The default fleet template version ID.</p>"""
    template_body: NotRequired["aws_sdk_iot.types.template_body.TemplateBody"]
    """<p>The JSON formatted contents of the provisioning template.</p>"""
    enabled: NotRequired["aws_sdk_iot.types.enabled2.Enabled2"]
    """<p>True if the provisioning template is enabled, otherwise false.</p>"""
    provisioning_role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The ARN of the role associated with the provisioning template. This IoT role grants permission to provision a device.</p>"""
    pre_provisioning_hook: NotRequired[
        "aws_sdk_iot.types.provisioning_hook.ProvisioningHook"
    ]
    """<p>Gets information about a pre-provisioned hook.</p>"""
    type: NotRequired["aws_sdk_iot.types.template_type.TemplateType"]
    r"""<p>The type you define in a provisioning template. You can create a template with only one type. You can't change the template type after its creation. The default value is <code>FLEET_PROVISIONING</code>. For more information about provisioning template, see: <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html\">Provisioning template</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProvisioningTemplateResponse) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_date" in value:
        import aws_sdk_iot.types.date_type

        out["creationDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.date_type

        out["lastModifiedDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_modified_date"]
        )
    if "default_version_id" in value:
        out["defaultVersionId"] = value["default_version_id"]
    if "template_body" in value:
        out["templateBody"] = value["template_body"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "provisioning_role_arn" in value:
        out["provisioningRoleArn"] = value["provisioning_role_arn"]
    if "pre_provisioning_hook" in value:
        import aws_sdk_iot.types.provisioning_hook

        out["preProvisioningHook"] = aws_sdk_iot.types.provisioning_hook.serialize_json(
            value["pre_provisioning_hook"]
        )
    if "type" in value:
        import aws_sdk_iot.types.template_type

        out["type"] = aws_sdk_iot.types.template_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> DescribeProvisioningTemplateResponse:
    out: DescribeProvisioningTemplateResponse = {}  # type: ignore[typeddict-item]
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationDate" in data:
        import aws_sdk_iot.types.date_type

        out["creation_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.date_type

        out["last_modified_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastModifiedDate"]
        )
    if "defaultVersionId" in data:
        out["default_version_id"] = data["defaultVersionId"]
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "provisioningRoleArn" in data:
        out["provisioning_role_arn"] = data["provisioningRoleArn"]
    if "preProvisioningHook" in data:
        import aws_sdk_iot.types.provisioning_hook

        out["pre_provisioning_hook"] = (
            aws_sdk_iot.types.provisioning_hook.deserialize_json(
                data["preProvisioningHook"]
            )
        )
    if "type" in data:
        import aws_sdk_iot.types.template_type

        out["type"] = aws_sdk_iot.types.template_type.deserialize_json(data["type"])
    return out
