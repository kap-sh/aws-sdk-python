"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetIdentityProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.identity_provider


class GetIdentityProviderResponse(TypedDict):
    identity_provider: NotRequired[
        "aws_sdk_workspaces_web.types.identity_provider.IdentityProvider"
    ]
    """<p>The identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityProviderResponse) -> dict:
    out: dict = {}
    if "identity_provider" in value:
        import aws_sdk_workspaces_web.types.identity_provider

        out["identityProvider"] = (
            aws_sdk_workspaces_web.types.identity_provider.serialize_json(
                value["identity_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetIdentityProviderResponse:
    out: GetIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if "identityProvider" in data:
        import aws_sdk_workspaces_web.types.identity_provider

        out["identity_provider"] = (
            aws_sdk_workspaces_web.types.identity_provider.deserialize_json(
                data["identityProvider"]
            )
        )
    return out
