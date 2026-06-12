"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionConfigurationItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.position_resource_identifier
    import aws_sdk_iot_wireless.types.position_resource_type
    import aws_sdk_iot_wireless.types.position_solver_details


class PositionConfigurationItem(TypedDict):
    resource_identifier: NotRequired[
        "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier"
    ]
    """<p>Resource identifier for the position configuration.</p>"""
    resource_type: NotRequired[
        "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType"
    ]
    """<p>Resource type of the resource for the position configuration.</p>"""
    solvers: NotRequired[
        "aws_sdk_iot_wireless.types.position_solver_details.PositionSolverDetails"
    ]
    """<p>The details of the positioning solver object used to compute the location.</p>"""
    destination: NotRequired[
        "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PositionConfigurationItem) -> dict:
    out: dict = {}
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "resource_type" in value:
        import aws_sdk_iot_wireless.types.position_resource_type

        out["ResourceType"] = (
            aws_sdk_iot_wireless.types.position_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "solvers" in value:
        import aws_sdk_iot_wireless.types.position_solver_details

        out["Solvers"] = (
            aws_sdk_iot_wireless.types.position_solver_details.serialize_json(
                value["solvers"]
            )
        )
    if "destination" in value:
        out["Destination"] = value["destination"]
    return out


def deserialize_json(data: dict) -> PositionConfigurationItem:
    out: PositionConfigurationItem = {}  # type: ignore[typeddict-item]
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if "ResourceType" in data:
        import aws_sdk_iot_wireless.types.position_resource_type

        out["resource_type"] = (
            aws_sdk_iot_wireless.types.position_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if "Solvers" in data:
        import aws_sdk_iot_wireless.types.position_solver_details

        out["solvers"] = (
            aws_sdk_iot_wireless.types.position_solver_details.deserialize_json(
                data["Solvers"]
            )
        )
    if "Destination" in data:
        out["destination"] = data["Destination"]
    return out
