"""Generated from Smithy shape ``com.amazonaws.eks#DescribeIdentityProviderConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.identity_provider_config_response


class DescribeIdentityProviderConfigResponse(TypedDict, closed=True):
    identity_provider_config: NotRequired[
        "capo_eks.types.identity_provider_config_response.IdentityProviderConfigResponse"
    ]
    """<p>The object that represents an OpenID Connect (OIDC) identity provider configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIdentityProviderConfigResponse) -> dict:
    out: dict = {}
    if "identity_provider_config" in value:
        import capo_eks.types.identity_provider_config_response

        out["identityProviderConfig"] = (
            capo_eks.types.identity_provider_config_response.serialize_json(
                value["identity_provider_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeIdentityProviderConfigResponse:
    out: DescribeIdentityProviderConfigResponse = {}  # type: ignore[typeddict-item]
    if "identityProviderConfig" in data:
        import capo_eks.types.identity_provider_config_response

        out["identity_provider_config"] = (
            capo_eks.types.identity_provider_config_response.deserialize_json(
                data["identityProviderConfig"]
            )
        )
    return out
