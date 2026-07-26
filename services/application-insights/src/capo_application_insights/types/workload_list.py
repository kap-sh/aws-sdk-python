"""Generated from Smithy shape ``com.amazonaws.applicationinsights#WorkloadList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.workload

WorkloadList: TypeAlias = list["capo_application_insights.types.workload.Workload"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkloadList) -> list:
    import capo_application_insights.types.workload

    out: list = []
    for item in value:
        out.append(
            capo_application_insights.types.workload.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkloadList:
    import capo_application_insights.types.workload

    out: WorkloadList = []
    for item in data:
        out.append(
            capo_application_insights.types.workload.deserialize_aws_json_1_1(item)
        )
    return out
