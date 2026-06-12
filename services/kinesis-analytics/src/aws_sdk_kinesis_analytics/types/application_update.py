"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ApplicationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_code
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_updates
    import aws_sdk_kinesis_analytics.types.input_updates
    import aws_sdk_kinesis_analytics.types.output_updates
    import aws_sdk_kinesis_analytics.types.reference_data_source_updates


class ApplicationUpdate(TypedDict):
    input_updates: NotRequired[
        "aws_sdk_kinesis_analytics.types.input_updates.InputUpdates"
    ]
    """<p>Describes application input configuration updates.</p>"""
    application_code_update: NotRequired[
        "aws_sdk_kinesis_analytics.types.application_code.ApplicationCode"
    ]
    """<p>Describes application code updates.</p>"""
    output_updates: NotRequired[
        "aws_sdk_kinesis_analytics.types.output_updates.OutputUpdates"
    ]
    """<p>Describes application output configuration updates.</p>"""
    reference_data_source_updates: NotRequired[
        "aws_sdk_kinesis_analytics.types.reference_data_source_updates.ReferenceDataSourceUpdates"
    ]
    """<p>Describes application reference data source updates.</p>"""
    cloud_watch_logging_option_updates: NotRequired[
        "aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_updates.CloudWatchLoggingOptionUpdates"
    ]
    """<p>Describes application CloudWatch logging option updates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationUpdate) -> dict:
    out: dict = {}
    if "input_updates" in value:
        import aws_sdk_kinesis_analytics.types.input_updates

        out["InputUpdates"] = (
            aws_sdk_kinesis_analytics.types.input_updates.serialize_aws_json_1_1(
                value["input_updates"]
            )
        )
    if "application_code_update" in value:
        out["ApplicationCodeUpdate"] = value["application_code_update"]
    if "output_updates" in value:
        import aws_sdk_kinesis_analytics.types.output_updates

        out["OutputUpdates"] = (
            aws_sdk_kinesis_analytics.types.output_updates.serialize_aws_json_1_1(
                value["output_updates"]
            )
        )
    if "reference_data_source_updates" in value:
        import aws_sdk_kinesis_analytics.types.reference_data_source_updates

        out["ReferenceDataSourceUpdates"] = (
            aws_sdk_kinesis_analytics.types.reference_data_source_updates.serialize_aws_json_1_1(
                value["reference_data_source_updates"]
            )
        )
    if "cloud_watch_logging_option_updates" in value:
        import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_updates

        out["CloudWatchLoggingOptionUpdates"] = (
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_updates.serialize_aws_json_1_1(
                value["cloud_watch_logging_option_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationUpdate:
    out: ApplicationUpdate = {}  # type: ignore[typeddict-item]
    if "InputUpdates" in data:
        import aws_sdk_kinesis_analytics.types.input_updates

        out["input_updates"] = (
            aws_sdk_kinesis_analytics.types.input_updates.deserialize_aws_json_1_1(
                data["InputUpdates"]
            )
        )
    if "ApplicationCodeUpdate" in data:
        out["application_code_update"] = data["ApplicationCodeUpdate"]
    if "OutputUpdates" in data:
        import aws_sdk_kinesis_analytics.types.output_updates

        out["output_updates"] = (
            aws_sdk_kinesis_analytics.types.output_updates.deserialize_aws_json_1_1(
                data["OutputUpdates"]
            )
        )
    if "ReferenceDataSourceUpdates" in data:
        import aws_sdk_kinesis_analytics.types.reference_data_source_updates

        out["reference_data_source_updates"] = (
            aws_sdk_kinesis_analytics.types.reference_data_source_updates.deserialize_aws_json_1_1(
                data["ReferenceDataSourceUpdates"]
            )
        )
    if "CloudWatchLoggingOptionUpdates" in data:
        import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_updates

        out["cloud_watch_logging_option_updates"] = (
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_updates.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptionUpdates"]
            )
        )
    return out
