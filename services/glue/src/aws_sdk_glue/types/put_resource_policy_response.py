"""Generated from Smithy shape ``com.amazonaws.glue#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class PutResourcePolicyResponse(TypedDict):
    policy_hash: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>A hash of the policy that has just been set. This must be included in a subsequent call that overwrites or updates this policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy_hash" in value:
        out["PolicyHash"] = value["policy_hash"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyHash" in data:
        out["policy_hash"] = data["PolicyHash"]
    return out
