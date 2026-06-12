"""Generated from Smithy shape ``com.amazonaws.glue#CrawlsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawls_filter

CrawlsFilterList: TypeAlias = list["aws_sdk_glue.types.crawls_filter.CrawlsFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlsFilterList) -> list:
    import aws_sdk_glue.types.crawls_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.crawls_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CrawlsFilterList:
    import aws_sdk_glue.types.crawls_filter

    out: CrawlsFilterList = []
    for item in data:
        out.append(aws_sdk_glue.types.crawls_filter.deserialize_aws_json_1_1(item))
    return out
