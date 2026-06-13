"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ImportPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.policy


class ImportPolicyResponse(TypedDict):
    policy: "aws_sdk_resiliencehubv2.types.policy.Policy"
    """<p>The imported policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportPolicyResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.policy

    out["policy"] = aws_sdk_resiliencehubv2.types.policy.serialize_json(value["policy"])
    return out


def deserialize_json(data: dict) -> ImportPolicyResponse:
    out: ImportPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_resiliencehubv2.types.policy

        out["policy"] = aws_sdk_resiliencehubv2.types.policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("ImportPolicyResponse.policy required")
    return out
