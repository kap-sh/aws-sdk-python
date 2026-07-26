"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn


class GetPolicyRequest(TypedDict, closed=True):
    policy_arn: "capo_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyRequest:
    out: GetPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
