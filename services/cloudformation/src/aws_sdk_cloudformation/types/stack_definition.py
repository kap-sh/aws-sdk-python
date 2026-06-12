"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_name
    import aws_sdk_cloudformation.types.template_body
    import aws_sdk_cloudformation.types.template_url


class StackDefinition(TypedDict):
    stack_name: NotRequired["aws_sdk_cloudformation.types.stack_name.StackName"]
    """<p>The name associated with the stack.</p>"""
    template_body: NotRequired[
        "aws_sdk_cloudformation.types.template_body.TemplateBody"
    ]
    """<p>The file path for the stack template file.</p>"""
    template_url: NotRequired["aws_sdk_cloudformation.types.template_url.TemplateURL"]
    """<p>The desired final state of the stack template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackDefinition, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "template_body" in value:
        pairs.append((f"{prefix}.TemplateBody", str(value["template_body"])))
    if "template_url" in value:
        pairs.append((f"{prefix}.TemplateURL", str(value["template_url"])))


def deserialize_query(el: Element) -> StackDefinition:
    out: StackDefinition = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_template_body = el.find("TemplateBody")
    if child_template_body is not None:
        out["template_body"] = str(child_template_body.text or "")
    child_template_url = el.find("TemplateURL")
    if child_template_url is not None:
        out["template_url"] = str(child_template_url.text or "")
    return out
