"""Generated from Smithy shape ``com.amazonaws.glue#RecrawlPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.recrawl_behavior


class RecrawlPolicy(TypedDict, closed=True):
    recrawl_behavior: NotRequired["capo_glue.types.recrawl_behavior.RecrawlBehavior"]
    """<p>Specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run.</p> <p>A value of <code>CRAWL_EVERYTHING</code> specifies crawling the entire dataset again.</p> <p>A value of <code>CRAWL_NEW_FOLDERS_ONLY</code> specifies crawling only folders that were added since the last crawler run.</p> <p>A value of <code>CRAWL_EVENT_MODE</code> specifies crawling only the changes identified by Amazon S3 events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecrawlPolicy) -> dict:
    out: dict = {}
    if "recrawl_behavior" in value:
        import capo_glue.types.recrawl_behavior

        out["RecrawlBehavior"] = (
            capo_glue.types.recrawl_behavior.serialize_aws_json_1_1(
                value["recrawl_behavior"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecrawlPolicy:
    out: RecrawlPolicy = {}  # type: ignore[typeddict-item]
    if "RecrawlBehavior" in data:
        import capo_glue.types.recrawl_behavior

        out["recrawl_behavior"] = (
            capo_glue.types.recrawl_behavior.deserialize_aws_json_1_1(
                data["RecrawlBehavior"]
            )
        )
    return out
