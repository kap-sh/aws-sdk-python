"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#DescribeReportCreationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.error_message
    import aws_sdk_resource_groups_tagging_api.types.s3_location
    import aws_sdk_resource_groups_tagging_api.types.start_date
    import aws_sdk_resource_groups_tagging_api.types.status


class DescribeReportCreationOutput(TypedDict, closed=True):
    status: NotRequired["aws_sdk_resource_groups_tagging_api.types.status.Status"]
    """<p>Reports the status of the operation.</p> <p>The operation status can be one of the following:</p> <ul> <li> <p> <code>RUNNING</code> - Report creation is in progress.</p> </li> <li> <p> <code>SUCCEEDED</code> - Report creation is complete. You can open the report from the Amazon S3 bucket that you specified when you ran <code>StartReportCreation</code>.</p> </li> <li> <p> <code>FAILED</code> - Report creation timed out or the Amazon S3 bucket is not accessible. </p> </li> <li> <p> <code>NO REPORT</code> - No report was generated in the last 90 days.</p> </li> </ul>"""
    s3_location: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.s3_location.S3Location"
    ]
    """<p>The path to the Amazon S3 bucket where the report was stored on creation.</p>"""
    start_date: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.start_date.StartDate"
    ]
    """<p>The date and time that the report was started. </p>"""
    error_message: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.error_message.ErrorMessage"
    ]
    """<p>Details of the common errors that all operations return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReportCreationOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "s3_location" in value:
        out["S3Location"] = value["s3_location"]
    if "start_date" in value:
        out["StartDate"] = value["start_date"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReportCreationOutput:
    out: DescribeReportCreationOutput = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "S3Location" in data:
        out["s3_location"] = data["S3Location"]
    if "StartDate" in data:
        out["start_date"] = data["StartDate"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
