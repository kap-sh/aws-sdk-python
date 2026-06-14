"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateImportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.import_filter
    import aws_sdk_cloudwatch_logs.types.role_arn


class CreateImportTaskRequest(TypedDict):
    import_source_arn: "aws_sdk_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the source to import from.</p>"""
    import_role_arn: "aws_sdk_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants CloudWatch Logs permission to import from the CloudTrail Lake Event Data Store.</p>"""
    import_filter: NotRequired[
        "aws_sdk_cloudwatch_logs.types.import_filter.ImportFilter"
    ]
    """<p>Optional filters to constrain the import by CloudTrail event time. Times are specified in Unix timestamp milliseconds. The range of data being imported must be within the specified source's retention period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImportTaskRequest) -> dict:
    out: dict = {}
    out["importSourceArn"] = value["import_source_arn"]
    out["importRoleArn"] = value["import_role_arn"]
    if "import_filter" in value:
        import aws_sdk_cloudwatch_logs.types.import_filter

        out["importFilter"] = (
            aws_sdk_cloudwatch_logs.types.import_filter.serialize_aws_json_1_1(
                value["import_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImportTaskRequest:
    out: CreateImportTaskRequest = {}  # type: ignore[typeddict-item]
    if "importSourceArn" in data:
        out["import_source_arn"] = data["importSourceArn"]
    else:
        raise DeserializationError("CreateImportTaskRequest.import_source_arn required")
    if "importRoleArn" in data:
        out["import_role_arn"] = data["importRoleArn"]
    else:
        raise DeserializationError("CreateImportTaskRequest.import_role_arn required")
    if "importFilter" in data:
        import aws_sdk_cloudwatch_logs.types.import_filter

        out["import_filter"] = (
            aws_sdk_cloudwatch_logs.types.import_filter.deserialize_aws_json_1_1(
                data["importFilter"]
            )
        )
    return out
