"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTemplateDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.template_error_list
    import aws_sdk_quicksight.types.template_name
    import aws_sdk_quicksight.types.template_version_definition


class DescribeTemplateDefinitionResponse(TypedDict):
    name: NotRequired["aws_sdk_quicksight.types.template_name.TemplateName"]
    """<p>The descriptive name of the template.</p>"""
    template_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the template described.</p>"""
    errors: NotRequired[
        "aws_sdk_quicksight.types.template_error_list.TemplateErrorList"
    ]
    """<p>Errors associated with the template version.</p>"""
    resource_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>Status associated with the template.</p> <ul> <li> <p> <code>CREATION_IN_PROGRESS</code> </p> </li> <li> <p> <code>CREATION_SUCCESSFUL</code> </p> </li> <li> <p> <code>CREATION_FAILED</code> </p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> </p> </li> <li> <p> <code>UPDATE_FAILED</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> </ul>"""
    theme_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme of the template.</p>"""
    definition: NotRequired[
        "aws_sdk_quicksight.types.template_version_definition.TemplateVersionDefinition"
    ]
    """<p>The definition of the template.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTemplateDefinitionResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "errors" in value:
        import aws_sdk_quicksight.types.template_error_list

        out["Errors"] = aws_sdk_quicksight.types.template_error_list.serialize_json(
            value["errors"]
        )
    if "resource_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["ResourceStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["resource_status"]
        )
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "definition" in value:
        import aws_sdk_quicksight.types.template_version_definition

        out["Definition"] = (
            aws_sdk_quicksight.types.template_version_definition.serialize_json(
                value["definition"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeTemplateDefinitionResponse:
    out: DescribeTemplateDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    if "Errors" in data:
        import aws_sdk_quicksight.types.template_error_list

        out["errors"] = aws_sdk_quicksight.types.template_error_list.deserialize_json(
            data["Errors"]
        )
    if "ResourceStatus" in data:
        import aws_sdk_quicksight.types.resource_status

        out["resource_status"] = (
            aws_sdk_quicksight.types.resource_status.deserialize_json(
                data["ResourceStatus"]
            )
        )
    if "ThemeArn" in data:
        out["theme_arn"] = data["ThemeArn"]
    if "Definition" in data:
        import aws_sdk_quicksight.types.template_version_definition

        out["definition"] = (
            aws_sdk_quicksight.types.template_version_definition.deserialize_json(
                data["Definition"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
