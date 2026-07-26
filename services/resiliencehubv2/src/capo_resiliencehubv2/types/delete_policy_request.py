"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeletePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn


class DeletePolicyRequest(TypedDict, closed=True):
    policy_arn: "capo_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyRequest) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> DeletePolicyRequest:
    out: DeletePolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("DeletePolicyRequest.policy_arn required")
    return out
