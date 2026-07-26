"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ErrorDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_database_migration_service.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_database_migration_service.types.default_error_details


class _ErrorDetails_defaultErrorDetails(TypedDict, closed=True):
    defaultErrorDetails: "capo_database_migration_service.types.default_error_details.DefaultErrorDetails"


ErrorDetails: TypeAlias = _ErrorDetails_defaultErrorDetails


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorDetails) -> dict:
    if "defaultErrorDetails" in value:
        import capo_database_migration_service.types.default_error_details

        return {
            "defaultErrorDetails": capo_database_migration_service.types.default_error_details.serialize_aws_json_1_1(
                value["defaultErrorDetails"]
            )
        }
    else:
        raise SerializationError("ErrorDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ErrorDetails:
    if "defaultErrorDetails" in data:
        import capo_database_migration_service.types.default_error_details

        return {
            "defaultErrorDetails": capo_database_migration_service.types.default_error_details.deserialize_aws_json_1_1(
                data["defaultErrorDetails"]
            )
        }
    else:
        raise DeserializationError("ErrorDetails: no recognized variant key")
