"""Generated from Smithy shape ``com.amazonaws.mpa#GetPolicyVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.qualified_policy_arn


class GetPolicyVersionRequest(TypedDict, closed=True):
    policy_version_arn: "capo_mpa.types.qualified_policy_arn.QualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyVersionRequest:
    out: GetPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    return out
