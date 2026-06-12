"""Generated from Smithy shape ``com.amazonaws.forecast#TestWindowDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.test_window_summary

TestWindowDetails: TypeAlias = list[
    "aws_sdk_forecast.types.test_window_summary.TestWindowSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestWindowDetails) -> list:
    import aws_sdk_forecast.types.test_window_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.test_window_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TestWindowDetails:
    import aws_sdk_forecast.types.test_window_summary

    out: TestWindowDetails = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.test_window_summary.deserialize_aws_json_1_1(item)
        )
    return out
