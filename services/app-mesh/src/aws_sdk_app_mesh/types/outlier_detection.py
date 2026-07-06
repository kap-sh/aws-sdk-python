"""Generated from Smithy shape ``com.amazonaws.appmesh#OutlierDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.duration
    import aws_sdk_app_mesh.types.outlier_detection_max_ejection_percent
    import aws_sdk_app_mesh.types.outlier_detection_max_server_errors


class OutlierDetection(TypedDict, closed=True):
    max_server_errors: "aws_sdk_app_mesh.types.outlier_detection_max_server_errors.OutlierDetectionMaxServerErrors"
    """<p>Number of consecutive <code>5xx</code> errors required for ejection. </p>"""
    interval: "aws_sdk_app_mesh.types.duration.Duration"
    """<p>The time interval between ejection sweep analysis.</p>"""
    base_ejection_duration: "aws_sdk_app_mesh.types.duration.Duration"
    """<p>The base amount of time for which a host is ejected.</p>"""
    max_ejection_percent: "aws_sdk_app_mesh.types.outlier_detection_max_ejection_percent.OutlierDetectionMaxEjectionPercent"
    """<p>Maximum percentage of hosts in load balancing pool for upstream service that can be ejected. Will eject at least one host regardless of the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutlierDetection) -> dict:
    out: dict = {}
    out["maxServerErrors"] = value["max_server_errors"]
    import aws_sdk_app_mesh.types.duration

    out["interval"] = aws_sdk_app_mesh.types.duration.serialize_json(value["interval"])
    import aws_sdk_app_mesh.types.duration

    out["baseEjectionDuration"] = aws_sdk_app_mesh.types.duration.serialize_json(
        value["base_ejection_duration"]
    )
    out["maxEjectionPercent"] = value["max_ejection_percent"]
    return out


def deserialize_json(data: dict) -> OutlierDetection:
    out: OutlierDetection = {}  # type: ignore[typeddict-item]
    if "maxServerErrors" in data:
        out["max_server_errors"] = data["maxServerErrors"]
    else:
        raise DeserializationError("OutlierDetection.max_server_errors required")
    if "interval" in data:
        import aws_sdk_app_mesh.types.duration

        out["interval"] = aws_sdk_app_mesh.types.duration.deserialize_json(
            data["interval"]
        )
    else:
        raise DeserializationError("OutlierDetection.interval required")
    if "baseEjectionDuration" in data:
        import aws_sdk_app_mesh.types.duration

        out["base_ejection_duration"] = (
            aws_sdk_app_mesh.types.duration.deserialize_json(
                data["baseEjectionDuration"]
            )
        )
    else:
        raise DeserializationError("OutlierDetection.base_ejection_duration required")
    if "maxEjectionPercent" in data:
        out["max_ejection_percent"] = data["maxEjectionPercent"]
    else:
        raise DeserializationError("OutlierDetection.max_ejection_percent required")
    return out
