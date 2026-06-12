"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.analysis_id

AnalysisIds: TypeAlias = list["aws_sdk_cost_explorer.types.analysis_id.AnalysisId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AnalysisIds:
    return list(data)
