"""Generated from Smithy shape ``com.amazonaws.cloudformation#CreateStackRefactorInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.description
    import aws_sdk_cloudformation.types.enable_stack_creation
    import aws_sdk_cloudformation.types.resource_mappings
    import aws_sdk_cloudformation.types.stack_definitions


class CreateStackRefactorInput(TypedDict):
    description: NotRequired["aws_sdk_cloudformation.types.description.Description"]
    """<p>A description to help you identify the stack refactor.</p>"""
    enable_stack_creation: NotRequired[
        "aws_sdk_cloudformation.types.enable_stack_creation.EnableStackCreation"
    ]
    """<p>Determines if a new stack is created with the refactor.</p>"""
    resource_mappings: NotRequired[
        "aws_sdk_cloudformation.types.resource_mappings.ResourceMappings"
    ]
    """<p>The mappings for the stack resource <code>Source</code> and stack resource <code>Destination</code>.</p>"""
    stack_definitions: NotRequired[
        "aws_sdk_cloudformation.types.stack_definitions.StackDefinitions"
    ]
    """<p>The stacks being refactored.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateStackRefactorInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "enable_stack_creation" in value:
        pairs.append(
            (
                f"{prefix}.EnableStackCreation",
                "true" if value["enable_stack_creation"] else "false",
            )
        )
    if "resource_mappings" in value:
        import aws_sdk_cloudformation.types.resource_mappings

        aws_sdk_cloudformation.types.resource_mappings.serialize_query(
            value["resource_mappings"], pairs, f"{prefix}.ResourceMappings"
        )
    if "stack_definitions" in value:
        import aws_sdk_cloudformation.types.stack_definitions

        aws_sdk_cloudformation.types.stack_definitions.serialize_query(
            value["stack_definitions"], pairs, f"{prefix}.StackDefinitions"
        )


def deserialize_query(el: Element) -> CreateStackRefactorInput:
    out: CreateStackRefactorInput = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_enable_stack_creation = el.find("EnableStackCreation")
    if child_enable_stack_creation is not None:
        out["enable_stack_creation"] = (
            child_enable_stack_creation.text or ""
        ).lower() == "true"
    child_resource_mappings = el.find("ResourceMappings")
    if child_resource_mappings is not None:
        import aws_sdk_cloudformation.types.resource_mappings

        out["resource_mappings"] = (
            aws_sdk_cloudformation.types.resource_mappings.deserialize_query(
                child_resource_mappings
            )
        )
    child_stack_definitions = el.find("StackDefinitions")
    if child_stack_definitions is not None:
        import aws_sdk_cloudformation.types.stack_definitions

        out["stack_definitions"] = (
            aws_sdk_cloudformation.types.stack_definitions.deserialize_query(
                child_stack_definitions
            )
        )
    return out
