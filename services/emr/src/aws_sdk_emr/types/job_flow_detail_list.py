"""Generated from Smithy shape ``com.amazonaws.emr#JobFlowDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.job_flow_detail

JobFlowDetailList: TypeAlias = list["aws_sdk_emr.types.job_flow_detail.JobFlowDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobFlowDetailList) -> list:
    import aws_sdk_emr.types.job_flow_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.job_flow_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobFlowDetailList:
    import aws_sdk_emr.types.job_flow_detail

    out: JobFlowDetailList = []
    for item in data:
        out.append(aws_sdk_emr.types.job_flow_detail.deserialize_aws_json_1_1(item))
    return out
