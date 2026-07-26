"""Generated from Smithy shape ``com.amazonaws.connect#GetFederationTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_resource_id
    import capo_connect.types.arn
    import capo_connect.types.credentials
    import capo_connect.types.url


class GetFederationTokenResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_connect.types.credentials.Credentials"]
    """<p>The credentials to use for federation.</p>"""
    sign_in_url: NotRequired["capo_connect.types.url.Url"]
    """<p>The URL to sign into the user's instance. </p>"""
    user_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the user.</p>"""
    user_id: NotRequired["capo_connect.types.agent_resource_id.AgentResourceId"]
    """<p>The identifier for the user. This can be the ID or the ARN of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFederationTokenResponse) -> dict:
    out: dict = {}
    if "credentials" in value:
        import capo_connect.types.credentials

        out["Credentials"] = capo_connect.types.credentials.serialize_json(
            value["credentials"]
        )
    if "sign_in_url" in value:
        out["SignInUrl"] = value["sign_in_url"]
    if "user_arn" in value:
        out["UserArn"] = value["user_arn"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> GetFederationTokenResponse:
    out: GetFederationTokenResponse = {}  # type: ignore[typeddict-item]
    if "Credentials" in data:
        import capo_connect.types.credentials

        out["credentials"] = capo_connect.types.credentials.deserialize_json(
            data["Credentials"]
        )
    if "SignInUrl" in data:
        out["sign_in_url"] = data["SignInUrl"]
    if "UserArn" in data:
        out["user_arn"] = data["UserArn"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    return out
