"""Generated from Smithy shape ``com.amazonaws.appfabric#UpdateAppAuthorizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.credential
    import aws_sdk_appfabric.types.identifier
    import aws_sdk_appfabric.types.tenant


class UpdateAppAuthorizationRequest(TypedDict):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    app_authorization_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.</p>"""
    credential: NotRequired["aws_sdk_appfabric.types.credential.Credential"]
    """<p>Contains credentials for the application, such as an API key or OAuth2 client ID and secret.</p> <p>Specify credentials that match the authorization type of the app authorization to update. For example, if the authorization type of the app authorization is OAuth2 (<code>oauth2</code>), then you should provide only the OAuth2 credentials.</p>"""
    tenant: NotRequired["aws_sdk_appfabric.types.tenant.Tenant"]
    """<p>Contains information about an application tenant, such as the application display name and identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppAuthorizationRequest) -> dict:
    out: dict = {}
    if "credential" in value:
        import aws_sdk_appfabric.types.credential

        out["credential"] = aws_sdk_appfabric.types.credential.serialize_json(
            value["credential"]
        )
    if "tenant" in value:
        import aws_sdk_appfabric.types.tenant

        out["tenant"] = aws_sdk_appfabric.types.tenant.serialize_json(value["tenant"])
    return out


def deserialize_json(data: dict) -> UpdateAppAuthorizationRequest:
    out: UpdateAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if "credential" in data:
        import aws_sdk_appfabric.types.credential

        out["credential"] = aws_sdk_appfabric.types.credential.deserialize_json(
            data["credential"]
        )
    if "tenant" in data:
        import aws_sdk_appfabric.types.tenant

        out["tenant"] = aws_sdk_appfabric.types.tenant.deserialize_json(data["tenant"])
    return out
