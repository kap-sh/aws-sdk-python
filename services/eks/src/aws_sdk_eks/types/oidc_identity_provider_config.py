"""Generated from Smithy shape ``com.amazonaws.eks#OidcIdentityProviderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.config_status
    import aws_sdk_eks.types.required_claims_map
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.tag_map


class OidcIdentityProviderConfig(TypedDict, closed=True):
    identity_provider_config_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the configuration.</p>"""
    identity_provider_config_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ARN of the configuration.</p>"""
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of your cluster.</p>"""
    issuer_url: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The URL of the OIDC identity provider that allows the API server to discover public signing keys for verifying tokens.</p>"""
    client_id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>This is also known as <i>audience</i>. The ID of the client application that makes authentication requests to the OIDC identity provider.</p>"""
    username_claim: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The JSON Web token (JWT) claim that is used as the username.</p>"""
    username_prefix: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The prefix that is prepended to username claims to prevent clashes with existing names. The prefix can't contain <code>system:</code> </p>"""
    groups_claim: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The JSON web token (JWT) claim that the provider uses to return your groups.</p>"""
    groups_prefix: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The prefix that is prepended to group claims to prevent clashes with existing names (such as <code>system:</code> groups). For example, the value<code> oidc:</code> creates group names like <code>oidc:engineering</code> and <code>oidc:infra</code>. The prefix can't contain <code>system:</code> </p>"""
    required_claims: NotRequired[
        "aws_sdk_eks.types.required_claims_map.requiredClaimsMap"
    ]
    """<p>The key-value pairs that describe required claims in the identity token. If set, each claim is verified to be present in the token with a matching value.</p>"""
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    status: NotRequired["aws_sdk_eks.types.config_status.configStatus"]
    """<p>The status of the OIDC identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OidcIdentityProviderConfig) -> dict:
    out: dict = {}
    if "identity_provider_config_name" in value:
        out["identityProviderConfigName"] = value["identity_provider_config_name"]
    if "identity_provider_config_arn" in value:
        out["identityProviderConfigArn"] = value["identity_provider_config_arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "issuer_url" in value:
        out["issuerUrl"] = value["issuer_url"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "username_claim" in value:
        out["usernameClaim"] = value["username_claim"]
    if "username_prefix" in value:
        out["usernamePrefix"] = value["username_prefix"]
    if "groups_claim" in value:
        out["groupsClaim"] = value["groups_claim"]
    if "groups_prefix" in value:
        out["groupsPrefix"] = value["groups_prefix"]
    if "required_claims" in value:
        import aws_sdk_eks.types.required_claims_map

        out["requiredClaims"] = aws_sdk_eks.types.required_claims_map.serialize_json(
            value["required_claims"]
        )
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    if "status" in value:
        import aws_sdk_eks.types.config_status

        out["status"] = aws_sdk_eks.types.config_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> OidcIdentityProviderConfig:
    out: OidcIdentityProviderConfig = {}  # type: ignore[typeddict-item]
    if "identityProviderConfigName" in data:
        out["identity_provider_config_name"] = data["identityProviderConfigName"]
    if "identityProviderConfigArn" in data:
        out["identity_provider_config_arn"] = data["identityProviderConfigArn"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "issuerUrl" in data:
        out["issuer_url"] = data["issuerUrl"]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    if "usernameClaim" in data:
        out["username_claim"] = data["usernameClaim"]
    if "usernamePrefix" in data:
        out["username_prefix"] = data["usernamePrefix"]
    if "groupsClaim" in data:
        out["groups_claim"] = data["groupsClaim"]
    if "groupsPrefix" in data:
        out["groups_prefix"] = data["groupsPrefix"]
    if "requiredClaims" in data:
        import aws_sdk_eks.types.required_claims_map

        out["required_claims"] = aws_sdk_eks.types.required_claims_map.deserialize_json(
            data["requiredClaims"]
        )
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    if "status" in data:
        import aws_sdk_eks.types.config_status

        out["status"] = aws_sdk_eks.types.config_status.deserialize_json(data["status"])
    return out
