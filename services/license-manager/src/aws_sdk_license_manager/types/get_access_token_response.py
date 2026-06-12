"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetAccessTokenResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.token_string


class GetAccessTokenResponse(TypedDict):
    access_token: NotRequired["aws_sdk_license_manager.types.token_string.TokenString"]
    """<p>Temporary access token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccessTokenResponse) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccessTokenResponse:
    out: GetAccessTokenResponse = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    return out
