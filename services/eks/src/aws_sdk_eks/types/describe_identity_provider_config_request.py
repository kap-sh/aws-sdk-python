"""Generated from Smithy shape ``com.amazonaws.eks#DescribeIdentityProviderConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.identity_provider_config
    import aws_sdk_eks.types.string


class DescribeIdentityProviderConfigRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    identity_provider_config: (
        "aws_sdk_eks.types.identity_provider_config.IdentityProviderConfig"
    )
    """<p>An object representing an identity provider configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIdentityProviderConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_eks.types.identity_provider_config

    out["identityProviderConfig"] = (
        aws_sdk_eks.types.identity_provider_config.serialize_json(
            value["identity_provider_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeIdentityProviderConfigRequest:
    out: DescribeIdentityProviderConfigRequest = {}  # type: ignore[typeddict-item]
    if "identityProviderConfig" in data:
        import aws_sdk_eks.types.identity_provider_config

        out["identity_provider_config"] = (
            aws_sdk_eks.types.identity_provider_config.deserialize_json(
                data["identityProviderConfig"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeIdentityProviderConfigRequest.identity_provider_config required"
        )
    return out
