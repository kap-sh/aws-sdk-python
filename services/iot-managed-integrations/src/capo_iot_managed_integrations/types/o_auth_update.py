"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OAuthUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.proactive_refresh_token_renewal


class OAuthUpdate(TypedDict, closed=True):
    o_auth_complete_redirect_url: NotRequired["str"]
    """<p>The updated URL where users are redirected after completing the OAuth authorization process.</p>"""
    proactive_refresh_token_renewal: NotRequired[
        "capo_iot_managed_integrations.types.proactive_refresh_token_renewal.ProactiveRefreshTokenRenewal"
    ]
    """<p>Updated configuration for proactively refreshing OAuth tokens before they expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthUpdate) -> dict:
    out: dict = {}
    if "o_auth_complete_redirect_url" in value:
        out["oAuthCompleteRedirectUrl"] = value["o_auth_complete_redirect_url"]
    if "proactive_refresh_token_renewal" in value:
        import capo_iot_managed_integrations.types.proactive_refresh_token_renewal

        out["proactiveRefreshTokenRenewal"] = (
            capo_iot_managed_integrations.types.proactive_refresh_token_renewal.serialize_json(
                value["proactive_refresh_token_renewal"]
            )
        )
    return out


def deserialize_json(data: dict) -> OAuthUpdate:
    out: OAuthUpdate = {}  # type: ignore[typeddict-item]
    if "oAuthCompleteRedirectUrl" in data:
        out["o_auth_complete_redirect_url"] = data["oAuthCompleteRedirectUrl"]
    if "proactiveRefreshTokenRenewal" in data:
        import capo_iot_managed_integrations.types.proactive_refresh_token_renewal

        out["proactive_refresh_token_renewal"] = (
            capo_iot_managed_integrations.types.proactive_refresh_token_renewal.deserialize_json(
                data["proactiveRefreshTokenRenewal"]
            )
        )
    return out
