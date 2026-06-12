"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ConnectionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.connection_type

ConnectionTypeList: TypeAlias = list[
    "aws_sdk_connectparticipant.types.connection_type.ConnectionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionTypeList) -> list:
    import aws_sdk_connectparticipant.types.connection_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectparticipant.types.connection_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConnectionTypeList:
    import aws_sdk_connectparticipant.types.connection_type

    out: ConnectionTypeList = []
    for item in data:
        out.append(
            aws_sdk_connectparticipant.types.connection_type.deserialize_json(item)
        )
    return out
