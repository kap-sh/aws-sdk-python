"""Generated from Smithy shape ``com.amazonaws.signer#ListSigningProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.next_token
    import aws_sdk_signer.types.signing_profiles


class ListSigningProfilesResponse(TypedDict, closed=True):
    profiles: NotRequired["aws_sdk_signer.types.signing_profiles.SigningProfiles"]
    """<p>A list of profiles that are available in the AWS account. This includes profiles with the status of <code>CANCELED</code> if the <code>includeCanceled</code> parameter is set to <code>true</code>.</p>"""
    next_token: NotRequired["aws_sdk_signer.types.next_token.NextToken"]
    """<p>Value for specifying the next set of paginated results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSigningProfilesResponse) -> dict:
    out: dict = {}
    if "profiles" in value:
        import aws_sdk_signer.types.signing_profiles

        out["profiles"] = aws_sdk_signer.types.signing_profiles.serialize_json(
            value["profiles"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSigningProfilesResponse:
    out: ListSigningProfilesResponse = {}  # type: ignore[typeddict-item]
    if "profiles" in data:
        import aws_sdk_signer.types.signing_profiles

        out["profiles"] = aws_sdk_signer.types.signing_profiles.deserialize_json(
            data["profiles"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
