"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.resource_policy


class GetResourcePolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_cloudhsm_v2.types.resource_policy.ResourcePolicy"]
    """<p>The policy attached to a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
