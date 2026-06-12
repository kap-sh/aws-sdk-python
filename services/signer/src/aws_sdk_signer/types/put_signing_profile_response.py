"""Generated from Smithy shape ``com.amazonaws.signer#PutSigningProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.arn
    import aws_sdk_signer.types.profile_version
    import aws_sdk_signer.types.string


class PutSigningProfileResponse(TypedDict):
    arn: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the signing profile created.</p>"""
    profile_version: NotRequired["aws_sdk_signer.types.profile_version.ProfileVersion"]
    """<p>The version of the signing profile being created.</p>"""
    profile_version_arn: NotRequired["aws_sdk_signer.types.arn.Arn"]
    """<p>The signing profile ARN, including the profile version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSigningProfileResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "profile_version" in value:
        out["profileVersion"] = value["profile_version"]
    if "profile_version_arn" in value:
        out["profileVersionArn"] = value["profile_version_arn"]
    return out


def deserialize_json(data: dict) -> PutSigningProfileResponse:
    out: PutSigningProfileResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "profileVersion" in data:
        out["profile_version"] = data["profileVersion"]
    if "profileVersionArn" in data:
        out["profile_version_arn"] = data["profileVersionArn"]
    return out
