"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeResiliencyPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.resiliency_policy


class DescribeResiliencyPolicyResponse(TypedDict):
    policy: "aws_sdk_resiliencehub.types.resiliency_policy.ResiliencyPolicy"
    """<p>Information about the specific resiliency policy, returned as an object. This object includes creation time, data location constraints, its name, description, tags, the recovery time objective (RTO) and recovery point objective (RPO) in seconds, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResiliencyPolicyResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.resiliency_policy

    out["policy"] = aws_sdk_resiliencehub.types.resiliency_policy.serialize_json(
        value["policy"]
    )
    return out


def deserialize_json(data: dict) -> DescribeResiliencyPolicyResponse:
    out: DescribeResiliencyPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_resiliencehub.types.resiliency_policy

        out["policy"] = aws_sdk_resiliencehub.types.resiliency_policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("DescribeResiliencyPolicyResponse.policy required")
    return out
