"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.connection

ConnectionResponseList: TypeAlias = list["capo_eventbridge.types.connection.Connection"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionResponseList) -> list:
    import capo_eventbridge.types.connection

    out: list = []
    for item in value:
        out.append(capo_eventbridge.types.connection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionResponseList:
    import capo_eventbridge.types.connection

    out: ConnectionResponseList = []
    for item in data:
        out.append(capo_eventbridge.types.connection.deserialize_aws_json_1_1(item))
    return out
