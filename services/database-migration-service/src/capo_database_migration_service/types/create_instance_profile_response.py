"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateInstanceProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.instance_profile


class CreateInstanceProfileResponse(TypedDict, closed=True):
    instance_profile: NotRequired[
        "capo_database_migration_service.types.instance_profile.InstanceProfile"
    ]
    """<p>The instance profile that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInstanceProfileResponse) -> dict:
    out: dict = {}
    if "instance_profile" in value:
        import capo_database_migration_service.types.instance_profile

        out["InstanceProfile"] = (
            capo_database_migration_service.types.instance_profile.serialize_aws_json_1_1(
                value["instance_profile"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInstanceProfileResponse:
    out: CreateInstanceProfileResponse = {}  # type: ignore[typeddict-item]
    if "InstanceProfile" in data:
        import capo_database_migration_service.types.instance_profile

        out["instance_profile"] = (
            capo_database_migration_service.types.instance_profile.deserialize_aws_json_1_1(
                data["InstanceProfile"]
            )
        )
    return out
