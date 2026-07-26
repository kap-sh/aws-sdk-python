"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerMetricsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.crawler_metrics

CrawlerMetricsList: TypeAlias = list["capo_glue.types.crawler_metrics.CrawlerMetrics"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerMetricsList) -> list:
    import capo_glue.types.crawler_metrics

    out: list = []
    for item in value:
        out.append(capo_glue.types.crawler_metrics.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CrawlerMetricsList:
    import capo_glue.types.crawler_metrics

    out: CrawlerMetricsList = []
    for item in data:
        out.append(capo_glue.types.crawler_metrics.deserialize_aws_json_1_1(item))
    return out
