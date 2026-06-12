"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.relational_database

RelationalDatabaseList: TypeAlias = list[
    "aws_sdk_lightsail.types.relational_database.RelationalDatabase"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseList) -> list:
    import aws_sdk_lightsail.types.relational_database

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.relational_database.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RelationalDatabaseList:
    import aws_sdk_lightsail.types.relational_database

    out: RelationalDatabaseList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.relational_database.deserialize_aws_json_1_1(item)
        )
    return out
