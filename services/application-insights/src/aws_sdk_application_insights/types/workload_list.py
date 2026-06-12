"""Generated from Smithy shape ``com.amazonaws.applicationinsights#WorkloadList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.workload

WorkloadList: TypeAlias = list["aws_sdk_application_insights.types.workload.Workload"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkloadList) -> list:
    import aws_sdk_application_insights.types.workload

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_insights.types.workload.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkloadList:
    import aws_sdk_application_insights.types.workload

    out: WorkloadList = []
    for item in data:
        out.append(
            aws_sdk_application_insights.types.workload.deserialize_aws_json_1_1(item)
        )
    return out
