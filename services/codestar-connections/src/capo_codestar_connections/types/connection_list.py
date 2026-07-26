"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_connections.types.connection

ConnectionList: TypeAlias = list[
    "capo_codestar_connections.types.connection.Connection"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionList) -> list:
    import capo_codestar_connections.types.connection

    out: list = []
    for item in value:
        out.append(
            capo_codestar_connections.types.connection.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConnectionList:
    import capo_codestar_connections.types.connection

    out: ConnectionList = []
    for item in data:
        out.append(
            capo_codestar_connections.types.connection.deserialize_aws_json_1_0(item)
        )
    return out
