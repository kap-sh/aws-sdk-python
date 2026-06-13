"""Generated from Smithy shape ``com.amazonaws.emr#StepMonitoringConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.s3_monitoring_configuration


class StepMonitoringConfiguration(TypedDict):
    s3_monitoring_configuration: NotRequired[
        "aws_sdk_emr.types.s3_monitoring_configuration.S3MonitoringConfiguration"
    ]
    """<p>The Amazon S3 configuration for monitoring log publishing. You can configure your step to send log information to Amazon S3. When it's specified, it takes precedence over the cluster's logging configuration. If you don't specify this configuration entirely, or omit individual fields, EMR falls back to cluster-level logging behavior. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepMonitoringConfiguration) -> dict:
    out: dict = {}
    if "s3_monitoring_configuration" in value:
        import aws_sdk_emr.types.s3_monitoring_configuration

        out["S3MonitoringConfiguration"] = (
            aws_sdk_emr.types.s3_monitoring_configuration.serialize_aws_json_1_1(
                value["s3_monitoring_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepMonitoringConfiguration:
    out: StepMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "S3MonitoringConfiguration" in data:
        import aws_sdk_emr.types.s3_monitoring_configuration

        out["s3_monitoring_configuration"] = (
            aws_sdk_emr.types.s3_monitoring_configuration.deserialize_aws_json_1_1(
                data["S3MonitoringConfiguration"]
            )
        )
    return out
