"""Generated from Smithy shape ``com.amazonaws.emr#JobFlowExecutionStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.job_flow_execution_state

JobFlowExecutionStateList: TypeAlias = list[
    "capo_emr.types.job_flow_execution_state.JobFlowExecutionState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobFlowExecutionStateList) -> list:
    import capo_emr.types.job_flow_execution_state

    out: list = []
    for item in value:
        out.append(capo_emr.types.job_flow_execution_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobFlowExecutionStateList:
    import capo_emr.types.job_flow_execution_state

    out: JobFlowExecutionStateList = []
    for item in data:
        out.append(
            capo_emr.types.job_flow_execution_state.deserialize_aws_json_1_1(item)
        )
    return out
