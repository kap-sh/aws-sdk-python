"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateProfileShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.share_id


class CreateProfileShareOutput(TypedDict, closed=True):
    share_id: NotRequired["aws_sdk_wellarchitected.types.share_id.ShareId"]
    profile_arn: NotRequired["aws_sdk_wellarchitected.types.profile_arn.ProfileArn"]
    """<p>The profile ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileShareOutput) -> dict:
    out: dict = {}
    if "share_id" in value:
        out["ShareId"] = value["share_id"]
    if "profile_arn" in value:
        out["ProfileArn"] = value["profile_arn"]
    return out


def deserialize_json(data: dict) -> CreateProfileShareOutput:
    out: CreateProfileShareOutput = {}  # type: ignore[typeddict-item]
    if "ShareId" in data:
        out["share_id"] = data["ShareId"]
    if "ProfileArn" in data:
        out["profile_arn"] = data["ProfileArn"]
    return out
