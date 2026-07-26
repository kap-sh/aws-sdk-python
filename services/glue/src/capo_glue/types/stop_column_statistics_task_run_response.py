"""Generated from Smithy shape ``com.amazonaws.glue#StopColumnStatisticsTaskRunResponse``."""

from typing_extensions import TypedDict


class StopColumnStatisticsTaskRunResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopColumnStatisticsTaskRunResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopColumnStatisticsTaskRunResponse:
    out: StopColumnStatisticsTaskRunResponse = {}  # type: ignore[typeddict-item]
    return out
