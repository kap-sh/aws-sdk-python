"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TestTransformerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.processors
    import aws_sdk_cloudwatch_logs.types.test_event_messages


class TestTransformerRequest(TypedDict, closed=True):
    transformer_config: "aws_sdk_cloudwatch_logs.types.processors.Processors"
    """<p>This structure contains the configuration of this log transformer that you want to test. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.</p>"""
    log_event_messages: (
        "aws_sdk_cloudwatch_logs.types.test_event_messages.TestEventMessages"
    )
    """<p>An array of the raw log events that you want to use to test this transformer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestTransformerRequest) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.processors

    out["transformerConfig"] = (
        aws_sdk_cloudwatch_logs.types.processors.serialize_aws_json_1_1(
            value["transformer_config"]
        )
    )
    import aws_sdk_cloudwatch_logs.types.test_event_messages

    out["logEventMessages"] = (
        aws_sdk_cloudwatch_logs.types.test_event_messages.serialize_aws_json_1_1(
            value["log_event_messages"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestTransformerRequest:
    out: TestTransformerRequest = {}  # type: ignore[typeddict-item]
    if "transformerConfig" in data:
        import aws_sdk_cloudwatch_logs.types.processors

        out["transformer_config"] = (
            aws_sdk_cloudwatch_logs.types.processors.deserialize_aws_json_1_1(
                data["transformerConfig"]
            )
        )
    else:
        raise DeserializationError("TestTransformerRequest.transformer_config required")
    if "logEventMessages" in data:
        import aws_sdk_cloudwatch_logs.types.test_event_messages

        out["log_event_messages"] = (
            aws_sdk_cloudwatch_logs.types.test_event_messages.deserialize_aws_json_1_1(
                data["logEventMessages"]
            )
        )
    else:
        raise DeserializationError("TestTransformerRequest.log_event_messages required")
    return out
