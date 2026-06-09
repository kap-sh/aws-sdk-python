"""Generated from Smithy shape ``com.amazonaws.eks#DisassociateIdentityProviderConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.identity_provider_config
    import aws_sdk_eks.types.string


class DisassociateIdentityProviderConfigRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    identity_provider_config: (
        "aws_sdk_eks.types.identity_provider_config.IdentityProviderConfig"
    )
    """<p>An object representing an identity provider configuration.</p>"""
    client_request_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateIdentityProviderConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_eks.types.identity_provider_config

    out["identityProviderConfig"] = (
        aws_sdk_eks.types.identity_provider_config.serialize_json(
            value["identity_provider_config"]
        )
    )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> DisassociateIdentityProviderConfigRequest:
    out: DisassociateIdentityProviderConfigRequest = {}  # type: ignore[typeddict-item]
    if "identityProviderConfig" in data:
        import aws_sdk_eks.types.identity_provider_config

        out["identity_provider_config"] = (
            aws_sdk_eks.types.identity_provider_config.deserialize_json(
                data["identityProviderConfig"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateIdentityProviderConfigRequest.identity_provider_config required"
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
