"""Generated from Smithy shape ``com.amazonaws.mailmanager#ExportDestinationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.s3_export_destination_configuration


class _ExportDestinationConfiguration_S3(TypedDict, closed=True):
    S3: "capo_mailmanager.types.s3_export_destination_configuration.S3ExportDestinationConfiguration"


ExportDestinationConfiguration: TypeAlias = _ExportDestinationConfiguration_S3


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportDestinationConfiguration) -> dict:
    if "S3" in value:
        import capo_mailmanager.types.s3_export_destination_configuration

        return {
            "S3": capo_mailmanager.types.s3_export_destination_configuration.serialize_aws_json_1_0(
                value["S3"]
            )
        }
    else:
        raise SerializationError("ExportDestinationConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ExportDestinationConfiguration:
    if "S3" in data:
        import capo_mailmanager.types.s3_export_destination_configuration

        return {
            "S3": capo_mailmanager.types.s3_export_destination_configuration.deserialize_aws_json_1_0(
                data["S3"]
            )
        }
    else:
        raise DeserializationError(
            "ExportDestinationConfiguration: no recognized variant key"
        )
