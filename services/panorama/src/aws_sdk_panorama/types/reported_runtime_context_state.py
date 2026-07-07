"""Generated from Smithy shape ``com.amazonaws.panorama#ReportedRuntimeContextState``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.desired_state
    import aws_sdk_panorama.types.device_reported_status
    import aws_sdk_panorama.types.runtime_context_name
    import aws_sdk_panorama.types.time_stamp


class ReportedRuntimeContextState(TypedDict, closed=True):
    desired_state: "aws_sdk_panorama.types.desired_state.DesiredState"
    """<p>The application's desired state.</p>"""
    runtime_context_name: (
        "aws_sdk_panorama.types.runtime_context_name.RuntimeContextName"
    )
    """<p>The device's name.</p>"""
    device_reported_status: (
        "aws_sdk_panorama.types.device_reported_status.DeviceReportedStatus"
    )
    """<p>The application's reported status.</p>"""
    device_reported_time: "aws_sdk_panorama.types.time_stamp.TimeStamp"
    """<p>When the device reported the application's state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportedRuntimeContextState) -> dict:
    out: dict = {}
    out["DesiredState"] = value["desired_state"]
    out["RuntimeContextName"] = value["runtime_context_name"]
    out["DeviceReportedStatus"] = value["device_reported_status"]
    import aws_sdk_panorama.types.time_stamp

    out["DeviceReportedTime"] = aws_sdk_panorama.types.time_stamp.serialize_json(
        value["device_reported_time"]
    )
    return out


def deserialize_json(data: dict) -> ReportedRuntimeContextState:
    out: ReportedRuntimeContextState = {}  # type: ignore[typeddict-item]
    if "DesiredState" in data:
        out["desired_state"] = data["DesiredState"]
    else:
        raise DeserializationError("ReportedRuntimeContextState.desired_state required")
    if "RuntimeContextName" in data:
        out["runtime_context_name"] = data["RuntimeContextName"]
    else:
        raise DeserializationError(
            "ReportedRuntimeContextState.runtime_context_name required"
        )
    if "DeviceReportedStatus" in data:
        out["device_reported_status"] = data["DeviceReportedStatus"]
    else:
        raise DeserializationError(
            "ReportedRuntimeContextState.device_reported_status required"
        )
    if "DeviceReportedTime" in data:
        import aws_sdk_panorama.types.time_stamp

        out["device_reported_time"] = (
            aws_sdk_panorama.types.time_stamp.deserialize_json(
                data["DeviceReportedTime"]
            )
        )
    else:
        raise DeserializationError(
            "ReportedRuntimeContextState.device_reported_time required"
        )
    return out
