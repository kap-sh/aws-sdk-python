"""Generated from Smithy shape ``com.amazonaws.cloudformation#CreateGeneratedTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.generated_template_name
    import capo_cloudformation.types.resource_definitions
    import capo_cloudformation.types.stack_name
    import capo_cloudformation.types.template_configuration


class CreateGeneratedTemplateInput(TypedDict, closed=True):
    resources: NotRequired[
        "capo_cloudformation.types.resource_definitions.ResourceDefinitions"
    ]
    """<p>An optional list of resources to be included in the generated template.</p> <p>If no resources are specified,the template will be created without any resources. Resources can be added to the template using the <code>UpdateGeneratedTemplate</code> API action.</p>"""
    generated_template_name: NotRequired[
        "capo_cloudformation.types.generated_template_name.GeneratedTemplateName"
    ]
    """<p>The name assigned to the generated template.</p>"""
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<p>An optional name or ARN of a stack to use as the base stack for the generated template.</p>"""
    template_configuration: NotRequired[
        "capo_cloudformation.types.template_configuration.TemplateConfiguration"
    ]
    """<p>The configuration details of the generated template, including the <code>DeletionPolicy</code> and <code>UpdateReplacePolicy</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateGeneratedTemplateInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resources" in value:
        import capo_cloudformation.types.resource_definitions

        capo_cloudformation.types.resource_definitions.serialize_query(
            value["resources"], pairs, f"{key_prefix}Resources"
        )
    if "generated_template_name" in value:
        pairs.append(
            (
                f"{key_prefix}GeneratedTemplateName",
                str(value["generated_template_name"]),
            )
        )
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "template_configuration" in value:
        import capo_cloudformation.types.template_configuration

        capo_cloudformation.types.template_configuration.serialize_query(
            value["template_configuration"], pairs, f"{key_prefix}TemplateConfiguration"
        )


def deserialize_query(el: Element) -> CreateGeneratedTemplateInput:
    out: CreateGeneratedTemplateInput = {}  # type: ignore[typeddict-item]
    child_resources = el.find("Resources")
    if child_resources is not None:
        import capo_cloudformation.types.resource_definitions

        out["resources"] = (
            capo_cloudformation.types.resource_definitions.deserialize_query(
                child_resources
            )
        )
    child_generated_template_name = el.find("GeneratedTemplateName")
    if child_generated_template_name is not None:
        out["generated_template_name"] = str(child_generated_template_name.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_template_configuration = el.find("TemplateConfiguration")
    if child_template_configuration is not None:
        import capo_cloudformation.types.template_configuration

        out["template_configuration"] = (
            capo_cloudformation.types.template_configuration.deserialize_query(
                child_template_configuration
            )
        )
    return out
