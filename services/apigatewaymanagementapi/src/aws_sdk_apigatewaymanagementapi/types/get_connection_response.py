"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#GetConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601
    import aws_sdk_apigatewaymanagementapi.types.identity


class GetConnectionResponse(TypedDict):
    connected_at: NotRequired[
        "aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time in ISO 8601 format for when the connection was established.</p>"""
    identity: NotRequired["aws_sdk_apigatewaymanagementapi.types.identity.Identity"]
    last_active_at: NotRequired[
        "aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time in ISO 8601 format for when the connection was last active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionResponse) -> dict:
    out: dict = {}
    if "connected_at" in value:
        import aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601

        out["connectedAt"] = (
            aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601.serialize_json(
                value["connected_at"]
            )
        )
    if "identity" in value:
        import aws_sdk_apigatewaymanagementapi.types.identity

        out["identity"] = aws_sdk_apigatewaymanagementapi.types.identity.serialize_json(
            value["identity"]
        )
    if "last_active_at" in value:
        import aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601

        out["lastActiveAt"] = (
            aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601.serialize_json(
                value["last_active_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConnectionResponse:
    out: GetConnectionResponse = {}  # type: ignore[typeddict-item]
    if "connectedAt" in data:
        import aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601

        out["connected_at"] = (
            aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601.deserialize_json(
                data["connectedAt"]
            )
        )
    if "identity" in data:
        import aws_sdk_apigatewaymanagementapi.types.identity

        out["identity"] = (
            aws_sdk_apigatewaymanagementapi.types.identity.deserialize_json(
                data["identity"]
            )
        )
    if "lastActiveAt" in data:
        import aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601

        out["last_active_at"] = (
            aws_sdk_apigatewaymanagementapi.types.__timestamp_iso8601.deserialize_json(
                data["lastActiveAt"]
            )
        )
    return out
