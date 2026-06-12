"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuditSuppressionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_name
    import aws_sdk_iot.types.audit_description
    import aws_sdk_iot.types.resource_identifier
    import aws_sdk_iot.types.suppress_indefinitely
    import aws_sdk_iot.types.timestamp


class DescribeAuditSuppressionResponse(TypedDict):
    check_name: NotRequired["aws_sdk_iot.types.audit_check_name.AuditCheckName"]
    resource_identifier: NotRequired[
        "aws_sdk_iot.types.resource_identifier.ResourceIdentifier"
    ]
    expiration_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The epoch timestamp in seconds at which this suppression expires. </p>"""
    suppress_indefinitely: NotRequired[
        "aws_sdk_iot.types.suppress_indefinitely.SuppressIndefinitely"
    ]
    """<p> Indicates whether a suppression should exist indefinitely or not. </p>"""
    description: NotRequired["aws_sdk_iot.types.audit_description.AuditDescription"]
    """<p> The description of the audit suppression. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuditSuppressionResponse) -> dict:
    out: dict = {}
    if "check_name" in value:
        out["checkName"] = value["check_name"]
    if "resource_identifier" in value:
        import aws_sdk_iot.types.resource_identifier

        out["resourceIdentifier"] = (
            aws_sdk_iot.types.resource_identifier.serialize_json(
                value["resource_identifier"]
            )
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


def deserialize_json(data: dict) -> DescribeAuditSuppressionResponse:
    out: DescribeAuditSuppressionResponse = {}  # type: ignore[typeddict-item]
    if "checkName" in data:
        out["check_name"] = data["checkName"]
    if "resourceIdentifier" in data:
        import aws_sdk_iot.types.resource_identifier

        out["resource_identifier"] = (
            aws_sdk_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
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
