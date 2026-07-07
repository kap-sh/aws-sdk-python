"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StopContinuousExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.time_stamp


class StopContinuousExportResponse(TypedDict, closed=True):
    start_time: NotRequired[
        "aws_sdk_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>Timestamp that represents when this continuous export started collecting data.</p>"""
    stop_time: NotRequired[
        "aws_sdk_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>Timestamp that represents when this continuous export was stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopContinuousExportResponse) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["startTime"] = (
            aws_sdk_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "stop_time" in value:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["stopTime"] = (
            aws_sdk_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["stop_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopContinuousExportResponse:
    out: StopContinuousExportResponse = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["start_time"] = (
            aws_sdk_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "stopTime" in data:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["stop_time"] = (
            aws_sdk_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["stopTime"]
            )
        )
    return out
