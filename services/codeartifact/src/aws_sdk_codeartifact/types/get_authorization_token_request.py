"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetAuthorizationTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.authorization_token_duration_seconds
    import aws_sdk_codeartifact.types.domain_name


class GetAuthorizationTokenRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that is in scope for the generated authorization token. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    duration_seconds: NotRequired[
        "aws_sdk_codeartifact.types.authorization_token_duration_seconds.AuthorizationTokenDurationSeconds"
    ]
    """<p>The time, in seconds, that the generated authorization token is valid. Valid values are <code>0</code> and any number between <code>900</code> (15 minutes) and <code>43200</code> (12 hours). A value of <code>0</code> will set the expiration of the authorization token to the same expiration of the user's role's temporary credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthorizationTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAuthorizationTokenRequest:
    out: GetAuthorizationTokenRequest = {}  # type: ignore[typeddict-item]
    return out
