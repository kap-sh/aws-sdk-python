"""Generated from Smithy shape ``com.amazonaws.cloudformation#GetTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.change_set_name_or_id
    import aws_sdk_cloudformation.types.stack_name
    import aws_sdk_cloudformation.types.template_stage


class GetTemplateInput(TypedDict, closed=True):
    stack_name: NotRequired["aws_sdk_cloudformation.types.stack_name.StackName"]
    """<p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul>"""
    change_set_name: NotRequired[
        "aws_sdk_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
    ]
    """<p>The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you specify a name, you must also specify the <code>StackName</code>.</p>"""
    template_stage: NotRequired[
        "aws_sdk_cloudformation.types.template_stage.TemplateStage"
    ]
    """<p>For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify <code>Original</code>. To get the template after CloudFormation has processed all transforms, specify <code>Processed</code>.</p> <p>If the template doesn't include transforms, <code>Original</code> and <code>Processed</code> return the same template. By default, CloudFormation specifies <code>Processed</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTemplateInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "change_set_name" in value:
        pairs.append((f"{prefix}.ChangeSetName", str(value["change_set_name"])))
    if "template_stage" in value:
        import aws_sdk_cloudformation.types.template_stage

        aws_sdk_cloudformation.types.template_stage.serialize_query(
            value["template_stage"], pairs, f"{prefix}.TemplateStage"
        )


def deserialize_query(el: Element) -> GetTemplateInput:
    out: GetTemplateInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_template_stage = el.find("TemplateStage")
    if child_template_stage is not None:
        import aws_sdk_cloudformation.types.template_stage

        out["template_stage"] = (
            aws_sdk_cloudformation.types.template_stage.deserialize_query(
                child_template_stage
            )
        )
    return out
