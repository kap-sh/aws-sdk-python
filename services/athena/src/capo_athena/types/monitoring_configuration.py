"""Generated from Smithy shape ``com.amazonaws.athena#MonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.cloud_watch_logging_configuration
    import capo_athena.types.managed_logging_configuration
    import capo_athena.types.s3_logging_configuration


class MonitoringConfiguration(TypedDict, closed=True):
    cloud_watch_logging_configuration: NotRequired[
        "capo_athena.types.cloud_watch_logging_configuration.CloudWatchLoggingConfiguration"
    ]
    """<p>Configuration settings for delivering logs to Amazon CloudWatch log groups. </p>"""
    managed_logging_configuration: NotRequired[
        "capo_athena.types.managed_logging_configuration.ManagedLoggingConfiguration"
    ]
    """<p>Configuration settings for managed log persistence. </p>"""
    s3_logging_configuration: NotRequired[
        "capo_athena.types.s3_logging_configuration.S3LoggingConfiguration"
    ]
    """<p>Configuration settings for delivering logs to Amazon S3 buckets. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringConfiguration) -> dict:
    out: dict = {}
    if "cloud_watch_logging_configuration" in value:
        import capo_athena.types.cloud_watch_logging_configuration

        out["CloudWatchLoggingConfiguration"] = (
            capo_athena.types.cloud_watch_logging_configuration.serialize_aws_json_1_1(
                value["cloud_watch_logging_configuration"]
            )
        )
    if "managed_logging_configuration" in value:
        import capo_athena.types.managed_logging_configuration

        out["ManagedLoggingConfiguration"] = (
            capo_athena.types.managed_logging_configuration.serialize_aws_json_1_1(
                value["managed_logging_configuration"]
            )
        )
    if "s3_logging_configuration" in value:
        import capo_athena.types.s3_logging_configuration

        out["S3LoggingConfiguration"] = (
            capo_athena.types.s3_logging_configuration.serialize_aws_json_1_1(
                value["s3_logging_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringConfiguration:
    out: MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "CloudWatchLoggingConfiguration" in data:
        import capo_athena.types.cloud_watch_logging_configuration

        out["cloud_watch_logging_configuration"] = (
            capo_athena.types.cloud_watch_logging_configuration.deserialize_aws_json_1_1(
                data["CloudWatchLoggingConfiguration"]
            )
        )
    if "ManagedLoggingConfiguration" in data:
        import capo_athena.types.managed_logging_configuration

        out["managed_logging_configuration"] = (
            capo_athena.types.managed_logging_configuration.deserialize_aws_json_1_1(
                data["ManagedLoggingConfiguration"]
            )
        )
    if "S3LoggingConfiguration" in data:
        import capo_athena.types.s3_logging_configuration

        out["s3_logging_configuration"] = (
            capo_athena.types.s3_logging_configuration.deserialize_aws_json_1_1(
                data["S3LoggingConfiguration"]
            )
        )
    return out
