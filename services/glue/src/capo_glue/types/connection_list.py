"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.connection

ConnectionList: TypeAlias = list["capo_glue.types.connection.Connection"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionList) -> list:
    import capo_glue.types.connection

    out: list = []
    for item in value:
        out.append(capo_glue.types.connection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionList:
    import capo_glue.types.connection

    out: ConnectionList = []
    for item in data:
        out.append(capo_glue.types.connection.deserialize_aws_json_1_1(item))
    return out
