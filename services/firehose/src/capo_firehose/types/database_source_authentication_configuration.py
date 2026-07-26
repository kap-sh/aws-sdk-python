"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseSourceAuthenticationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.secrets_manager_configuration


class DatabaseSourceAuthenticationConfiguration(TypedDict, closed=True):
    secrets_manager_configuration: (
        "capo_firehose.types.secrets_manager_configuration.SecretsManagerConfiguration"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseSourceAuthenticationConfiguration) -> dict:
    out: dict = {}
    import capo_firehose.types.secrets_manager_configuration

    out["SecretsManagerConfiguration"] = (
        capo_firehose.types.secrets_manager_configuration.serialize_aws_json_1_1(
            value["secrets_manager_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseSourceAuthenticationConfiguration:
    out: DatabaseSourceAuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if "SecretsManagerConfiguration" in data:
        import capo_firehose.types.secrets_manager_configuration

        out["secrets_manager_configuration"] = (
            capo_firehose.types.secrets_manager_configuration.deserialize_aws_json_1_1(
                data["SecretsManagerConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DatabaseSourceAuthenticationConfiguration.secrets_manager_configuration required"
        )
    return out
