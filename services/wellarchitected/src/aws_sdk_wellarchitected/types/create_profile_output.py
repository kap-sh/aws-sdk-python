"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.profile_version


class CreateProfileOutput(TypedDict, closed=True):
    profile_arn: NotRequired["aws_sdk_wellarchitected.types.profile_arn.ProfileArn"]
    """<p>The profile ARN.</p>"""
    profile_version: NotRequired[
        "aws_sdk_wellarchitected.types.profile_version.ProfileVersion"
    ]
    """<p>Version of the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileOutput) -> dict:
    out: dict = {}
    if "profile_arn" in value:
        out["ProfileArn"] = value["profile_arn"]
    if "profile_version" in value:
        out["ProfileVersion"] = value["profile_version"]
    return out


def deserialize_json(data: dict) -> CreateProfileOutput:
    out: CreateProfileOutput = {}  # type: ignore[typeddict-item]
    if "ProfileArn" in data:
        out["profile_arn"] = data["ProfileArn"]
    if "ProfileVersion" in data:
        out["profile_version"] = data["ProfileVersion"]
    return out
