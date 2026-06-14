"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteResiliencyPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.client_token


class DeleteResiliencyPolicyRequest(TypedDict):
    policy_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    client_token: NotRequired["aws_sdk_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResiliencyPolicyRequest) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteResiliencyPolicyRequest:
    out: DeleteResiliencyPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("DeleteResiliencyPolicyRequest.policy_arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
