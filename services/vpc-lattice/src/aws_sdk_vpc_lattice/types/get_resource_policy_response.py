"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.policy_string


class GetResourcePolicyResponse(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_vpc_lattice.types.policy_string.PolicyString"]
    """<p>An IAM policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
