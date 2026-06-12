"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateResiliencyPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.resiliency_policy


class UpdateResiliencyPolicyResponse(TypedDict):
    policy: "aws_sdk_resiliencehub.types.resiliency_policy.ResiliencyPolicy"
    """<p>The resiliency policy that was updated, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResiliencyPolicyResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.resiliency_policy

    out["policy"] = aws_sdk_resiliencehub.types.resiliency_policy.serialize_json(
        value["policy"]
    )
    return out


def deserialize_json(data: dict) -> UpdateResiliencyPolicyResponse:
    out: UpdateResiliencyPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_resiliencehub.types.resiliency_policy

        out["policy"] = aws_sdk_resiliencehub.types.resiliency_policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("UpdateResiliencyPolicyResponse.policy required")
    return out
