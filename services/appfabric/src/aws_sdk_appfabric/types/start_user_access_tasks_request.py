"""Generated from Smithy shape ``com.amazonaws.appfabric#StartUserAccessTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.email
    import aws_sdk_appfabric.types.identifier


class StartUserAccessTasksRequest(TypedDict):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    email: "aws_sdk_appfabric.types.email.Email"
    """<p>The email address of the target user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartUserAccessTasksRequest) -> dict:
    out: dict = {}
    out["appBundleIdentifier"] = value["app_bundle_identifier"]
    out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> StartUserAccessTasksRequest:
    out: StartUserAccessTasksRequest = {}  # type: ignore[typeddict-item]
    if "appBundleIdentifier" in data:
        out["app_bundle_identifier"] = data["appBundleIdentifier"]
    else:
        raise DeserializationError(
            "StartUserAccessTasksRequest.app_bundle_identifier required"
        )
    if "email" in data:
        out["email"] = data["email"]
    else:
        raise DeserializationError("StartUserAccessTasksRequest.email required")
    return out
