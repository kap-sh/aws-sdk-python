"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetIdentityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.subresource_arn


class GetIdentityProviderRequest(TypedDict, closed=True):
    identity_provider_arn: "capo_workspaces_web.types.subresource_arn.SubresourceARN"
    """<p>The ARN of the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdentityProviderRequest:
    out: GetIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    return out
