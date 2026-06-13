"""Generated from Smithy shape ``com.amazonaws.backup#TieringConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.tiering_configurations_list_member

TieringConfigurationsList: TypeAlias = list[
    "aws_sdk_backup.types.tiering_configurations_list_member.TieringConfigurationsListMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: TieringConfigurationsList) -> list:
    import aws_sdk_backup.types.tiering_configurations_list_member

    out: list = []
    for item in value:
        out.append(
            aws_sdk_backup.types.tiering_configurations_list_member.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TieringConfigurationsList:
    import aws_sdk_backup.types.tiering_configurations_list_member

    out: TieringConfigurationsList = []
    for item in data:
        out.append(
            aws_sdk_backup.types.tiering_configurations_list_member.deserialize_json(
                item
            )
        )
    return out
