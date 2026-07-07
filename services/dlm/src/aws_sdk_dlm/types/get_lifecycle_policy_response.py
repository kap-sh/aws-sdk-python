"""Generated from Smithy shape ``com.amazonaws.dlm#GetLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.lifecycle_policy


class GetLifecyclePolicyResponse(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_dlm.types.lifecycle_policy.LifecyclePolicy"]
    """<p>Detailed information about the lifecycle policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_dlm.types.lifecycle_policy

        out["Policy"] = aws_sdk_dlm.types.lifecycle_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> GetLifecyclePolicyResponse:
    out: GetLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        import aws_sdk_dlm.types.lifecycle_policy

        out["policy"] = aws_sdk_dlm.types.lifecycle_policy.deserialize_json(
            data["Policy"]
        )
    return out
