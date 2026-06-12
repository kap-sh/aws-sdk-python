"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.relational_database_parameter

RelationalDatabaseParameterList: TypeAlias = list[
    "aws_sdk_lightsail.types.relational_database_parameter.RelationalDatabaseParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseParameterList) -> list:
    import aws_sdk_lightsail.types.relational_database_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.relational_database_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RelationalDatabaseParameterList:
    import aws_sdk_lightsail.types.relational_database_parameter

    out: RelationalDatabaseParameterList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.relational_database_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
