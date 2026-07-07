"""Generated from Smithy shape ``com.amazonaws.cloudformation#UpdateGeneratedTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.generated_template_name
    import aws_sdk_cloudformation.types.jazz_logical_resource_ids
    import aws_sdk_cloudformation.types.refresh_all_resources
    import aws_sdk_cloudformation.types.resource_definitions
    import aws_sdk_cloudformation.types.template_configuration


class UpdateGeneratedTemplateInput(TypedDict, closed=True):
    generated_template_name: NotRequired[
        "aws_sdk_cloudformation.types.generated_template_name.GeneratedTemplateName"
    ]
    """<p>The name or Amazon Resource Name (ARN) of a generated template.</p>"""
    new_generated_template_name: NotRequired[
        "aws_sdk_cloudformation.types.generated_template_name.GeneratedTemplateName"
    ]
    """<p>An optional new name to assign to the generated template.</p>"""
    add_resources: NotRequired[
        "aws_sdk_cloudformation.types.resource_definitions.ResourceDefinitions"
    ]
    """<p>An optional list of resources to be added to the generated template.</p>"""
    remove_resources: NotRequired[
        "aws_sdk_cloudformation.types.jazz_logical_resource_ids.JazzLogicalResourceIds"
    ]
    """<p>A list of logical ids for resources to remove from the generated template.</p>"""
    refresh_all_resources: NotRequired[
        "aws_sdk_cloudformation.types.refresh_all_resources.RefreshAllResources"
    ]
    """<p>If <code>true</code>, update the resource properties in the generated template with their current live state. This feature is useful when the resource properties in your generated a template does not reflect the live state of the resource properties. This happens when a user update the resource properties after generating a template.</p>"""
    template_configuration: NotRequired[
        "aws_sdk_cloudformation.types.template_configuration.TemplateConfiguration"
    ]
    """<p>The configuration details of the generated template, including the <code>DeletionPolicy</code> and <code>UpdateReplacePolicy</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateGeneratedTemplateInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "generated_template_name" in value:
        pairs.append(
            (f"{prefix}.GeneratedTemplateName", str(value["generated_template_name"]))
        )
    if "new_generated_template_name" in value:
        pairs.append(
            (
                f"{prefix}.NewGeneratedTemplateName",
                str(value["new_generated_template_name"]),
            )
        )
    if "add_resources" in value:
        import aws_sdk_cloudformation.types.resource_definitions

        aws_sdk_cloudformation.types.resource_definitions.serialize_query(
            value["add_resources"], pairs, f"{prefix}.AddResources"
        )
    if "remove_resources" in value:
        import aws_sdk_cloudformation.types.jazz_logical_resource_ids

        aws_sdk_cloudformation.types.jazz_logical_resource_ids.serialize_query(
            value["remove_resources"], pairs, f"{prefix}.RemoveResources"
        )
    if "refresh_all_resources" in value:
        pairs.append(
            (
                f"{prefix}.RefreshAllResources",
                "true" if value["refresh_all_resources"] else "false",
            )
        )
    if "template_configuration" in value:
        import aws_sdk_cloudformation.types.template_configuration

        aws_sdk_cloudformation.types.template_configuration.serialize_query(
            value["template_configuration"], pairs, f"{prefix}.TemplateConfiguration"
        )


def deserialize_query(el: Element) -> UpdateGeneratedTemplateInput:
    out: UpdateGeneratedTemplateInput = {}  # type: ignore[typeddict-item]
    child_generated_template_name = el.find("GeneratedTemplateName")
    if child_generated_template_name is not None:
        out["generated_template_name"] = str(child_generated_template_name.text or "")
    child_new_generated_template_name = el.find("NewGeneratedTemplateName")
    if child_new_generated_template_name is not None:
        out["new_generated_template_name"] = str(
            child_new_generated_template_name.text or ""
        )
    child_add_resources = el.find("AddResources")
    if child_add_resources is not None:
        import aws_sdk_cloudformation.types.resource_definitions

        out["add_resources"] = (
            aws_sdk_cloudformation.types.resource_definitions.deserialize_query(
                child_add_resources
            )
        )
    child_remove_resources = el.find("RemoveResources")
    if child_remove_resources is not None:
        import aws_sdk_cloudformation.types.jazz_logical_resource_ids

        out["remove_resources"] = (
            aws_sdk_cloudformation.types.jazz_logical_resource_ids.deserialize_query(
                child_remove_resources
            )
        )
    child_refresh_all_resources = el.find("RefreshAllResources")
    if child_refresh_all_resources is not None:
        out["refresh_all_resources"] = (
            child_refresh_all_resources.text or ""
        ).lower() == "true"
    child_template_configuration = el.find("TemplateConfiguration")
    if child_template_configuration is not None:
        import aws_sdk_cloudformation.types.template_configuration

        out["template_configuration"] = (
            aws_sdk_cloudformation.types.template_configuration.deserialize_query(
                child_template_configuration
            )
        )
    return out
