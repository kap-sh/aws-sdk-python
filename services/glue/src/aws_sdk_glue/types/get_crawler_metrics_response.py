"""Generated from Smithy shape ``com.amazonaws.glue#GetCrawlerMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler_metrics_list
    import aws_sdk_glue.types.token


class GetCrawlerMetricsResponse(TypedDict, closed=True):
    crawler_metrics_list: NotRequired[
        "aws_sdk_glue.types.crawler_metrics_list.CrawlerMetricsList"
    ]
    """<p>A list of metrics for the specified crawler.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if the returned list does not contain the last metric available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCrawlerMetricsResponse) -> dict:
    out: dict = {}
    if "crawler_metrics_list" in value:
        import aws_sdk_glue.types.crawler_metrics_list

        out["CrawlerMetricsList"] = (
            aws_sdk_glue.types.crawler_metrics_list.serialize_aws_json_1_1(
                value["crawler_metrics_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCrawlerMetricsResponse:
    out: GetCrawlerMetricsResponse = {}  # type: ignore[typeddict-item]
    if "CrawlerMetricsList" in data:
        import aws_sdk_glue.types.crawler_metrics_list

        out["crawler_metrics_list"] = (
            aws_sdk_glue.types.crawler_metrics_list.deserialize_aws_json_1_1(
                data["CrawlerMetricsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
