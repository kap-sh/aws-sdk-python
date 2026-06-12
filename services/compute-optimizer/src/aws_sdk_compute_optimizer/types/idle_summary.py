"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.idle_finding
    import aws_sdk_compute_optimizer.types.summary_value


class IdleSummary(TypedDict):
    name: NotRequired["aws_sdk_compute_optimizer.types.idle_finding.IdleFinding"]
    """<p>The name of the finding group for the idle resources.</p>"""
    value: "aws_sdk_compute_optimizer.types.summary_value.SummaryValue"
    """<p>The count of idle resources in the finding group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleSummary) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_compute_optimizer.types.idle_finding

        out["name"] = (
            aws_sdk_compute_optimizer.types.idle_finding.serialize_aws_json_1_0(
                value["name"]
            )
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> IdleSummary:
    out: IdleSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_compute_optimizer.types.idle_finding

        out["name"] = (
            aws_sdk_compute_optimizer.types.idle_finding.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
