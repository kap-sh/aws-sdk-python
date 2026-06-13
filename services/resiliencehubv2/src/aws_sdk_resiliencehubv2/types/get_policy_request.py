"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn


class GetPolicyRequest(TypedDict):
    policy_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyRequest:
    out: GetPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
