"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ReasonCodeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.finding_reason_code
    import aws_sdk_compute_optimizer.types.summary_value


class ReasonCodeSummary(TypedDict):
    name: NotRequired[
        "aws_sdk_compute_optimizer.types.finding_reason_code.FindingReasonCode"
    ]
    """<p>The name of the finding reason code.</p>"""
    value: "aws_sdk_compute_optimizer.types.summary_value.SummaryValue"
    """<p>The value of the finding reason code summary.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReasonCodeSummary) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_compute_optimizer.types.finding_reason_code

        out["name"] = (
            aws_sdk_compute_optimizer.types.finding_reason_code.serialize_aws_json_1_0(
                value["name"]
            )
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ReasonCodeSummary:
    out: ReasonCodeSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_compute_optimizer.types.finding_reason_code

        out["name"] = (
            aws_sdk_compute_optimizer.types.finding_reason_code.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
