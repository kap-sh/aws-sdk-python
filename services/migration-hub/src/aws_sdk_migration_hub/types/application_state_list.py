"""Generated from Smithy shape ``com.amazonaws.migrationhub#ApplicationStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.application_state

ApplicationStateList: TypeAlias = list[
    "aws_sdk_migration_hub.types.application_state.ApplicationState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationStateList) -> list:
    import aws_sdk_migration_hub.types.application_state

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migration_hub.types.application_state.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationStateList:
    import aws_sdk_migration_hub.types.application_state

    out: ApplicationStateList = []
    for item in data:
        out.append(
            aws_sdk_migration_hub.types.application_state.deserialize_aws_json_1_1(item)
        )
    return out
