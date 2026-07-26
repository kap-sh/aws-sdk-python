"""Generated from Smithy shape ``com.amazonaws.costexplorer#CoveragesByTime``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.coverage_by_time

CoveragesByTime: TypeAlias = list[
    "capo_cost_explorer.types.coverage_by_time.CoverageByTime"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CoveragesByTime) -> list:
    import capo_cost_explorer.types.coverage_by_time

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.coverage_by_time.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CoveragesByTime:
    import capo_cost_explorer.types.coverage_by_time

    out: CoveragesByTime = []
    for item in data:
        out.append(
            capo_cost_explorer.types.coverage_by_time.deserialize_aws_json_1_1(item)
        )
    return out
