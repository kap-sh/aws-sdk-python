"""Generated from Smithy shape ``com.amazonaws.migrationhub#ApplicationStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub.types.application_state

ApplicationStateList: TypeAlias = list[
    "capo_migration_hub.types.application_state.ApplicationState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationStateList) -> list:
    import capo_migration_hub.types.application_state

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub.types.application_state.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationStateList:
    import capo_migration_hub.types.application_state

    out: ApplicationStateList = []
    for item in data:
        out.append(
            capo_migration_hub.types.application_state.deserialize_aws_json_1_1(item)
        )
    return out
