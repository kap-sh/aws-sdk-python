"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.tag_list
    import aws_sdk_quicksight.types.template_name
    import aws_sdk_quicksight.types.template_source_entity
    import aws_sdk_quicksight.types.template_version_definition
    import aws_sdk_quicksight.types.validation_strategy
    import aws_sdk_quicksight.types.version_description


class CreateTemplateRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. You use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    template_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An ID for the template that you want to create. This template is unique per Amazon Web Services Region; in each Amazon Web Services account.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.template_name.TemplateName"]
    """<p>A display name for the template.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A list of resource permissions to be set on the template. </p>"""
    source_entity: NotRequired[
        "aws_sdk_quicksight.types.template_source_entity.TemplateSourceEntity"
    ]
    """<p>The entity that you are using as a source when you create the template. In <code>SourceEntity</code>, you specify the type of object you're using as source: <code>SourceTemplate</code> for a template or <code>SourceAnalysis</code> for an analysis. Both of these require an Amazon Resource Name (ARN). For <code>SourceTemplate</code>, specify the ARN of the source template. For <code>SourceAnalysis</code>, specify the ARN of the source analysis. The <code>SourceTemplate</code> ARN can contain any Amazon Web Services account and any Quick Sight-supported Amazon Web Services Region. </p> <p>Use the <code>DataSetReferences</code> entity within <code>SourceTemplate</code> or <code>SourceAnalysis</code> to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder. </p> <p>Either a <code>SourceEntity</code> or a <code>Definition</code> must be provided in order for the request to be valid.</p>"""
    tags: NotRequired["aws_sdk_quicksight.types.tag_list.TagList"]
    """<p>Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.</p>"""
    version_description: NotRequired[
        "aws_sdk_quicksight.types.version_description.VersionDescription"
    ]
    """<p>A description of the current template version being created. This API operation creates the first version of the template. Every time <code>UpdateTemplate</code> is called, a new version is created. Each version of the template maintains a description of the version in the <code>VersionDescription</code> field.</p>"""
    definition: NotRequired[
        "aws_sdk_quicksight.types.template_version_definition.TemplateVersionDefinition"
    ]
    """<p>The definition of a template.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p> <p>Either a <code>SourceEntity</code> or a <code>Definition</code> must be provided in order for the request to be valid.</p>"""
    validation_strategy: NotRequired[
        "aws_sdk_quicksight.types.validation_strategy.ValidationStrategy"
    ]
    """<p>TThe option to relax the validation needed to create a template with definition objects. This skips the validation step for specific errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "source_entity" in value:
        import aws_sdk_quicksight.types.template_source_entity

        out["SourceEntity"] = (
            aws_sdk_quicksight.types.template_source_entity.serialize_json(
                value["source_entity"]
            )
        )
    if "tags" in value:
        import aws_sdk_quicksight.types.tag_list

        out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "definition" in value:
        import aws_sdk_quicksight.types.template_version_definition

        out["Definition"] = (
            aws_sdk_quicksight.types.template_version_definition.serialize_json(
                value["definition"]
            )
        )
    if "validation_strategy" in value:
        import aws_sdk_quicksight.types.validation_strategy

        out["ValidationStrategy"] = (
            aws_sdk_quicksight.types.validation_strategy.serialize_json(
                value["validation_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTemplateRequest:
    out: CreateTemplateRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Permissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "SourceEntity" in data:
        import aws_sdk_quicksight.types.template_source_entity

        out["source_entity"] = (
            aws_sdk_quicksight.types.template_source_entity.deserialize_json(
                data["SourceEntity"]
            )
        )
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "Definition" in data:
        import aws_sdk_quicksight.types.template_version_definition

        out["definition"] = (
            aws_sdk_quicksight.types.template_version_definition.deserialize_json(
                data["Definition"]
            )
        )
    if "ValidationStrategy" in data:
        import aws_sdk_quicksight.types.validation_strategy

        out["validation_strategy"] = (
            aws_sdk_quicksight.types.validation_strategy.deserialize_json(
                data["ValidationStrategy"]
            )
        )
    return out
