"""Generated from Smithy shape ``com.amazonaws.iot#DeletePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_name


class DeletePolicyRequest(TypedDict):
    policy_name: "aws_sdk_iot.types.policy_name.PolicyName"
    """<p>The name of the policy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePolicyRequest:
    out: DeletePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
