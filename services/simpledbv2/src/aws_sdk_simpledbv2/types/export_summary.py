"""Generated from Smithy shape ``com.amazonaws.simpledbv2#ExportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_simpledbv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_simpledbv2.types.domain_name
    import aws_sdk_simpledbv2.types.export_arn
    import aws_sdk_simpledbv2.types.export_status
    import aws_sdk_simpledbv2.types.requested_at


class ExportSummary(TypedDict, closed=True):
    export_arn: "aws_sdk_simpledbv2.types.export_arn.ExportArn"
    """Unique ARN identifier of the export."""
    export_status: "aws_sdk_simpledbv2.types.export_status.ExportStatus"
    """The current state of the export. Current possible values include : PENDING - export request received, IN_PROGRESS - export is being processed, SUCCEEDED - export completed successfully, and FAILED - export encountered an error."""
    requested_at: "aws_sdk_simpledbv2.types.requested_at.RequestedAt"
    """Timestamp when the export request was received by the service"""
    domain_name: "aws_sdk_simpledbv2.types.domain_name.DomainName"
    """The name of the domain for which the export was created."""


# --- restJson1 ser/de ---
def serialize_json(value: ExportSummary) -> dict:
    out: dict = {}
    out["exportArn"] = value["export_arn"]
    import aws_sdk_simpledbv2.types.export_status

    out["exportStatus"] = aws_sdk_simpledbv2.types.export_status.serialize_json(
        value["export_status"]
    )
    import aws_sdk_simpledbv2.types.requested_at

    out["requestedAt"] = aws_sdk_simpledbv2.types.requested_at.serialize_json(
        value["requested_at"]
    )
    out["domainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> ExportSummary:
    out: ExportSummary = {}  # type: ignore[typeddict-item]
    if "exportArn" in data:
        out["export_arn"] = data["exportArn"]
    else:
        raise DeserializationError("ExportSummary.export_arn required")
    if "exportStatus" in data:
        import aws_sdk_simpledbv2.types.export_status

        out["export_status"] = aws_sdk_simpledbv2.types.export_status.deserialize_json(
            data["exportStatus"]
        )
    else:
        raise DeserializationError("ExportSummary.export_status required")
    if "requestedAt" in data:
        import aws_sdk_simpledbv2.types.requested_at

        out["requested_at"] = aws_sdk_simpledbv2.types.requested_at.deserialize_json(
            data["requestedAt"]
        )
    else:
        raise DeserializationError("ExportSummary.requested_at required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("ExportSummary.domain_name required")
    return out
