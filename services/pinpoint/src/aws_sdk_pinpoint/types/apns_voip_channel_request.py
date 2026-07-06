"""Generated from Smithy shape ``com.amazonaws.pinpoint#APNSVoipChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__string


class APNSVoipChannelRequest(TypedDict, closed=True):
    bundle_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.</p>"""
    certificate: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The APNs client certificate that you received from Apple, if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.</p>"""
    default_authentication_method: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs, key or certificate.</p>"""
    enabled: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to enable the APNs VoIP channel for the application.</p>"""
    private_key: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.</p>"""
    team_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The identifier that's assigned to your Apple developer account team. This identifier is used for APNs tokens.</p>"""
    token_key: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The authentication key to use for APNs tokens.</p>"""
    token_key_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The key identifier that's assigned to your APNs signing key, if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: APNSVoipChannelRequest) -> dict:
    out: dict = {}
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "default_authentication_method" in value:
        out["DefaultAuthenticationMethod"] = value["default_authentication_method"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "private_key" in value:
        out["PrivateKey"] = value["private_key"]
    if "team_id" in value:
        out["TeamId"] = value["team_id"]
    if "token_key" in value:
        out["TokenKey"] = value["token_key"]
    if "token_key_id" in value:
        out["TokenKeyId"] = value["token_key_id"]
    return out


def deserialize_json(data: dict) -> APNSVoipChannelRequest:
    out: APNSVoipChannelRequest = {}  # type: ignore[typeddict-item]
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    if "DefaultAuthenticationMethod" in data:
        out["default_authentication_method"] = data["DefaultAuthenticationMethod"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "PrivateKey" in data:
        out["private_key"] = data["PrivateKey"]
    if "TeamId" in data:
        out["team_id"] = data["TeamId"]
    if "TokenKey" in data:
        out["token_key"] = data["TokenKey"]
    if "TokenKeyId" in data:
        out["token_key_id"] = data["TokenKeyId"]
    return out
