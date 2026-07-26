"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseCharacterSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_character_set_summary

AutonomousDatabaseCharacterSetList: TypeAlias = list[
    "capo_odb.types.autonomous_database_character_set_summary.AutonomousDatabaseCharacterSetSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseCharacterSetList) -> list:
    import capo_odb.types.autonomous_database_character_set_summary

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.autonomous_database_character_set_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutonomousDatabaseCharacterSetList:
    import capo_odb.types.autonomous_database_character_set_summary

    out: AutonomousDatabaseCharacterSetList = []
    for item in data:
        out.append(
            capo_odb.types.autonomous_database_character_set_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
