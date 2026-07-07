"""Generated from Smithy shape ``com.amazonaws.eks#ListIdentityProviderConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.identity_provider_configs
    import aws_sdk_eks.types.string


class ListIdentityProviderConfigsResponse(TypedDict, closed=True):
    identity_provider_configs: NotRequired[
        "aws_sdk_eks.types.identity_provider_configs.IdentityProviderConfigs"
    ]
    """<p>The identity provider configurations for the cluster.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListIdentityProviderConfigsResponse</code> request. When the results of a <code>ListIdentityProviderConfigsResponse</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityProviderConfigsResponse) -> dict:
    out: dict = {}
    if "identity_provider_configs" in value:
        import aws_sdk_eks.types.identity_provider_configs

        out["identityProviderConfigs"] = (
            aws_sdk_eks.types.identity_provider_configs.serialize_json(
                value["identity_provider_configs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdentityProviderConfigsResponse:
    out: ListIdentityProviderConfigsResponse = {}  # type: ignore[typeddict-item]
    if "identityProviderConfigs" in data:
        import aws_sdk_eks.types.identity_provider_configs

        out["identity_provider_configs"] = (
            aws_sdk_eks.types.identity_provider_configs.deserialize_json(
                data["identityProviderConfigs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
