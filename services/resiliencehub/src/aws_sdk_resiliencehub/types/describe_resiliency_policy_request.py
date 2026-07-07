"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeResiliencyPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn


class DescribeResiliencyPolicyRequest(TypedDict, closed=True):
    policy_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResiliencyPolicyRequest) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> DescribeResiliencyPolicyRequest:
    out: DescribeResiliencyPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "DescribeResiliencyPolicyRequest.policy_arn required"
        )
    return out
