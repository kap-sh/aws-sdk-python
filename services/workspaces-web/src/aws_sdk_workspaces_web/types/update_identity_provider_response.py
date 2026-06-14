"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateIdentityProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.identity_provider


class UpdateIdentityProviderResponse(TypedDict):
    identity_provider: "aws_sdk_workspaces_web.types.identity_provider.IdentityProvider"
    """<p>The identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdentityProviderResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_web.types.identity_provider

    out["identityProvider"] = (
        aws_sdk_workspaces_web.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIdentityProviderResponse:
    out: UpdateIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if "identityProvider" in data:
        import aws_sdk_workspaces_web.types.identity_provider

        out["identity_provider"] = (
            aws_sdk_workspaces_web.types.identity_provider.deserialize_json(
                data["identityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIdentityProviderResponse.identity_provider required"
        )
    return out
