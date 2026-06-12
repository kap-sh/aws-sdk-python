"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TestTransformerResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.transformed_logs


class TestTransformerResponse(TypedDict):
    transformed_logs: NotRequired[
        "aws_sdk_cloudwatch_logs.types.transformed_logs.TransformedLogs"
    ]
    """<p>An array where each member of the array includes both the original version and the transformed version of one of the log events that you input.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestTransformerResponse) -> dict:
    out: dict = {}
    if "transformed_logs" in value:
        import aws_sdk_cloudwatch_logs.types.transformed_logs

        out["transformedLogs"] = (
            aws_sdk_cloudwatch_logs.types.transformed_logs.serialize_aws_json_1_1(
                value["transformed_logs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestTransformerResponse:
    out: TestTransformerResponse = {}  # type: ignore[typeddict-item]
    if "transformedLogs" in data:
        import aws_sdk_cloudwatch_logs.types.transformed_logs

        out["transformed_logs"] = (
            aws_sdk_cloudwatch_logs.types.transformed_logs.deserialize_aws_json_1_1(
                data["transformedLogs"]
            )
        )
    return out
