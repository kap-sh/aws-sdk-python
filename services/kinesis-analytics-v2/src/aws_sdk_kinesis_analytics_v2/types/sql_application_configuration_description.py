"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SqlApplicationConfigurationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.input_descriptions
    import aws_sdk_kinesis_analytics_v2.types.output_descriptions
    import aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions


class SqlApplicationConfigurationDescription(TypedDict):
    input_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_descriptions.InputDescriptions"
    ]
    """<p>The array of <a>InputDescription</a> objects describing the input streams used by the application.</p>"""
    output_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.output_descriptions.OutputDescriptions"
    ]
    """<p>The array of <a>OutputDescription</a> objects describing the destination streams used by the application.</p>"""
    reference_data_source_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions.ReferenceDataSourceDescriptions"
    ]
    """<p>The array of <a>ReferenceDataSourceDescription</a> objects describing the reference data sources used by the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlApplicationConfigurationDescription) -> dict:
    out: dict = {}
    if "input_descriptions" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_descriptions

        out["InputDescriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.input_descriptions.serialize_aws_json_1_1(
                value["input_descriptions"]
            )
        )
    if "output_descriptions" in value:
        import aws_sdk_kinesis_analytics_v2.types.output_descriptions

        out["OutputDescriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.output_descriptions.serialize_aws_json_1_1(
                value["output_descriptions"]
            )
        )
    if "reference_data_source_descriptions" in value:
        import aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions

        out["ReferenceDataSourceDescriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions.serialize_aws_json_1_1(
                value["reference_data_source_descriptions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlApplicationConfigurationDescription:
    out: SqlApplicationConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "InputDescriptions" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_descriptions

        out["input_descriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.input_descriptions.deserialize_aws_json_1_1(
                data["InputDescriptions"]
            )
        )
    if "OutputDescriptions" in data:
        import aws_sdk_kinesis_analytics_v2.types.output_descriptions

        out["output_descriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.output_descriptions.deserialize_aws_json_1_1(
                data["OutputDescriptions"]
            )
        )
    if "ReferenceDataSourceDescriptions" in data:
        import aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions

        out["reference_data_source_descriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions.deserialize_aws_json_1_1(
                data["ReferenceDataSourceDescriptions"]
            )
        )
    return out
