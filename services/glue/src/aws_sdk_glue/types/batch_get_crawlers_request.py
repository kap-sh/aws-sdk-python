"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetCrawlersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler_name_list


class BatchGetCrawlersRequest(TypedDict, closed=True):
    crawler_names: "aws_sdk_glue.types.crawler_name_list.CrawlerNameList"
    """<p>A list of crawler names, which might be the names returned from the <code>ListCrawlers</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCrawlersRequest) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.crawler_name_list

    out["CrawlerNames"] = aws_sdk_glue.types.crawler_name_list.serialize_aws_json_1_1(
        value["crawler_names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCrawlersRequest:
    out: BatchGetCrawlersRequest = {}  # type: ignore[typeddict-item]
    if "CrawlerNames" in data:
        import aws_sdk_glue.types.crawler_name_list

        out["crawler_names"] = (
            aws_sdk_glue.types.crawler_name_list.deserialize_aws_json_1_1(
                data["CrawlerNames"]
            )
        )
    else:
        raise DeserializationError("BatchGetCrawlersRequest.crawler_names required")
    return out
