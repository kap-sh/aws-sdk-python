"""Generated from Smithy shape ``com.amazonaws.emr#S3LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.log_type_map


class S3LoggingConfiguration(TypedDict, closed=True):
    log_type_upload_policy: NotRequired["aws_sdk_emr.types.log_type_map.LogTypeMap"]
    """<p>A map that specifies the upload policy for each log type. The key is the log type, and the value is the upload policy.</p> <p>Valid log types:</p> <ul> <li> <p> <code>system-logs</code>: EMR Daemon logs.</p> </li> <li> <p> <code>application-logs</code>: Framework logs from Hadoop, Spark, Hive and other applications running on the cluster.</p> </li> <li> <p> <code>persistent-ui-logs</code>: Logs required for persistent application UIs such as Spark History Server and Tez UI.</p> </li> </ul> <p>Valid upload policies:</p> <ul> <li> <p> <code>emr-managed</code>: Standard behavior. Logs are uploaded to S3 bucket as configured in your LogUri, with certain logs retained by the service for operational support and troubleshooting purposes.</p> </li> <li> <p> <code>on-customer-s3only</code>: Logs are uploaded only to the customer-specified S3 bucket. This requires you to specify a LogUri when creating the cluster. Persistent-ui-logs cannot have on-customer-s3only policy. Allowed policies for persistent-ui-logs are emr-managed and disabled.</p> </li> <li> <p> <code>disabled</code>: No S3 upload for this log type.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3LoggingConfiguration) -> dict:
    out: dict = {}
    if "log_type_upload_policy" in value:
        import aws_sdk_emr.types.log_type_map

        out["LogTypeUploadPolicy"] = (
            aws_sdk_emr.types.log_type_map.serialize_aws_json_1_1(
                value["log_type_upload_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3LoggingConfiguration:
    out: S3LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "LogTypeUploadPolicy" in data:
        import aws_sdk_emr.types.log_type_map

        out["log_type_upload_policy"] = (
            aws_sdk_emr.types.log_type_map.deserialize_aws_json_1_1(
                data["LogTypeUploadPolicy"]
            )
        )
    return out
