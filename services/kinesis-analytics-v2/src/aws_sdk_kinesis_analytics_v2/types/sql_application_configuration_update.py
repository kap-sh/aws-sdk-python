"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SqlApplicationConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.input_updates
    import aws_sdk_kinesis_analytics_v2.types.output_updates
    import aws_sdk_kinesis_analytics_v2.types.reference_data_source_updates


class SqlApplicationConfigurationUpdate(TypedDict, closed=True):
    input_updates: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_updates.InputUpdates"
    ]
    """<p>The array of <a>InputUpdate</a> objects describing the new input streams used by the application.</p>"""
    output_updates: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.output_updates.OutputUpdates"
    ]
    """<p>The array of <a>OutputUpdate</a> objects describing the new destination streams used by the application.</p>"""
    reference_data_source_updates: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.reference_data_source_updates.ReferenceDataSourceUpdates"
    ]
    """<p>The array of <a>ReferenceDataSourceUpdate</a> objects describing the new reference data sources used by the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlApplicationConfigurationUpdate) -> dict:
    out: dict = {}
    if "input_updates" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_updates

        out["InputUpdates"] = (
            aws_sdk_kinesis_analytics_v2.types.input_updates.serialize_aws_json_1_1(
                value["input_updates"]
            )
        )
    if "output_updates" in value:
        import aws_sdk_kinesis_analytics_v2.types.output_updates

        out["OutputUpdates"] = (
            aws_sdk_kinesis_analytics_v2.types.output_updates.serialize_aws_json_1_1(
                value["output_updates"]
            )
        )
    if "reference_data_source_updates" in value:
        import aws_sdk_kinesis_analytics_v2.types.reference_data_source_updates

        out["ReferenceDataSourceUpdates"] = (
            aws_sdk_kinesis_analytics_v2.types.reference_data_source_updates.serialize_aws_json_1_1(
                value["reference_data_source_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlApplicationConfigurationUpdate:
    out: SqlApplicationConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "InputUpdates" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_updates

        out["input_updates"] = (
            aws_sdk_kinesis_analytics_v2.types.input_updates.deserialize_aws_json_1_1(
                data["InputUpdates"]
            )
        )
    if "OutputUpdates" in data:
        import aws_sdk_kinesis_analytics_v2.types.output_updates

        out["output_updates"] = (
            aws_sdk_kinesis_analytics_v2.types.output_updates.deserialize_aws_json_1_1(
                data["OutputUpdates"]
            )
        )
    if "ReferenceDataSourceUpdates" in data:
        import aws_sdk_kinesis_analytics_v2.types.reference_data_source_updates

        out["reference_data_source_updates"] = (
            aws_sdk_kinesis_analytics_v2.types.reference_data_source_updates.deserialize_aws_json_1_1(
                data["ReferenceDataSourceUpdates"]
            )
        )
    return out
