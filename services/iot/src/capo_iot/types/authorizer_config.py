"""Generated from Smithy shape ``com.amazonaws.iot#AuthorizerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.allow_authorizer_override
    import capo_iot.types.authorizer_name


class AuthorizerConfig(TypedDict, closed=True):
    default_authorizer_name: NotRequired[
        "capo_iot.types.authorizer_name.AuthorizerName"
    ]
    """<p>The name of the authorization service for a domain configuration.</p>"""
    allow_authorizer_override: NotRequired[
        "capo_iot.types.allow_authorizer_override.AllowAuthorizerOverride"
    ]
    """<p>A Boolean that specifies whether the domain configuration's authorization service can be overridden.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizerConfig) -> dict:
    out: dict = {}
    if "default_authorizer_name" in value:
        out["defaultAuthorizerName"] = value["default_authorizer_name"]
    if "allow_authorizer_override" in value:
        out["allowAuthorizerOverride"] = value["allow_authorizer_override"]
    return out


def deserialize_json(data: dict) -> AuthorizerConfig:
    out: AuthorizerConfig = {}  # type: ignore[typeddict-item]
    if "defaultAuthorizerName" in data:
        out["default_authorizer_name"] = data["defaultAuthorizerName"]
    if "allowAuthorizerOverride" in data:
        out["allow_authorizer_override"] = data["allowAuthorizerOverride"]
    return out
