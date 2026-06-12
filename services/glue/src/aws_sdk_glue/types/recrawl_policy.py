"""Generated from Smithy shape ``com.amazonaws.glue#RecrawlPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.recrawl_behavior


class RecrawlPolicy(TypedDict):
    recrawl_behavior: NotRequired["aws_sdk_glue.types.recrawl_behavior.RecrawlBehavior"]
    """<p>Specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run.</p> <p>A value of <code>CRAWL_EVERYTHING</code> specifies crawling the entire dataset again.</p> <p>A value of <code>CRAWL_NEW_FOLDERS_ONLY</code> specifies crawling only folders that were added since the last crawler run.</p> <p>A value of <code>CRAWL_EVENT_MODE</code> specifies crawling only the changes identified by Amazon S3 events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecrawlPolicy) -> dict:
    out: dict = {}
    if "recrawl_behavior" in value:
        import aws_sdk_glue.types.recrawl_behavior

        out["RecrawlBehavior"] = (
            aws_sdk_glue.types.recrawl_behavior.serialize_aws_json_1_1(
                value["recrawl_behavior"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecrawlPolicy:
    out: RecrawlPolicy = {}  # type: ignore[typeddict-item]
    if "RecrawlBehavior" in data:
        import aws_sdk_glue.types.recrawl_behavior

        out["recrawl_behavior"] = (
            aws_sdk_glue.types.recrawl_behavior.deserialize_aws_json_1_1(
                data["RecrawlBehavior"]
            )
        )
    return out
