"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityAggregatedMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.nullable_double


class DataQualityAggregatedMetrics(TypedDict, closed=True):
    total_rows_processed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of rows that were processed during the data quality evaluation.</p>"""
    total_rows_passed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of rows that passed all applicable data quality rules.</p>"""
    total_rows_failed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of rows that failed one or more data quality rules.</p>"""
    total_rules_processed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of data quality rules that were evaluated.</p>"""
    total_rules_passed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of data quality rules that passed their evaluation criteria.</p>"""
    total_rules_failed: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total number of data quality rules that failed their evaluation criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityAggregatedMetrics) -> dict:
    out: dict = {}
    if "total_rows_processed" in value:
        out["TotalRowsProcessed"] = value["total_rows_processed"]
    if "total_rows_passed" in value:
        out["TotalRowsPassed"] = value["total_rows_passed"]
    if "total_rows_failed" in value:
        out["TotalRowsFailed"] = value["total_rows_failed"]
    if "total_rules_processed" in value:
        out["TotalRulesProcessed"] = value["total_rules_processed"]
    if "total_rules_passed" in value:
        out["TotalRulesPassed"] = value["total_rules_passed"]
    if "total_rules_failed" in value:
        out["TotalRulesFailed"] = value["total_rules_failed"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityAggregatedMetrics:
    out: DataQualityAggregatedMetrics = {}  # type: ignore[typeddict-item]
    if "TotalRowsProcessed" in data:
        out["total_rows_processed"] = data["TotalRowsProcessed"]
    if "TotalRowsPassed" in data:
        out["total_rows_passed"] = data["TotalRowsPassed"]
    if "TotalRowsFailed" in data:
        out["total_rows_failed"] = data["TotalRowsFailed"]
    if "TotalRulesProcessed" in data:
        out["total_rules_processed"] = data["TotalRulesProcessed"]
    if "TotalRulesPassed" in data:
        out["total_rules_passed"] = data["TotalRulesPassed"]
    if "TotalRulesFailed" in data:
        out["total_rules_failed"] = data["TotalRulesFailed"]
    return out
