"""Generated from Smithy shape ``com.amazonaws.eks#DescribeIdentityProviderConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.identity_provider_config_response


class DescribeIdentityProviderConfigResponse(TypedDict):
    identity_provider_config: NotRequired[
        "aws_sdk_eks.types.identity_provider_config_response.IdentityProviderConfigResponse"
    ]
    """<p>The object that represents an OpenID Connect (OIDC) identity provider configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIdentityProviderConfigResponse) -> dict:
    out: dict = {}
    if "identity_provider_config" in value:
        import aws_sdk_eks.types.identity_provider_config_response

        out["identityProviderConfig"] = (
            aws_sdk_eks.types.identity_provider_config_response.serialize_json(
                value["identity_provider_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeIdentityProviderConfigResponse:
    out: DescribeIdentityProviderConfigResponse = {}  # type: ignore[typeddict-item]
    if "identityProviderConfig" in data:
        import aws_sdk_eks.types.identity_provider_config_response

        out["identity_provider_config"] = (
            aws_sdk_eks.types.identity_provider_config_response.deserialize_json(
                data["identityProviderConfig"]
            )
        )
    return out
