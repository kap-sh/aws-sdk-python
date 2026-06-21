"""Generated from Smithy shape ``com.amazonaws.kendra#MetricType``."""

from typing import Literal, TypeAlias, cast

MetricType: TypeAlias = Literal[
    "QUERIES_BY_COUNT",
    "QUERIES_BY_ZERO_CLICK_RATE",
    "QUERIES_BY_ZERO_RESULT_RATE",
    "DOCS_BY_CLICK_COUNT",
    "AGG_QUERY_DOC_METRICS",
    "TREND_QUERY_DOC_METRICS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricType:
    return cast(MetricType, data)
