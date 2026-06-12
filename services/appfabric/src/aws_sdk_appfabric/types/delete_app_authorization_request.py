"""Generated from Smithy shape ``com.amazonaws.appfabric#DeleteAppAuthorizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.identifier


class DeleteAppAuthorizationRequest(TypedDict):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    app_authorization_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppAuthorizationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppAuthorizationRequest:
    out: DeleteAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
    return out
