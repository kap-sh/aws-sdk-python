"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glue_run_configuration_input
    import aws_sdk_datazone.types.redshift_run_configuration_input
    import aws_sdk_datazone.types.sage_maker_run_configuration_input


class _DataSourceConfigurationInput_glueRunConfiguration(TypedDict):
    glueRunConfiguration: (
        "aws_sdk_datazone.types.glue_run_configuration_input.GlueRunConfigurationInput"
    )


class _DataSourceConfigurationInput_redshiftRunConfiguration(TypedDict):
    redshiftRunConfiguration: "aws_sdk_datazone.types.redshift_run_configuration_input.RedshiftRunConfigurationInput"


class _DataSourceConfigurationInput_sageMakerRunConfiguration(TypedDict):
    sageMakerRunConfiguration: "aws_sdk_datazone.types.sage_maker_run_configuration_input.SageMakerRunConfigurationInput"


DataSourceConfigurationInput: TypeAlias = (
    _DataSourceConfigurationInput_glueRunConfiguration
    | _DataSourceConfigurationInput_redshiftRunConfiguration
    | _DataSourceConfigurationInput_sageMakerRunConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfigurationInput) -> dict:
    if "glueRunConfiguration" in value:
        import aws_sdk_datazone.types.glue_run_configuration_input

        return {
            "glueRunConfiguration": aws_sdk_datazone.types.glue_run_configuration_input.serialize_json(
                value["glueRunConfiguration"]
            )
        }
    elif "redshiftRunConfiguration" in value:
        import aws_sdk_datazone.types.redshift_run_configuration_input

        return {
            "redshiftRunConfiguration": aws_sdk_datazone.types.redshift_run_configuration_input.serialize_json(
                value["redshiftRunConfiguration"]
            )
        }
    elif "sageMakerRunConfiguration" in value:
        import aws_sdk_datazone.types.sage_maker_run_configuration_input

        return {
            "sageMakerRunConfiguration": aws_sdk_datazone.types.sage_maker_run_configuration_input.serialize_json(
                value["sageMakerRunConfiguration"]
            )
        }
    else:
        raise SerializationError("DataSourceConfigurationInput: no variant present")


def deserialize_json(data: dict) -> DataSourceConfigurationInput:
    if "glueRunConfiguration" in data:
        import aws_sdk_datazone.types.glue_run_configuration_input

        return {
            "glueRunConfiguration": aws_sdk_datazone.types.glue_run_configuration_input.deserialize_json(
                data["glueRunConfiguration"]
            )
        }
    elif "redshiftRunConfiguration" in data:
        import aws_sdk_datazone.types.redshift_run_configuration_input

        return {
            "redshiftRunConfiguration": aws_sdk_datazone.types.redshift_run_configuration_input.deserialize_json(
                data["redshiftRunConfiguration"]
            )
        }
    elif "sageMakerRunConfiguration" in data:
        import aws_sdk_datazone.types.sage_maker_run_configuration_input

        return {
            "sageMakerRunConfiguration": aws_sdk_datazone.types.sage_maker_run_configuration_input.deserialize_json(
                data["sageMakerRunConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "DataSourceConfigurationInput: no recognized variant key"
        )
