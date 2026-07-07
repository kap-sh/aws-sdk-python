"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyInstanceProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.instance_profile


class ModifyInstanceProfileResponse(TypedDict, closed=True):
    instance_profile: NotRequired[
        "aws_sdk_database_migration_service.types.instance_profile.InstanceProfile"
    ]
    """<p>The instance profile that was modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyInstanceProfileResponse) -> dict:
    out: dict = {}
    if "instance_profile" in value:
        import aws_sdk_database_migration_service.types.instance_profile

        out["InstanceProfile"] = (
            aws_sdk_database_migration_service.types.instance_profile.serialize_aws_json_1_1(
                value["instance_profile"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyInstanceProfileResponse:
    out: ModifyInstanceProfileResponse = {}  # type: ignore[typeddict-item]
    if "InstanceProfile" in data:
        import aws_sdk_database_migration_service.types.instance_profile

        out["instance_profile"] = (
            aws_sdk_database_migration_service.types.instance_profile.deserialize_aws_json_1_1(
                data["InstanceProfile"]
            )
        )
    return out
