"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftRunConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.redshift_credential_configuration
    import aws_sdk_datazone.types.redshift_storage
    import aws_sdk_datazone.types.relational_filter_configurations


class RedshiftRunConfigurationInput(TypedDict, closed=True):
    data_access_role: NotRequired["str"]
    """<p>The data access role included in the configuration details of the Amazon Redshift data source.</p>"""
    relational_filter_configurations: "aws_sdk_datazone.types.relational_filter_configurations.RelationalFilterConfigurations"
    """<p>The relational filger configurations included in the configuration details of the Amazon Redshift data source.</p>"""
    redshift_credential_configuration: NotRequired[
        "aws_sdk_datazone.types.redshift_credential_configuration.RedshiftCredentialConfiguration"
    ]
    redshift_storage: NotRequired[
        "aws_sdk_datazone.types.redshift_storage.RedshiftStorage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftRunConfigurationInput) -> dict:
    out: dict = {}
    if "data_access_role" in value:
        out["dataAccessRole"] = value["data_access_role"]
    import aws_sdk_datazone.types.relational_filter_configurations

    out["relationalFilterConfigurations"] = (
        aws_sdk_datazone.types.relational_filter_configurations.serialize_json(
            value["relational_filter_configurations"]
        )
    )
    if "redshift_credential_configuration" in value:
        import aws_sdk_datazone.types.redshift_credential_configuration

        out["redshiftCredentialConfiguration"] = (
            aws_sdk_datazone.types.redshift_credential_configuration.serialize_json(
                value["redshift_credential_configuration"]
            )
        )
    if "redshift_storage" in value:
        import aws_sdk_datazone.types.redshift_storage

        out["redshiftStorage"] = aws_sdk_datazone.types.redshift_storage.serialize_json(
            value["redshift_storage"]
        )
    return out


def deserialize_json(data: dict) -> RedshiftRunConfigurationInput:
    out: RedshiftRunConfigurationInput = {}  # type: ignore[typeddict-item]
    if "dataAccessRole" in data:
        out["data_access_role"] = data["dataAccessRole"]
    if "relationalFilterConfigurations" in data:
        import aws_sdk_datazone.types.relational_filter_configurations

        out["relational_filter_configurations"] = (
            aws_sdk_datazone.types.relational_filter_configurations.deserialize_json(
                data["relationalFilterConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftRunConfigurationInput.relational_filter_configurations required"
        )
    if "redshiftCredentialConfiguration" in data:
        import aws_sdk_datazone.types.redshift_credential_configuration

        out["redshift_credential_configuration"] = (
            aws_sdk_datazone.types.redshift_credential_configuration.deserialize_json(
                data["redshiftCredentialConfiguration"]
            )
        )
    if "redshiftStorage" in data:
        import aws_sdk_datazone.types.redshift_storage

        out["redshift_storage"] = (
            aws_sdk_datazone.types.redshift_storage.deserialize_json(
                data["redshiftStorage"]
            )
        )
    return out
