"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogs``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination
    import aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination
    import aws_sdk_ec2.types.verified_access_log_s3_destination


class VerifiedAccessLogs(TypedDict):
    s3: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_s3_destination.VerifiedAccessLogS3Destination"
    ]
    """<p>Amazon S3 logging options.</p>"""
    cloud_watch_logs: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination.VerifiedAccessLogCloudWatchLogsDestination"
    ]
    """<p>CloudWatch Logs logging destination.</p>"""
    kinesis_data_firehose: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination.VerifiedAccessLogKinesisDataFirehoseDestination"
    ]
    """<p>Kinesis logging destination.</p>"""
    log_version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The log version.</p>"""
    include_trust_context: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether trust data is included in the logs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessLogs, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "s3" in value:
        import aws_sdk_ec2.types.verified_access_log_s3_destination

        aws_sdk_ec2.types.verified_access_log_s3_destination.serialize_ec2_query(
            value["s3"], pairs, f"{prefix}.S3"
        )
    if "cloud_watch_logs" in value:
        import aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination

        aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination.serialize_ec2_query(
            value["cloud_watch_logs"], pairs, f"{prefix}.CloudWatchLogs"
        )
    if "kinesis_data_firehose" in value:
        import aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination

        aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination.serialize_ec2_query(
            value["kinesis_data_firehose"], pairs, f"{prefix}.KinesisDataFirehose"
        )
    if "log_version" in value:
        pairs.append((f"{prefix}.LogVersion", str(value["log_version"])))
    if "include_trust_context" in value:
        pairs.append(
            (
                f"{prefix}.IncludeTrustContext",
                "true" if value["include_trust_context"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessLogs:
    out: VerifiedAccessLogs = {}  # type: ignore[typeddict-item]
    child_s3 = el.find("S3")
    if child_s3 is not None:
        import aws_sdk_ec2.types.verified_access_log_s3_destination

        out["s3"] = (
            aws_sdk_ec2.types.verified_access_log_s3_destination.deserialize_ec2_query(
                child_s3
            )
        )
    child_cloud_watch_logs = el.find("CloudWatchLogs")
    if child_cloud_watch_logs is not None:
        import aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination

        out["cloud_watch_logs"] = (
            aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination.deserialize_ec2_query(
                child_cloud_watch_logs
            )
        )
    child_kinesis_data_firehose = el.find("KinesisDataFirehose")
    if child_kinesis_data_firehose is not None:
        import aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination

        out["kinesis_data_firehose"] = (
            aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination.deserialize_ec2_query(
                child_kinesis_data_firehose
            )
        )
    child_log_version = el.find("LogVersion")
    if child_log_version is not None:
        out["log_version"] = str(child_log_version.text or "")
    child_include_trust_context = el.find("IncludeTrustContext")
    if child_include_trust_context is not None:
        out["include_trust_context"] = (
            child_include_trust_context.text or ""
        ).lower() == "true"
    return out
