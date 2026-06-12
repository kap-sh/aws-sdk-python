"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteInstanceProfileMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DeleteInstanceProfileMessage(TypedDict):
    instance_profile_identifier: (
        "aws_sdk_database_migration_service.types.string.String"
    )
    """<p>The identifier of the instance profile to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInstanceProfileMessage) -> dict:
    out: dict = {}
    out["InstanceProfileIdentifier"] = value["instance_profile_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInstanceProfileMessage:
    out: DeleteInstanceProfileMessage = {}  # type: ignore[typeddict-item]
    if "InstanceProfileIdentifier" in data:
        out["instance_profile_identifier"] = data["InstanceProfileIdentifier"]
    else:
        raise DeserializationError(
            "DeleteInstanceProfileMessage.instance_profile_identifier required"
        )
    return out
