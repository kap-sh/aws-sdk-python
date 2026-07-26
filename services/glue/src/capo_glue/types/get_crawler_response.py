"""Generated from Smithy shape ``com.amazonaws.glue#GetCrawlerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.crawler


class GetCrawlerResponse(TypedDict, closed=True):
    crawler: NotRequired["capo_glue.types.crawler.Crawler"]
    """<p>The metadata for the specified crawler.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCrawlerResponse) -> dict:
    out: dict = {}
    if "crawler" in value:
        import capo_glue.types.crawler

        out["Crawler"] = capo_glue.types.crawler.serialize_aws_json_1_1(
            value["crawler"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCrawlerResponse:
    out: GetCrawlerResponse = {}  # type: ignore[typeddict-item]
    if "Crawler" in data:
        import capo_glue.types.crawler

        out["crawler"] = capo_glue.types.crawler.deserialize_aws_json_1_1(
            data["Crawler"]
        )
    return out
