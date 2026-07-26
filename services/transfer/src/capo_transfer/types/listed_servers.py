"""Generated from Smithy shape ``com.amazonaws.transfer#ListedServers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.listed_server

ListedServers: TypeAlias = list["capo_transfer.types.listed_server.ListedServer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedServers) -> list:
    import capo_transfer.types.listed_server

    out: list = []
    for item in value:
        out.append(capo_transfer.types.listed_server.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedServers:
    import capo_transfer.types.listed_server

    out: ListedServers = []
    for item in data:
        out.append(capo_transfer.types.listed_server.deserialize_aws_json_1_1(item))
    return out
