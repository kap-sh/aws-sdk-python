"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controltower.types.landing_zone_operation_status
    import aws_sdk_controltower.types.landing_zone_operation_type
    import aws_sdk_controltower.types.operation_identifier


class LandingZoneOperationSummary(TypedDict, closed=True):
    operation_type: NotRequired[
        "aws_sdk_controltower.types.landing_zone_operation_type.LandingZoneOperationType"
    ]
    """<p>The type of the landing zone operation.</p>"""
    operation_identifier: NotRequired[
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    ]
    """<p>The <code>operationIdentifier</code> of the landing zone operation.</p>"""
    status: NotRequired[
        "aws_sdk_controltower.types.landing_zone_operation_status.LandingZoneOperationStatus"
    ]
    """<p>The status of the landing zone operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneOperationSummary) -> dict:
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
    return out


def deserialize_json(data: dict) -> LandingZoneOperationSummary:
    out: LandingZoneOperationSummary = {}  # type: ignore[typeddict-item]
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
    return out
