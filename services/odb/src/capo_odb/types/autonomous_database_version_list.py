"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_version_summary

AutonomousDatabaseVersionList: TypeAlias = list[
    "capo_odb.types.autonomous_database_version_summary.AutonomousDatabaseVersionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseVersionList) -> list:
    import capo_odb.types.autonomous_database_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.autonomous_database_version_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutonomousDatabaseVersionList:
    import capo_odb.types.autonomous_database_version_summary

    out: AutonomousDatabaseVersionList = []
    for item in data:
        out.append(
            capo_odb.types.autonomous_database_version_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
