"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#StartAccountAssociationRefreshResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.o_auth_authorization_url_output


class StartAccountAssociationRefreshResponse(TypedDict):
    o_auth_authorization_url: "aws_sdk_iot_managed_integrations.types.o_auth_authorization_url_output.OAuthAuthorizationUrlOutput"
    """<p>Third-party IoT platform OAuth authorization server URL with all required parameters to perform end-user authentication during the refresh process. This field will be empty when using General Authorization flows that do not require OAuth.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAccountAssociationRefreshResponse) -> dict:
    out: dict = {}
    out["OAuthAuthorizationUrl"] = value.get("o_auth_authorization_url", "")
    return out


def deserialize_json(data: dict) -> StartAccountAssociationRefreshResponse:
    out: StartAccountAssociationRefreshResponse = {}  # type: ignore[typeddict-item]
    if "OAuthAuthorizationUrl" in data:
        out["o_auth_authorization_url"] = data["OAuthAuthorizationUrl"]
    else:
        out["o_auth_authorization_url"] = ""
    return out
