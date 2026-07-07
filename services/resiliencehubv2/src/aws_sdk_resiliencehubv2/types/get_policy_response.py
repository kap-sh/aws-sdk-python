"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.policy


class GetPolicyResponse(TypedDict, closed=True):
    policy: "aws_sdk_resiliencehubv2.types.policy.Policy"
    """<p>The requested resilience policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.policy

    out["policy"] = aws_sdk_resiliencehubv2.types.policy.serialize_json(value["policy"])
    return out


def deserialize_json(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_resiliencehubv2.types.policy

        out["policy"] = aws_sdk_resiliencehubv2.types.policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("GetPolicyResponse.policy required")
    return out
