"""Generated from Smithy shape ``com.amazonaws.forecast#TestWindows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.window_summary

TestWindows: TypeAlias = list["aws_sdk_forecast.types.window_summary.WindowSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestWindows) -> list:
    import aws_sdk_forecast.types.window_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_forecast.types.window_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TestWindows:
    import aws_sdk_forecast.types.window_summary

    out: TestWindows = []
    for item in data:
        out.append(aws_sdk_forecast.types.window_summary.deserialize_aws_json_1_1(item))
    return out
