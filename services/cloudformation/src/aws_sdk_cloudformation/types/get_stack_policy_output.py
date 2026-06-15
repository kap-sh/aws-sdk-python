"""Generated from Smithy shape ``com.amazonaws.cloudformation#GetStackPolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_policy_body


class GetStackPolicyOutput(TypedDict):
    stack_policy_body: NotRequired[
        "aws_sdk_cloudformation.types.stack_policy_body.StackPolicyBody"
    ]
    r"""<p>Structure that contains the stack policy body. For more information, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html\">Prevent updates to stack resources</a> in the <i>CloudFormation User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetStackPolicyOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_policy_body" in value:
        pairs.append((f"{prefix}.StackPolicyBody", str(value["stack_policy_body"])))


def deserialize_query(el: Element) -> GetStackPolicyOutput:
    out: GetStackPolicyOutput = {}  # type: ignore[typeddict-item]
    child_stack_policy_body = el.find("StackPolicyBody")
    if child_stack_policy_body is not None:
        out["stack_policy_body"] = str(child_stack_policy_body.text or "")
    return out
