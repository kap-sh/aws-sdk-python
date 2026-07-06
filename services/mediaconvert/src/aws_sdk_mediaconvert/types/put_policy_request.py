"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PutPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.policy


class PutPolicyRequest(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_mediaconvert.types.policy.Policy"]
    """A policy configures behavior that you allow or disallow for your account. For information about MediaConvert policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPolicyRequest) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_mediaconvert.types.policy

        out["policy"] = aws_sdk_mediaconvert.types.policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> PutPolicyRequest:
    out: PutPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_mediaconvert.types.policy

        out["policy"] = aws_sdk_mediaconvert.types.policy.deserialize_json(
            data["policy"]
        )
    return out
