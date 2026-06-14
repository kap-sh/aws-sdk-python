"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceConfigurationOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glue_run_configuration_output
    import aws_sdk_datazone.types.redshift_run_configuration_output
    import aws_sdk_datazone.types.sage_maker_run_configuration_output


class _DataSourceConfigurationOutput_glueRunConfiguration(TypedDict):
    glueRunConfiguration: "aws_sdk_datazone.types.glue_run_configuration_output.GlueRunConfigurationOutput"


class _DataSourceConfigurationOutput_redshiftRunConfiguration(TypedDict):
    redshiftRunConfiguration: "aws_sdk_datazone.types.redshift_run_configuration_output.RedshiftRunConfigurationOutput"


class _DataSourceConfigurationOutput_sageMakerRunConfiguration(TypedDict):
    sageMakerRunConfiguration: "aws_sdk_datazone.types.sage_maker_run_configuration_output.SageMakerRunConfigurationOutput"


DataSourceConfigurationOutput: TypeAlias = (
    _DataSourceConfigurationOutput_glueRunConfiguration
    | _DataSourceConfigurationOutput_redshiftRunConfiguration
    | _DataSourceConfigurationOutput_sageMakerRunConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfigurationOutput) -> dict:
    if "glueRunConfiguration" in value:
        import aws_sdk_datazone.types.glue_run_configuration_output

        return {
            "glueRunConfiguration": aws_sdk_datazone.types.glue_run_configuration_output.serialize_json(
                value["glueRunConfiguration"]
            )
        }
    elif "redshiftRunConfiguration" in value:
        import aws_sdk_datazone.types.redshift_run_configuration_output

        return {
            "redshiftRunConfiguration": aws_sdk_datazone.types.redshift_run_configuration_output.serialize_json(
                value["redshiftRunConfiguration"]
            )
        }
    elif "sageMakerRunConfiguration" in value:
        import aws_sdk_datazone.types.sage_maker_run_configuration_output

        return {
            "sageMakerRunConfiguration": aws_sdk_datazone.types.sage_maker_run_configuration_output.serialize_json(
                value["sageMakerRunConfiguration"]
            )
        }
    else:
        raise SerializationError("DataSourceConfigurationOutput: no variant present")


def deserialize_json(data: dict) -> DataSourceConfigurationOutput:
    if "glueRunConfiguration" in data:
        import aws_sdk_datazone.types.glue_run_configuration_output

        return {
            "glueRunConfiguration": aws_sdk_datazone.types.glue_run_configuration_output.deserialize_json(
                data["glueRunConfiguration"]
            )
        }
    elif "redshiftRunConfiguration" in data:
        import aws_sdk_datazone.types.redshift_run_configuration_output

        return {
            "redshiftRunConfiguration": aws_sdk_datazone.types.redshift_run_configuration_output.deserialize_json(
                data["redshiftRunConfiguration"]
            )
        }
    elif "sageMakerRunConfiguration" in data:
        import aws_sdk_datazone.types.sage_maker_run_configuration_output

        return {
            "sageMakerRunConfiguration": aws_sdk_datazone.types.sage_maker_run_configuration_output.deserialize_json(
                data["sageMakerRunConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "DataSourceConfigurationOutput: no recognized variant key"
        )
