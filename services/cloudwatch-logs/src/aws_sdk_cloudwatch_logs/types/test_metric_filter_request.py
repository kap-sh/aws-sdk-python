"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TestMetricFilterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.filter_pattern
    import aws_sdk_cloudwatch_logs.types.test_event_messages


class TestMetricFilterRequest(TypedDict):
    filter_pattern: "aws_sdk_cloudwatch_logs.types.filter_pattern.FilterPattern"
    log_event_messages: (
        "aws_sdk_cloudwatch_logs.types.test_event_messages.TestEventMessages"
    )
    """<p>The log event messages to test.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestMetricFilterRequest) -> dict:
    out: dict = {}
    out["filterPattern"] = value["filter_pattern"]
    import aws_sdk_cloudwatch_logs.types.test_event_messages

    out["logEventMessages"] = (
        aws_sdk_cloudwatch_logs.types.test_event_messages.serialize_aws_json_1_1(
            value["log_event_messages"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestMetricFilterRequest:
    out: TestMetricFilterRequest = {}  # type: ignore[typeddict-item]
    if "filterPattern" in data:
        out["filter_pattern"] = data["filterPattern"]
    else:
        raise DeserializationError("TestMetricFilterRequest.filter_pattern required")
    if "logEventMessages" in data:
        import aws_sdk_cloudwatch_logs.types.test_event_messages

        out["log_event_messages"] = (
            aws_sdk_cloudwatch_logs.types.test_event_messages.deserialize_aws_json_1_1(
                data["logEventMessages"]
            )
        )
    else:
        raise DeserializationError(
            "TestMetricFilterRequest.log_event_messages required"
        )
    return out
