"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAppSyncGraphQlApiOpenIdConnectConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.long
    import aws_sdk_securityhub.types.non_empty_string


class AwsAppSyncGraphQlApiOpenIdConnectConfigDetails(TypedDict, closed=True):
    auth_tt_l: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p> The number of milliseconds that a token is valid after being authenticated. </p>"""
    client_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The client identifier of the relying party at the OpenID identity provider. This identifier is typically obtained when the relying party is registered with the OpenID identity provider. You can specify a regular expression so that AppSync can validate against multiple client identifiers at a time. </p>"""
    iat_tt_l: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p> The number of milliseconds that a token is valid after it's issued to a user. </p>"""
    issuer: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of <code>iss</code> in the ID token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAppSyncGraphQlApiOpenIdConnectConfigDetails) -> dict:
    out: dict = {}
    if "auth_tt_l" in value:
        out["AuthTtL"] = value["auth_tt_l"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "iat_tt_l" in value:
        out["IatTtL"] = value["iat_tt_l"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    return out


def deserialize_json(data: dict) -> AwsAppSyncGraphQlApiOpenIdConnectConfigDetails:
    out: AwsAppSyncGraphQlApiOpenIdConnectConfigDetails = {}  # type: ignore[typeddict-item]
    if "AuthTtL" in data:
        out["auth_tt_l"] = data["AuthTtL"]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "IatTtL" in data:
        out["iat_tt_l"] = data["IatTtL"]
    if "Issuer" in data:
        out["issuer"] = data["Issuer"]
    return out
