"""Generated from Smithy shape ``com.amazonaws.athena#DatabaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.database

DatabaseList: TypeAlias = list["aws_sdk_athena.types.database.Database"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseList) -> list:
    import aws_sdk_athena.types.database

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.database.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DatabaseList:
    import aws_sdk_athena.types.database

    out: DatabaseList = []
    for item in data:
        out.append(aws_sdk_athena.types.database.deserialize_aws_json_1_1(item))
    return out
