"""Generated from Smithy shape ``com.amazonaws.securityhub#InsightResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.insight_result_value_list
    import capo_securityhub.types.non_empty_string


class InsightResults(TypedDict, closed=True):
    insight_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the insight whose results are returned by the <code>GetInsightResults</code> operation.</p>"""
    group_by_attribute: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The attribute that the findings are grouped by for the insight whose results are returned by the <code>GetInsightResults</code> operation.</p>"""
    result_values: NotRequired[
        "capo_securityhub.types.insight_result_value_list.InsightResultValueList"
    ]
    """<p>The list of insight result values returned by the <code>GetInsightResults</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightResults) -> dict:
    out: dict = {}
    if "insight_arn" in value:
        out["InsightArn"] = value["insight_arn"]
    if "group_by_attribute" in value:
        out["GroupByAttribute"] = value["group_by_attribute"]
    if "result_values" in value:
        import capo_securityhub.types.insight_result_value_list

        out["ResultValues"] = (
            capo_securityhub.types.insight_result_value_list.serialize_json(
                value["result_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> InsightResults:
    out: InsightResults = {}  # type: ignore[typeddict-item]
    if "InsightArn" in data:
        out["insight_arn"] = data["InsightArn"]
    if "GroupByAttribute" in data:
        out["group_by_attribute"] = data["GroupByAttribute"]
    if "ResultValues" in data:
        import capo_securityhub.types.insight_result_value_list

        out["result_values"] = (
            capo_securityhub.types.insight_result_value_list.deserialize_json(
                data["ResultValues"]
            )
        )
    return out
