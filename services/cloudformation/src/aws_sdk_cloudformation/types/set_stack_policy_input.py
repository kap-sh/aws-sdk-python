"""Generated from Smithy shape ``com.amazonaws.cloudformation#SetStackPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_name
    import aws_sdk_cloudformation.types.stack_policy_body
    import aws_sdk_cloudformation.types.stack_policy_url


class SetStackPolicyInput(TypedDict):
    stack_name: NotRequired["aws_sdk_cloudformation.types.stack_name.StackName"]
    """<p>The name or unique stack ID that you want to associate a policy with.</p>"""
    stack_policy_body: NotRequired[
        "aws_sdk_cloudformation.types.stack_policy_body.StackPolicyBody"
    ]
    r"""<p>Structure that contains the stack policy body. For more information, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html\">Prevent updates to stack resources</a> in the <i>CloudFormation User Guide</i>. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p>"""
    stack_policy_url: NotRequired[
        "aws_sdk_cloudformation.types.stack_policy_url.StackPolicyURL"
    ]
    """<p>Location of a file that contains the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an Amazon S3 bucket in the same Amazon Web Services Region as the stack. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetStackPolicyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "stack_policy_body" in value:
        pairs.append((f"{prefix}.StackPolicyBody", str(value["stack_policy_body"])))
    if "stack_policy_url" in value:
        pairs.append((f"{prefix}.StackPolicyURL", str(value["stack_policy_url"])))


def deserialize_query(el: Element) -> SetStackPolicyInput:
    out: SetStackPolicyInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_stack_policy_body = el.find("StackPolicyBody")
    if child_stack_policy_body is not None:
        out["stack_policy_body"] = str(child_stack_policy_body.text or "")
    child_stack_policy_url = el.find("StackPolicyURL")
    if child_stack_policy_url is not None:
        out["stack_policy_url"] = str(child_stack_policy_url.text or "")
    return out
