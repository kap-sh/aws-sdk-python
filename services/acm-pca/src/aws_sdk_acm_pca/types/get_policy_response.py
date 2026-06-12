"""Generated from Smithy shape ``com.amazonaws.acmpca#GetPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.aws_policy


class GetPolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_acm_pca.types.aws_policy.AWSPolicy"]
    """<p>The policy attached to the private CA as a JSON document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
