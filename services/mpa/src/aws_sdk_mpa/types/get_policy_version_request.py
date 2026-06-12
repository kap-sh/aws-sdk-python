"""Generated from Smithy shape ``com.amazonaws.mpa#GetPolicyVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.qualified_policy_arn


class GetPolicyVersionRequest(TypedDict):
    policy_version_arn: "aws_sdk_mpa.types.qualified_policy_arn.QualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyVersionRequest:
    out: GetPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    return out
