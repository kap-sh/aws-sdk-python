"""Generated from Smithy shape ``com.amazonaws.iam#GetPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type


class GetPolicyRequest(TypedDict):
    policy_arn: "aws_sdk_iam.types.arn_type.arnType"
    r"""<p>The Amazon Resource Name (ARN) of the managed policy that you want information about.</p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.PolicyArn", str(value["policy_arn"])))


def deserialize_query(el: Element) -> GetPolicyRequest:
    out: GetPolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    else:
        raise DeserializationError("GetPolicyRequest.policy_arn required")
    return out
