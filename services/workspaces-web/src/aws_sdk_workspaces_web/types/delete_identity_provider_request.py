"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteIdentityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.subresource_arn


class DeleteIdentityProviderRequest(TypedDict):
    identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN"
    """<p>The ARN of the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdentityProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIdentityProviderRequest:
    out: DeleteIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    return out
