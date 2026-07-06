"""Generated from Smithy shape ``com.amazonaws.iot#UpdateAuditSuppressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_name
    import aws_sdk_iot.types.audit_description
    import aws_sdk_iot.types.resource_identifier
    import aws_sdk_iot.types.suppress_indefinitely
    import aws_sdk_iot.types.timestamp


class UpdateAuditSuppressionRequest(TypedDict, closed=True):
    check_name: "aws_sdk_iot.types.audit_check_name.AuditCheckName"
    resource_identifier: "aws_sdk_iot.types.resource_identifier.ResourceIdentifier"
    expiration_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The expiration date (epoch timestamp in seconds) that you want the suppression to adhere to. </p>"""
    suppress_indefinitely: NotRequired[
        "aws_sdk_iot.types.suppress_indefinitely.SuppressIndefinitely"
    ]
    """<p> Indicates whether a suppression should exist indefinitely or not. </p>"""
    description: NotRequired["aws_sdk_iot.types.audit_description.AuditDescription"]
    """<p> The description of the audit suppression. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAuditSuppressionRequest) -> dict:
    out: dict = {}
    out["checkName"] = value["check_name"]
    import aws_sdk_iot.types.resource_identifier

    out["resourceIdentifier"] = aws_sdk_iot.types.resource_identifier.serialize_json(
        value["resource_identifier"]
    )
    if "expiration_date" in value:
        import aws_sdk_iot.types.timestamp

        out["expirationDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["expiration_date"]
        )
    if "suppress_indefinitely" in value:
        out["suppressIndefinitely"] = value["suppress_indefinitely"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAuditSuppressionRequest:
    out: UpdateAuditSuppressionRequest = {}  # type: ignore[typeddict-item]
    if "checkName" in data:
        out["check_name"] = data["checkName"]
    else:
        raise DeserializationError("UpdateAuditSuppressionRequest.check_name required")
    if "resourceIdentifier" in data:
        import aws_sdk_iot.types.resource_identifier

        out["resource_identifier"] = (
            aws_sdk_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAuditSuppressionRequest.resource_identifier required"
        )
    if "expirationDate" in data:
        import aws_sdk_iot.types.timestamp

        out["expiration_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["expirationDate"]
        )
    if "suppressIndefinitely" in data:
        out["suppress_indefinitely"] = data["suppressIndefinitely"]
    if "description" in data:
        out["description"] = data["description"]
    return out
