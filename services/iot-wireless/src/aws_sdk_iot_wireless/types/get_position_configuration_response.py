"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetPositionConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.position_solver_details


class GetPositionConfigurationResponse(TypedDict):
    solvers: NotRequired[
        "aws_sdk_iot_wireless.types.position_solver_details.PositionSolverDetails"
    ]
    """<p>The wrapper for the solver configuration details object.</p>"""
    destination: NotRequired[
        "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPositionConfigurationResponse) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> GetPositionConfigurationResponse:
    out: GetPositionConfigurationResponse = {}  # type: ignore[typeddict-item]
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
