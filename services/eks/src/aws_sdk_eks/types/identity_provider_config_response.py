"""Generated from Smithy shape ``com.amazonaws.eks#IdentityProviderConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.oidc_identity_provider_config


class IdentityProviderConfigResponse(TypedDict, closed=True):
    oidc: NotRequired[
        "aws_sdk_eks.types.oidc_identity_provider_config.OidcIdentityProviderConfig"
    ]
    """<p>An object representing an OpenID Connect (OIDC) identity provider configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderConfigResponse) -> dict:
    out: dict = {}
    if "oidc" in value:
        import aws_sdk_eks.types.oidc_identity_provider_config

        out["oidc"] = aws_sdk_eks.types.oidc_identity_provider_config.serialize_json(
            value["oidc"]
        )
    return out


def deserialize_json(data: dict) -> IdentityProviderConfigResponse:
    out: IdentityProviderConfigResponse = {}  # type: ignore[typeddict-item]
    if "oidc" in data:
        import aws_sdk_eks.types.oidc_identity_provider_config

        out["oidc"] = aws_sdk_eks.types.oidc_identity_provider_config.deserialize_json(
            data["oidc"]
        )
    return out
