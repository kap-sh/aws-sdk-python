"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeWorkloadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.remarks
    import aws_sdk_application_insights.types.workload_configuration
    import aws_sdk_application_insights.types.workload_id


class DescribeWorkloadResponse(TypedDict, closed=True):
    workload_id: NotRequired[
        "aws_sdk_application_insights.types.workload_id.WorkloadId"
    ]
    """<p>The ID of the workload.</p>"""
    workload_remarks: NotRequired["aws_sdk_application_insights.types.remarks.Remarks"]
    """<p>If logging is supported for the resource type, shows whether the component has configured logs to be monitored.</p>"""
    workload_configuration: NotRequired[
        "aws_sdk_application_insights.types.workload_configuration.WorkloadConfiguration"
    ]
    """<p>The configuration settings of the workload. The value is the escaped JSON of the configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkloadResponse) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_remarks" in value:
        out["WorkloadRemarks"] = value["workload_remarks"]
    if "workload_configuration" in value:
        import aws_sdk_application_insights.types.workload_configuration

        out["WorkloadConfiguration"] = (
            aws_sdk_application_insights.types.workload_configuration.serialize_aws_json_1_1(
                value["workload_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkloadResponse:
    out: DescribeWorkloadResponse = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadRemarks" in data:
        out["workload_remarks"] = data["WorkloadRemarks"]
    if "WorkloadConfiguration" in data:
        import aws_sdk_application_insights.types.workload_configuration

        out["workload_configuration"] = (
            aws_sdk_application_insights.types.workload_configuration.deserialize_aws_json_1_1(
                data["WorkloadConfiguration"]
            )
        )
    return out
