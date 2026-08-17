"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TestTransformerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.transformed_logs


class TestTransformerResponse(TypedDict, closed=True):
    transformed_logs: NotRequired[
        "capo_cloudwatch_logs.types.transformed_logs.TransformedLogs"
    ]
    """<p>An array where each member of the array includes both the original version and the transformed version of one of the log events that you input.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestTransformerResponse) -> dict:
    out: dict = {}
    if "transformed_logs" in value:
        import capo_cloudwatch_logs.types.transformed_logs

        out["transformedLogs"] = (
            capo_cloudwatch_logs.types.transformed_logs.serialize_aws_json_1_1(
                value["transformed_logs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestTransformerResponse:
    out: TestTransformerResponse = {}  # type: ignore[typeddict-item]
    if data.get("transformedLogs") is not None:
        import capo_cloudwatch_logs.types.transformed_logs

        out["transformed_logs"] = (
            capo_cloudwatch_logs.types.transformed_logs.deserialize_aws_json_1_1(
                data["transformedLogs"]
            )
        )
    return out
