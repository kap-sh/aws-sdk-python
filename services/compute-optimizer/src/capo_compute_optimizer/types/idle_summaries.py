"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.idle_summary

IdleSummaries: TypeAlias = list["capo_compute_optimizer.types.idle_summary.IdleSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleSummaries) -> list:
    import capo_compute_optimizer.types.idle_summary

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.idle_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdleSummaries:
    import capo_compute_optimizer.types.idle_summary

    out: IdleSummaries = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.idle_summary.deserialize_aws_json_1_0(item)
        )
    return out
