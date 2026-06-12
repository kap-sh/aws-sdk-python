"""Generated from Smithy shape ``com.amazonaws.glue#GetCrawlerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler


class GetCrawlerResponse(TypedDict):
    crawler: NotRequired["aws_sdk_glue.types.crawler.Crawler"]
    """<p>The metadata for the specified crawler.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCrawlerResponse) -> dict:
    out: dict = {}
    if "crawler" in value:
        import aws_sdk_glue.types.crawler

        out["Crawler"] = aws_sdk_glue.types.crawler.serialize_aws_json_1_1(
            value["crawler"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCrawlerResponse:
    out: GetCrawlerResponse = {}  # type: ignore[typeddict-item]
    if "Crawler" in data:
        import aws_sdk_glue.types.crawler

        out["crawler"] = aws_sdk_glue.types.crawler.deserialize_aws_json_1_1(
            data["Crawler"]
        )
    return out
