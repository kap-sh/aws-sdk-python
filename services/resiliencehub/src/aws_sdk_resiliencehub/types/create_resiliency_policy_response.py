"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CreateResiliencyPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.resiliency_policy


class CreateResiliencyPolicyResponse(TypedDict, closed=True):
    policy: "aws_sdk_resiliencehub.types.resiliency_policy.ResiliencyPolicy"
    """<p>The type of resiliency policy that was created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResiliencyPolicyResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.resiliency_policy

    out["policy"] = aws_sdk_resiliencehub.types.resiliency_policy.serialize_json(
        value["policy"]
    )
    return out


def deserialize_json(data: dict) -> CreateResiliencyPolicyResponse:
    out: CreateResiliencyPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_resiliencehub.types.resiliency_policy

        out["policy"] = aws_sdk_resiliencehub.types.resiliency_policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("CreateResiliencyPolicyResponse.policy required")
    return out
