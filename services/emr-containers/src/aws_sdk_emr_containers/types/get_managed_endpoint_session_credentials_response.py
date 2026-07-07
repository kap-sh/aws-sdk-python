"""Generated from Smithy shape ``com.amazonaws.emrcontainers#GetManagedEndpointSessionCredentialsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.credentials
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.resource_id_string


class GetManagedEndpointSessionCredentialsResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The identifier of the session token returned.</p>"""
    credentials: NotRequired["aws_sdk_emr_containers.types.credentials.Credentials"]
    """<p>The structure containing the session credentials.</p>"""
    expires_at: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time when the session token will expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedEndpointSessionCredentialsResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "credentials" in value:
        import aws_sdk_emr_containers.types.credentials

        out["credentials"] = aws_sdk_emr_containers.types.credentials.serialize_json(
            value["credentials"]
        )
    if "expires_at" in value:
        import aws_sdk_emr_containers.types.date

        out["expiresAt"] = aws_sdk_emr_containers.types.date.serialize_json(
            value["expires_at"]
        )
    return out


def deserialize_json(data: dict) -> GetManagedEndpointSessionCredentialsResponse:
    out: GetManagedEndpointSessionCredentialsResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "credentials" in data:
        import aws_sdk_emr_containers.types.credentials

        out["credentials"] = aws_sdk_emr_containers.types.credentials.deserialize_json(
            data["credentials"]
        )
    if "expiresAt" in data:
        import aws_sdk_emr_containers.types.date

        out["expires_at"] = aws_sdk_emr_containers.types.date.deserialize_json(
            data["expiresAt"]
        )
    return out
