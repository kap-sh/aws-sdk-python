"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IdentityProviderSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.identity_provider_name
    import aws_sdk_workspaces_web.types.identity_provider_type
    import aws_sdk_workspaces_web.types.subresource_arn


class IdentityProviderSummary(TypedDict):
    identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN"
    """<p>The ARN of the identity provider.</p>"""
    identity_provider_name: NotRequired[
        "aws_sdk_workspaces_web.types.identity_provider_name.IdentityProviderName"
    ]
    """<p>The identity provider name.</p>"""
    identity_provider_type: NotRequired[
        "aws_sdk_workspaces_web.types.identity_provider_type.IdentityProviderType"
    ]
    """<p>The identity provider type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderSummary) -> dict:
    out: dict = {}
    out["identityProviderArn"] = value["identity_provider_arn"]
    if "identity_provider_name" in value:
        out["identityProviderName"] = value["identity_provider_name"]
    if "identity_provider_type" in value:
        out["identityProviderType"] = value["identity_provider_type"]
    return out


def deserialize_json(data: dict) -> IdentityProviderSummary:
    out: IdentityProviderSummary = {}  # type: ignore[typeddict-item]
    if "identityProviderArn" in data:
        out["identity_provider_arn"] = data["identityProviderArn"]
    else:
        raise DeserializationError(
            "IdentityProviderSummary.identity_provider_arn required"
        )
    if "identityProviderName" in data:
        out["identity_provider_name"] = data["identityProviderName"]
    if "identityProviderType" in data:
        out["identity_provider_type"] = data["identityProviderType"]
    return out
