"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.non_negative_double
    import aws_sdk_glue.types.non_negative_integer


class CrawlerMetrics(TypedDict):
    crawler_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the crawler.</p>"""
    time_left_seconds: "aws_sdk_glue.types.non_negative_double.NonNegativeDouble"
    """<p>The estimated time left to complete a running crawl.</p>"""
    still_estimating: "aws_sdk_glue.types.boolean.Boolean"
    """<p>True if the crawler is still estimating how long it will take to complete this run.</p>"""
    last_runtime_seconds: "aws_sdk_glue.types.non_negative_double.NonNegativeDouble"
    """<p>The duration of the crawler's most recent run, in seconds.</p>"""
    median_runtime_seconds: "aws_sdk_glue.types.non_negative_double.NonNegativeDouble"
    """<p>The median duration of this crawler's runs, in seconds.</p>"""
    tables_created: "aws_sdk_glue.types.non_negative_integer.NonNegativeInteger"
    """<p>The number of tables created by this crawler.</p>"""
    tables_updated: "aws_sdk_glue.types.non_negative_integer.NonNegativeInteger"
    """<p>The number of tables updated by this crawler.</p>"""
    tables_deleted: "aws_sdk_glue.types.non_negative_integer.NonNegativeInteger"
    """<p>The number of tables deleted by this crawler.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerMetrics) -> dict:
    out: dict = {}
    if "crawler_name" in value:
        out["CrawlerName"] = value["crawler_name"]
    out["TimeLeftSeconds"] = value.get("time_left_seconds", 0)
    out["StillEstimating"] = value.get("still_estimating", False)
    out["LastRuntimeSeconds"] = value.get("last_runtime_seconds", 0)
    out["MedianRuntimeSeconds"] = value.get("median_runtime_seconds", 0)
    out["TablesCreated"] = value.get("tables_created", 0)
    out["TablesUpdated"] = value.get("tables_updated", 0)
    out["TablesDeleted"] = value.get("tables_deleted", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CrawlerMetrics:
    out: CrawlerMetrics = {}  # type: ignore[typeddict-item]
    if "CrawlerName" in data:
        out["crawler_name"] = data["CrawlerName"]
    if "TimeLeftSeconds" in data:
        out["time_left_seconds"] = data["TimeLeftSeconds"]
    else:
        out["time_left_seconds"] = 0
    if "StillEstimating" in data:
        out["still_estimating"] = data["StillEstimating"]
    else:
        out["still_estimating"] = False
    if "LastRuntimeSeconds" in data:
        out["last_runtime_seconds"] = data["LastRuntimeSeconds"]
    else:
        out["last_runtime_seconds"] = 0
    if "MedianRuntimeSeconds" in data:
        out["median_runtime_seconds"] = data["MedianRuntimeSeconds"]
    else:
        out["median_runtime_seconds"] = 0
    if "TablesCreated" in data:
        out["tables_created"] = data["TablesCreated"]
    else:
        out["tables_created"] = 0
    if "TablesUpdated" in data:
        out["tables_updated"] = data["TablesUpdated"]
    else:
        out["tables_updated"] = 0
    if "TablesDeleted" in data:
        out["tables_deleted"] = data["TablesDeleted"]
    else:
        out["tables_deleted"] = 0
    return out
