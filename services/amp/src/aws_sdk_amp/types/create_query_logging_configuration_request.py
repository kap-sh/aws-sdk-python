"""Generated from Smithy shape ``com.amazonaws.amp#CreateQueryLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.logging_destinations
    import aws_sdk_amp.types.workspace_id


class CreateQueryLoggingConfigurationRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace for which to create the query logging configuration.</p>"""
    destinations: "aws_sdk_amp.types.logging_destinations.LoggingDestinations"
    """<p>The destinations where query logs will be sent. Only CloudWatch Logs destination is supported. The list must contain exactly one element.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueryLoggingConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.logging_destinations

    out["destinations"] = aws_sdk_amp.types.logging_destinations.serialize_json(
        value["destinations"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateQueryLoggingConfigurationRequest:
    out: CreateQueryLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import aws_sdk_amp.types.logging_destinations

        out["destinations"] = aws_sdk_amp.types.logging_destinations.deserialize_json(
            data["destinations"]
        )
    else:
        raise DeserializationError(
            "CreateQueryLoggingConfigurationRequest.destinations required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
