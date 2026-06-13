"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#PreviewResultSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.rule_preview_total


class PreviewResultSummary(TypedDict):
    key: "str"
    """<p>The key identifier for this preview result summary.</p>"""
    total: (
        "aws_sdk_compute_optimizer_automation.types.rule_preview_total.RulePreviewTotal"
    )


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreviewResultSummary) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import aws_sdk_compute_optimizer_automation.types.rule_preview_total

    out["total"] = (
        aws_sdk_compute_optimizer_automation.types.rule_preview_total.serialize_aws_json_1_0(
            value["total"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PreviewResultSummary:
    out: PreviewResultSummary = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("PreviewResultSummary.key required")
    if "total" in data:
        import aws_sdk_compute_optimizer_automation.types.rule_preview_total

        out["total"] = (
            aws_sdk_compute_optimizer_automation.types.rule_preview_total.deserialize_aws_json_1_0(
                data["total"]
            )
        )
    else:
        raise DeserializationError("PreviewResultSummary.total required")
    return out
