"""Generated from Smithy shape ``com.amazonaws.simpledbv2#StartDomainExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_simpledbv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_simpledbv2.types.export_arn
    import aws_sdk_simpledbv2.types.idempotency_token
    import aws_sdk_simpledbv2.types.requested_at


class StartDomainExportResponse(TypedDict, closed=True):
    client_token: "aws_sdk_simpledbv2.types.idempotency_token.IdempotencyToken"
    """The client token that was provided in the request."""
    export_arn: "aws_sdk_simpledbv2.types.export_arn.ExportArn"
    """Unique ARN identifier of the export."""
    requested_at: "aws_sdk_simpledbv2.types.requested_at.RequestedAt"
    """Timestamp when the export request was received by the service."""


# --- restJson1 ser/de ---
def serialize_json(value: StartDomainExportResponse) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["exportArn"] = value["export_arn"]
    import aws_sdk_simpledbv2.types.requested_at

    out["requestedAt"] = aws_sdk_simpledbv2.types.requested_at.serialize_json(
        value["requested_at"]
    )
    return out


def deserialize_json(data: dict) -> StartDomainExportResponse:
    out: StartDomainExportResponse = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("StartDomainExportResponse.client_token required")
    if "exportArn" in data:
        out["export_arn"] = data["exportArn"]
    else:
        raise DeserializationError("StartDomainExportResponse.export_arn required")
    if "requestedAt" in data:
        import aws_sdk_simpledbv2.types.requested_at

        out["requested_at"] = aws_sdk_simpledbv2.types.requested_at.deserialize_json(
            data["requestedAt"]
        )
    else:
        raise DeserializationError("StartDomainExportResponse.requested_at required")
    return out
