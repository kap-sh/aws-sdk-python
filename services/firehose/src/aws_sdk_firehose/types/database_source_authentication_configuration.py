"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseSourceAuthenticationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.secrets_manager_configuration


class DatabaseSourceAuthenticationConfiguration(TypedDict):
    secrets_manager_configuration: "aws_sdk_firehose.types.secrets_manager_configuration.SecretsManagerConfiguration"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseSourceAuthenticationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_firehose.types.secrets_manager_configuration

    out["SecretsManagerConfiguration"] = (
        aws_sdk_firehose.types.secrets_manager_configuration.serialize_aws_json_1_1(
            value["secrets_manager_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseSourceAuthenticationConfiguration:
    out: DatabaseSourceAuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if "SecretsManagerConfiguration" in data:
        import aws_sdk_firehose.types.secrets_manager_configuration

        out["secrets_manager_configuration"] = (
            aws_sdk_firehose.types.secrets_manager_configuration.deserialize_aws_json_1_1(
                data["SecretsManagerConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DatabaseSourceAuthenticationConfiguration.secrets_manager_configuration required"
        )
    return out
