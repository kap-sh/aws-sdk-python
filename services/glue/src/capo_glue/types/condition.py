"""Generated from Smithy shape ``com.amazonaws.glue#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.crawl_state
    import capo_glue.types.job_run_state
    import capo_glue.types.logical_operator
    import capo_glue.types.name_string


class Condition(TypedDict, closed=True):
    logical_operator: NotRequired["capo_glue.types.logical_operator.LogicalOperator"]
    """<p>A logical operator.</p>"""
    job_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the job whose <code>JobRuns</code> this condition applies to, and on which this trigger waits.</p>"""
    state: NotRequired["capo_glue.types.job_run_state.JobRunState"]
    """<p>The condition state. Currently, the only job states that a trigger can listen for are <code>SUCCEEDED</code>, <code>STOPPED</code>, <code>FAILED</code>, and <code>TIMEOUT</code>. The only crawler states that a trigger can listen for are <code>SUCCEEDED</code>, <code>FAILED</code>, and <code>CANCELLED</code>.</p>"""
    crawler_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the crawler to which this condition applies.</p>"""
    crawl_state: NotRequired["capo_glue.types.crawl_state.CrawlState"]
    """<p>The state of the crawler to which this condition applies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Condition) -> dict:
    out: dict = {}
    if "logical_operator" in value:
        import capo_glue.types.logical_operator

        out["LogicalOperator"] = (
            capo_glue.types.logical_operator.serialize_aws_json_1_1(
                value["logical_operator"]
            )
        )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "state" in value:
        import capo_glue.types.job_run_state

        out["State"] = capo_glue.types.job_run_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "crawler_name" in value:
        out["CrawlerName"] = value["crawler_name"]
    if "crawl_state" in value:
        import capo_glue.types.crawl_state

        out["CrawlState"] = capo_glue.types.crawl_state.serialize_aws_json_1_1(
            value["crawl_state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "LogicalOperator" in data:
        import capo_glue.types.logical_operator

        out["logical_operator"] = (
            capo_glue.types.logical_operator.deserialize_aws_json_1_1(
                data["LogicalOperator"]
            )
        )
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "State" in data:
        import capo_glue.types.job_run_state

        out["state"] = capo_glue.types.job_run_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "CrawlerName" in data:
        out["crawler_name"] = data["CrawlerName"]
    if "CrawlState" in data:
        import capo_glue.types.crawl_state

        out["crawl_state"] = capo_glue.types.crawl_state.deserialize_aws_json_1_1(
            data["CrawlState"]
        )
    return out
