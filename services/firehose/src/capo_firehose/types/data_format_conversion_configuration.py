"""Generated from Smithy shape ``com.amazonaws.firehose#DataFormatConversionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.input_format_configuration
    import capo_firehose.types.output_format_configuration
    import capo_firehose.types.schema_configuration


class DataFormatConversionConfiguration(TypedDict, closed=True):
    schema_configuration: NotRequired[
        "capo_firehose.types.schema_configuration.SchemaConfiguration"
    ]
    """<p>Specifies the Amazon Web Services Glue Data Catalog table that contains the column information. This parameter is required if <code>Enabled</code> is set to true.</p>"""
    input_format_configuration: NotRequired[
        "capo_firehose.types.input_format_configuration.InputFormatConfiguration"
    ]
    """<p>Specifies the deserializer that you want Firehose to use to convert the format of your data from JSON. This parameter is required if <code>Enabled</code> is set to true.</p>"""
    output_format_configuration: NotRequired[
        "capo_firehose.types.output_format_configuration.OutputFormatConfiguration"
    ]
    """<p>Specifies the serializer that you want Firehose to use to convert the format of your data to the Parquet or ORC format. This parameter is required if <code>Enabled</code> is set to true.</p>"""
    enabled: NotRequired["capo_firehose.types.boolean_object.BooleanObject"]
    """<p>Defaults to <code>true</code>. Set it to <code>false</code> if you want to disable format conversion while preserving the configuration details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataFormatConversionConfiguration) -> dict:
    out: dict = {}
    if "schema_configuration" in value:
        import capo_firehose.types.schema_configuration

        out["SchemaConfiguration"] = (
            capo_firehose.types.schema_configuration.serialize_aws_json_1_1(
                value["schema_configuration"]
            )
        )
    if "input_format_configuration" in value:
        import capo_firehose.types.input_format_configuration

        out["InputFormatConfiguration"] = (
            capo_firehose.types.input_format_configuration.serialize_aws_json_1_1(
                value["input_format_configuration"]
            )
        )
    if "output_format_configuration" in value:
        import capo_firehose.types.output_format_configuration

        out["OutputFormatConfiguration"] = (
            capo_firehose.types.output_format_configuration.serialize_aws_json_1_1(
                value["output_format_configuration"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataFormatConversionConfiguration:
    out: DataFormatConversionConfiguration = {}  # type: ignore[typeddict-item]
    if "SchemaConfiguration" in data:
        import capo_firehose.types.schema_configuration

        out["schema_configuration"] = (
            capo_firehose.types.schema_configuration.deserialize_aws_json_1_1(
                data["SchemaConfiguration"]
            )
        )
    if "InputFormatConfiguration" in data:
        import capo_firehose.types.input_format_configuration

        out["input_format_configuration"] = (
            capo_firehose.types.input_format_configuration.deserialize_aws_json_1_1(
                data["InputFormatConfiguration"]
            )
        )
    if "OutputFormatConfiguration" in data:
        import capo_firehose.types.output_format_configuration

        out["output_format_configuration"] = (
            capo_firehose.types.output_format_configuration.deserialize_aws_json_1_1(
                data["OutputFormatConfiguration"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
