"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdatePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.policy


class UpdatePolicyResponse(TypedDict):
    policy: "aws_sdk_resiliencehubv2.types.policy.Policy"
    """<p>The updated policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicyResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.policy

    out["policy"] = aws_sdk_resiliencehubv2.types.policy.serialize_json(value["policy"])
    return out


def deserialize_json(data: dict) -> UpdatePolicyResponse:
    out: UpdatePolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_resiliencehubv2.types.policy

        out["policy"] = aws_sdk_resiliencehubv2.types.policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.policy required")
    return out
