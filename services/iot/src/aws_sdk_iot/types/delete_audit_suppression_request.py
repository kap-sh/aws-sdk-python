"""Generated from Smithy shape ``com.amazonaws.iot#DeleteAuditSuppressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_name
    import aws_sdk_iot.types.resource_identifier


class DeleteAuditSuppressionRequest(TypedDict, closed=True):
    check_name: "aws_sdk_iot.types.audit_check_name.AuditCheckName"
    resource_identifier: "aws_sdk_iot.types.resource_identifier.ResourceIdentifier"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAuditSuppressionRequest) -> dict:
    out: dict = {}
    out["checkName"] = value["check_name"]
    import aws_sdk_iot.types.resource_identifier

    out["resourceIdentifier"] = aws_sdk_iot.types.resource_identifier.serialize_json(
        value["resource_identifier"]
    )
    return out


def deserialize_json(data: dict) -> DeleteAuditSuppressionRequest:
    out: DeleteAuditSuppressionRequest = {}  # type: ignore[typeddict-item]
    if "checkName" in data:
        out["check_name"] = data["checkName"]
    else:
        raise DeserializationError("DeleteAuditSuppressionRequest.check_name required")
    if "resourceIdentifier" in data:
        import aws_sdk_iot.types.resource_identifier

        out["resource_identifier"] = (
            aws_sdk_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAuditSuppressionRequest.resource_identifier required"
        )
    return out
