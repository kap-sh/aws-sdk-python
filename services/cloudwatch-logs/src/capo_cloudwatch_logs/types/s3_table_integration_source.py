"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#S3TableIntegrationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.data_source
    import capo_cloudwatch_logs.types.s3_table_integration_source_identifier
    import capo_cloudwatch_logs.types.s3_table_integration_source_status
    import capo_cloudwatch_logs.types.s3_table_integration_source_status_reason
    import capo_cloudwatch_logs.types.timestamp


class S3TableIntegrationSource(TypedDict, closed=True):
    identifier: NotRequired[
        "capo_cloudwatch_logs.types.s3_table_integration_source_identifier.S3TableIntegrationSourceIdentifier"
    ]
    """<p>The unique identifier for this data source association.</p>"""
    data_source: NotRequired["capo_cloudwatch_logs.types.data_source.DataSource"]
    """<p>The data source associated with the S3 Table Integration.</p>"""
    status: NotRequired[
        "capo_cloudwatch_logs.types.s3_table_integration_source_status.S3TableIntegrationSourceStatus"
    ]
    """<p>The current status of the data source association.</p>"""
    status_reason: NotRequired[
        "capo_cloudwatch_logs.types.s3_table_integration_source_status_reason.S3TableIntegrationSourceStatusReason"
    ]
    """<p>Additional information about the status of the data source association.</p>"""
    created_time_stamp: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the data source association was created.</p>"""
    parent_source_identifier: NotRequired[
        "capo_cloudwatch_logs.types.s3_table_integration_source_identifier.S3TableIntegrationSourceIdentifier"
    ]
    """<p>The identifier of the parent data source for this association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TableIntegrationSource) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "data_source" in value:
        import capo_cloudwatch_logs.types.data_source

        out["dataSource"] = (
            capo_cloudwatch_logs.types.data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    if "status" in value:
        import capo_cloudwatch_logs.types.s3_table_integration_source_status

        out["status"] = (
            capo_cloudwatch_logs.types.s3_table_integration_source_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "created_time_stamp" in value:
        out["createdTimeStamp"] = value["created_time_stamp"]
    if "parent_source_identifier" in value:
        out["parentSourceIdentifier"] = value["parent_source_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3TableIntegrationSource:
    out: S3TableIntegrationSource = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    if "dataSource" in data:
        import capo_cloudwatch_logs.types.data_source

        out["data_source"] = (
            capo_cloudwatch_logs.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    if "status" in data:
        import capo_cloudwatch_logs.types.s3_table_integration_source_status

        out["status"] = (
            capo_cloudwatch_logs.types.s3_table_integration_source_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "createdTimeStamp" in data:
        out["created_time_stamp"] = data["createdTimeStamp"]
    if "parentSourceIdentifier" in data:
        out["parent_source_identifier"] = data["parentSourceIdentifier"]
    return out
