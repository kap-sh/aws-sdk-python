"""Generated from Smithy shape ``com.amazonaws.directconnect#ConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection

ConnectionList: TypeAlias = list["aws_sdk_direct_connect.types.connection.Connection"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionList) -> list:
    import aws_sdk_direct_connect.types.connection

    out: list = []
    for item in value:
        out.append(aws_sdk_direct_connect.types.connection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionList:
    import aws_sdk_direct_connect.types.connection

    out: ConnectionList = []
    for item in data:
        out.append(
            aws_sdk_direct_connect.types.connection.deserialize_aws_json_1_1(item)
        )
    return out
