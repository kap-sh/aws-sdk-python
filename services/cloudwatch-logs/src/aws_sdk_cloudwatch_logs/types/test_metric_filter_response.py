"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TestMetricFilterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.metric_filter_matches


class TestMetricFilterResponse(TypedDict):
    matches: NotRequired[
        "aws_sdk_cloudwatch_logs.types.metric_filter_matches.MetricFilterMatches"
    ]
    """<p>The matched events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestMetricFilterResponse) -> dict:
    out: dict = {}
    if "matches" in value:
        import aws_sdk_cloudwatch_logs.types.metric_filter_matches

        out["matches"] = (
            aws_sdk_cloudwatch_logs.types.metric_filter_matches.serialize_aws_json_1_1(
                value["matches"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestMetricFilterResponse:
    out: TestMetricFilterResponse = {}  # type: ignore[typeddict-item]
    if "matches" in data:
        import aws_sdk_cloudwatch_logs.types.metric_filter_matches

        out["matches"] = (
            aws_sdk_cloudwatch_logs.types.metric_filter_matches.deserialize_aws_json_1_1(
                data["matches"]
            )
        )
    return out
