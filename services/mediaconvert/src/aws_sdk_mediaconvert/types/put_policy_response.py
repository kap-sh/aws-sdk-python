"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PutPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.policy


class PutPolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_mediaconvert.types.policy.Policy"]
    """A policy configures behavior that you allow or disallow for your account. For information about MediaConvert policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_mediaconvert.types.policy

        out["policy"] = aws_sdk_mediaconvert.types.policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> PutPolicyResponse:
    out: PutPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_mediaconvert.types.policy

        out["policy"] = aws_sdk_mediaconvert.types.policy.deserialize_json(
            data["policy"]
        )
    return out
