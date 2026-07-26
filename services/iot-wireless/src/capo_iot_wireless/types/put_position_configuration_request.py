"""Generated from Smithy shape ``com.amazonaws.iotwireless#PutPositionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.position_resource_identifier
    import capo_iot_wireless.types.position_resource_type
    import capo_iot_wireless.types.position_solver_configurations


class PutPositionConfigurationRequest(TypedDict, closed=True):
    resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier"
    """<p>Resource identifier used to update the position configuration.</p>"""
    resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType"
    """<p>Resource type of the resource for which you want to update the position configuration.</p>"""
    solvers: NotRequired[
        "capo_iot_wireless.types.position_solver_configurations.PositionSolverConfigurations"
    ]
    """<p>The positioning solvers used to update the position configuration of the resource.</p>"""
    destination: NotRequired["capo_iot_wireless.types.destination_name.DestinationName"]
    """<p>The position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPositionConfigurationRequest) -> dict:
    out: dict = {}
    if "solvers" in value:
        import capo_iot_wireless.types.position_solver_configurations

        out["Solvers"] = (
            capo_iot_wireless.types.position_solver_configurations.serialize_json(
                value["solvers"]
            )
        )
    if "destination" in value:
        out["Destination"] = value["destination"]
    return out


def deserialize_json(data: dict) -> PutPositionConfigurationRequest:
    out: PutPositionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "Solvers" in data:
        import capo_iot_wireless.types.position_solver_configurations

        out["solvers"] = (
            capo_iot_wireless.types.position_solver_configurations.deserialize_json(
                data["Solvers"]
            )
        )
    if "Destination" in data:
        out["destination"] = data["Destination"]
    return out
