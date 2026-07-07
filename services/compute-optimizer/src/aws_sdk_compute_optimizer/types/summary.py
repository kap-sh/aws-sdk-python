"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Summary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.finding
    import aws_sdk_compute_optimizer.types.reason_code_summaries
    import aws_sdk_compute_optimizer.types.summary_value


class Summary(TypedDict, closed=True):
    name: NotRequired["aws_sdk_compute_optimizer.types.finding.Finding"]
    """<p>The finding classification of the recommendation.</p>"""
    value: "aws_sdk_compute_optimizer.types.summary_value.SummaryValue"
    """<p>The value of the recommendation summary.</p>"""
    reason_code_summaries: NotRequired[
        "aws_sdk_compute_optimizer.types.reason_code_summaries.ReasonCodeSummaries"
    ]
    """<p>An array of objects that summarize a finding reason code.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Summary) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_compute_optimizer.types.finding

        out["name"] = aws_sdk_compute_optimizer.types.finding.serialize_aws_json_1_0(
            value["name"]
        )
    out["value"] = value.get("value", 0)
    if "reason_code_summaries" in value:
        import aws_sdk_compute_optimizer.types.reason_code_summaries

        out["reasonCodeSummaries"] = (
            aws_sdk_compute_optimizer.types.reason_code_summaries.serialize_aws_json_1_0(
                value["reason_code_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Summary:
    out: Summary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_compute_optimizer.types.finding

        out["name"] = aws_sdk_compute_optimizer.types.finding.deserialize_aws_json_1_0(
            data["name"]
        )
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    if "reasonCodeSummaries" in data:
        import aws_sdk_compute_optimizer.types.reason_code_summaries

        out["reason_code_summaries"] = (
            aws_sdk_compute_optimizer.types.reason_code_summaries.deserialize_aws_json_1_0(
                data["reasonCodeSummaries"]
            )
        )
    return out
