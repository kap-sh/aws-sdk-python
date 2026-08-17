"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TestMetricFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.metric_filter_matches


class TestMetricFilterResponse(TypedDict, closed=True):
    matches: NotRequired[
        "capo_cloudwatch_logs.types.metric_filter_matches.MetricFilterMatches"
    ]
    """<p>The matched events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestMetricFilterResponse) -> dict:
    out: dict = {}
    if "matches" in value:
        import capo_cloudwatch_logs.types.metric_filter_matches

        out["matches"] = (
            capo_cloudwatch_logs.types.metric_filter_matches.serialize_aws_json_1_1(
                value["matches"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestMetricFilterResponse:
    out: TestMetricFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("matches") is not None:
        import capo_cloudwatch_logs.types.metric_filter_matches

        out["matches"] = (
            capo_cloudwatch_logs.types.metric_filter_matches.deserialize_aws_json_1_1(
                data["matches"]
            )
        )
    return out
