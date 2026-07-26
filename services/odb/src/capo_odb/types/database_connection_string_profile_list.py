"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseConnectionStringProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.database_connection_string_profile

DatabaseConnectionStringProfileList: TypeAlias = list[
    "capo_odb.types.database_connection_string_profile.DatabaseConnectionStringProfile"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseConnectionStringProfileList) -> list:
    import capo_odb.types.database_connection_string_profile

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.database_connection_string_profile.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DatabaseConnectionStringProfileList:
    import capo_odb.types.database_connection_string_profile

    out: DatabaseConnectionStringProfileList = []
    for item in data:
        out.append(
            capo_odb.types.database_connection_string_profile.deserialize_aws_json_1_0(
                item
            )
        )
    return out
