"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetPositionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.accuracy
    import capo_iot_wireless.types.iso_date_time_string
    import capo_iot_wireless.types.position_coordinate
    import capo_iot_wireless.types.position_solver_provider
    import capo_iot_wireless.types.position_solver_type
    import capo_iot_wireless.types.position_solver_version


class GetPositionResponse(TypedDict, closed=True):
    position: NotRequired[
        "capo_iot_wireless.types.position_coordinate.PositionCoordinate"
    ]
    """<p>The position information of the resource.</p>"""
    accuracy: NotRequired["capo_iot_wireless.types.accuracy.Accuracy"]
    """<p>The accuracy of the estimated position in meters. An empty value indicates that no position data is available. A value of ‘0.0’ value indicates that position data is available. This data corresponds to the position information that you specified instead of the position computed by solver.</p>"""
    solver_type: NotRequired[
        "capo_iot_wireless.types.position_solver_type.PositionSolverType"
    ]
    """<p>The type of solver used to identify the position of the resource.</p>"""
    solver_provider: NotRequired[
        "capo_iot_wireless.types.position_solver_provider.PositionSolverProvider"
    ]
    """<p>The vendor of the positioning solver.</p>"""
    solver_version: NotRequired[
        "capo_iot_wireless.types.position_solver_version.PositionSolverVersion"
    ]
    """<p>The version of the positioning solver.</p>"""
    timestamp: NotRequired[
        "capo_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The timestamp at which the device's position was determined.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPositionResponse) -> dict:
    out: dict = {}
    if "position" in value:
        import capo_iot_wireless.types.position_coordinate

        out["Position"] = capo_iot_wireless.types.position_coordinate.serialize_json(
            value["position"]
        )
    if "accuracy" in value:
        import capo_iot_wireless.types.accuracy

        out["Accuracy"] = capo_iot_wireless.types.accuracy.serialize_json(
            value["accuracy"]
        )
    if "solver_type" in value:
        import capo_iot_wireless.types.position_solver_type

        out["SolverType"] = capo_iot_wireless.types.position_solver_type.serialize_json(
            value["solver_type"]
        )
    if "solver_provider" in value:
        import capo_iot_wireless.types.position_solver_provider

        out["SolverProvider"] = (
            capo_iot_wireless.types.position_solver_provider.serialize_json(
                value["solver_provider"]
            )
        )
    if "solver_version" in value:
        out["SolverVersion"] = value["solver_version"]
    if "timestamp" in value:
        out["Timestamp"] = value["timestamp"]
    return out


def deserialize_json(data: dict) -> GetPositionResponse:
    out: GetPositionResponse = {}  # type: ignore[typeddict-item]
    if "Position" in data:
        import capo_iot_wireless.types.position_coordinate

        out["position"] = capo_iot_wireless.types.position_coordinate.deserialize_json(
            data["Position"]
        )
    if "Accuracy" in data:
        import capo_iot_wireless.types.accuracy

        out["accuracy"] = capo_iot_wireless.types.accuracy.deserialize_json(
            data["Accuracy"]
        )
    if "SolverType" in data:
        import capo_iot_wireless.types.position_solver_type

        out["solver_type"] = (
            capo_iot_wireless.types.position_solver_type.deserialize_json(
                data["SolverType"]
            )
        )
    if "SolverProvider" in data:
        import capo_iot_wireless.types.position_solver_provider

        out["solver_provider"] = (
            capo_iot_wireless.types.position_solver_provider.deserialize_json(
                data["SolverProvider"]
            )
        )
    if "SolverVersion" in data:
        out["solver_version"] = data["SolverVersion"]
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    return out
