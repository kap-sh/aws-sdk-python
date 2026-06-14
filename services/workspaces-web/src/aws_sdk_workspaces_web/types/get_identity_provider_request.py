"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetIdentityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.subresource_arn


class GetIdentityProviderRequest(TypedDict):
    identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN"
    """<p>The ARN of the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdentityProviderRequest:
    out: GetIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    return out
