"""Generated from Smithy shape ``com.amazonaws.amplifybackend#BackendAPIAppSyncAuthSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__double
    import aws_sdk_amplifybackend.types.__string


class BackendAPIAppSyncAuthSettings(TypedDict):
    cognito_user_pool_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The Amazon Cognito user pool ID, if Amazon Cognito was used as an authentication setting to access your data models.</p>"""
    description: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The API key description for API_KEY, if it was used as an authentication mechanism to access your data models.</p>"""
    expiration_time: NotRequired["aws_sdk_amplifybackend.types.__double.__double"]
    """<p>The API key expiration time for API_KEY, if it was used as an authentication mechanism to access your data models.</p>"""
    open_id_auth_ttl: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The expiry time for the OpenID authentication mechanism.</p>"""
    open_id_client_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The clientID for openID, if openID was used as an authentication setting to access your data models.</p>"""
    open_id_iat_ttl: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The expiry time for the OpenID authentication mechanism.</p>"""
    open_id_issue_url: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The openID issuer URL, if openID was used as an authentication setting to access your data models.</p>"""
    open_id_provider_name: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The OpenID provider name, if OpenID was used as an authentication mechanism to access your data models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendAPIAppSyncAuthSettings) -> dict:
    out: dict = {}
    if "cognito_user_pool_id" in value:
        out["cognitoUserPoolId"] = value["cognito_user_pool_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "expiration_time" in value:
        out["expirationTime"] = value["expiration_time"]
    if "open_id_auth_ttl" in value:
        out["openIDAuthTTL"] = value["open_id_auth_ttl"]
    if "open_id_client_id" in value:
        out["openIDClientId"] = value["open_id_client_id"]
    if "open_id_iat_ttl" in value:
        out["openIDIatTTL"] = value["open_id_iat_ttl"]
    if "open_id_issue_url" in value:
        out["openIDIssueURL"] = value["open_id_issue_url"]
    if "open_id_provider_name" in value:
        out["openIDProviderName"] = value["open_id_provider_name"]
    return out


def deserialize_json(data: dict) -> BackendAPIAppSyncAuthSettings:
    out: BackendAPIAppSyncAuthSettings = {}  # type: ignore[typeddict-item]
    if "cognitoUserPoolId" in data:
        out["cognito_user_pool_id"] = data["cognitoUserPoolId"]
    if "description" in data:
        out["description"] = data["description"]
    if "expirationTime" in data:
        out["expiration_time"] = data["expirationTime"]
    if "openIDAuthTTL" in data:
        out["open_id_auth_ttl"] = data["openIDAuthTTL"]
    if "openIDClientId" in data:
        out["open_id_client_id"] = data["openIDClientId"]
    if "openIDIatTTL" in data:
        out["open_id_iat_ttl"] = data["openIDIatTTL"]
    if "openIDIssueURL" in data:
        out["open_id_issue_url"] = data["openIDIssueURL"]
    if "openIDProviderName" in data:
        out["open_id_provider_name"] = data["openIDProviderName"]
    return out
