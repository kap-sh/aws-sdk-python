"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTimeData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_time_instant


class _RealTimeContactAnalysisTimeData_AbsoluteTime(TypedDict, closed=True):
    AbsoluteTime: "aws_sdk_connect.types.real_time_contact_analysis_time_instant.RealTimeContactAnalysisTimeInstant"


RealTimeContactAnalysisTimeData: TypeAlias = (
    _RealTimeContactAnalysisTimeData_AbsoluteTime
)


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisTimeData) -> dict:
    if "AbsoluteTime" in value:
        import aws_sdk_connect.types.real_time_contact_analysis_time_instant

        return {
            "AbsoluteTime": aws_sdk_connect.types.real_time_contact_analysis_time_instant.serialize_json(
                value["AbsoluteTime"]
            )
        }
    else:
        raise SerializationError("RealTimeContactAnalysisTimeData: no variant present")


def deserialize_json(data: dict) -> RealTimeContactAnalysisTimeData:
    if "AbsoluteTime" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_time_instant

        return {
            "AbsoluteTime": aws_sdk_connect.types.real_time_contact_analysis_time_instant.deserialize_json(
                data["AbsoluteTime"]
            )
        }
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisTimeData: no recognized variant key"
        )
