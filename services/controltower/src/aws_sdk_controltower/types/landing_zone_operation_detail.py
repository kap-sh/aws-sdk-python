"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.landing_zone_operation_status
    import aws_sdk_controltower.types.landing_zone_operation_type
    import aws_sdk_controltower.types.operation_identifier
    import aws_sdk_controltower.types.timestamp


class LandingZoneOperationDetail(TypedDict):
    operation_type: NotRequired[
        "aws_sdk_controltower.types.landing_zone_operation_type.LandingZoneOperationType"
    ]
    """<p>The landing zone operation type. </p> <p>Valid values:</p> <ul> <li> <p> <code>DELETE</code>: The <code>DeleteLandingZone</code> operation. </p> </li> <li> <p> <code>CREATE</code>: The <code>CreateLandingZone</code> operation. </p> </li> <li> <p> <code>UPDATE</code>: The <code>UpdateLandingZone</code> operation. </p> </li> <li> <p> <code>RESET</code>: The <code>ResetLandingZone</code> operation. </p> </li> </ul>"""
    operation_identifier: NotRequired[
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    ]
    """<p>The <code>operationIdentifier</code> of the landing zone operation.</p>"""
    status: NotRequired[
        "aws_sdk_controltower.types.landing_zone_operation_status.LandingZoneOperationStatus"
    ]
    """<p>Valid values:</p> <ul> <li> <p> <code>SUCCEEDED</code>: The landing zone operation succeeded. </p> </li> <li> <p> <code>IN_PROGRESS</code>: The landing zone operation is in progress. </p> </li> <li> <p> <code>FAILED</code>: The landing zone operation failed. </p> </li> </ul>"""
    start_time: NotRequired["aws_sdk_controltower.types.timestamp.Timestamp"]
    """<p>The landing zone operation start time.</p>"""
    end_time: NotRequired["aws_sdk_controltower.types.timestamp.Timestamp"]
    """<p>The landing zone operation end time.</p>"""
    status_message: NotRequired["str"]
    """<p>If the operation result is FAILED, this string contains a message explaining why the operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneOperationDetail) -> dict:
    out: dict = {}
    if "operation_type" in value:
        import aws_sdk_controltower.types.landing_zone_operation_type

        out["operationType"] = (
            aws_sdk_controltower.types.landing_zone_operation_type.serialize_json(
                value["operation_type"]
            )
        )
    if "operation_identifier" in value:
        out["operationIdentifier"] = value["operation_identifier"]
    if "status" in value:
        import aws_sdk_controltower.types.landing_zone_operation_status

        out["status"] = (
            aws_sdk_controltower.types.landing_zone_operation_status.serialize_json(
                value["status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_controltower.types.timestamp

        out["startTime"] = aws_sdk_controltower.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_controltower.types.timestamp

        out["endTime"] = aws_sdk_controltower.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> LandingZoneOperationDetail:
    out: LandingZoneOperationDetail = {}  # type: ignore[typeddict-item]
    if "operationType" in data:
        import aws_sdk_controltower.types.landing_zone_operation_type

        out["operation_type"] = (
            aws_sdk_controltower.types.landing_zone_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    if "operationIdentifier" in data:
        out["operation_identifier"] = data["operationIdentifier"]
    if "status" in data:
        import aws_sdk_controltower.types.landing_zone_operation_status

        out["status"] = (
            aws_sdk_controltower.types.landing_zone_operation_status.deserialize_json(
                data["status"]
            )
        )
    if "startTime" in data:
        import aws_sdk_controltower.types.timestamp

        out["start_time"] = aws_sdk_controltower.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_controltower.types.timestamp

        out["end_time"] = aws_sdk_controltower.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
