"""Generated from Smithy shape ``com.amazonaws.eks#AssociateIdentityProviderConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.oidc_identity_provider_config_request
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.tag_map


class AssociateIdentityProviderConfigRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    oidc: "aws_sdk_eks.types.oidc_identity_provider_config_request.OidcIdentityProviderConfigRequest"
    """<p>An object representing an OpenID Connect (OIDC) identity provider configuration.</p>"""
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    client_request_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateIdentityProviderConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_eks.types.oidc_identity_provider_config_request

    out["oidc"] = (
        aws_sdk_eks.types.oidc_identity_provider_config_request.serialize_json(
            value["oidc"]
        )
    )
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> AssociateIdentityProviderConfigRequest:
    out: AssociateIdentityProviderConfigRequest = {}  # type: ignore[typeddict-item]
    if "oidc" in data:
        import aws_sdk_eks.types.oidc_identity_provider_config_request

        out["oidc"] = (
            aws_sdk_eks.types.oidc_identity_provider_config_request.deserialize_json(
                data["oidc"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateIdentityProviderConfigRequest.oidc required"
        )
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
