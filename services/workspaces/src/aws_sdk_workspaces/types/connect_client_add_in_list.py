"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectClientAddInList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connect_client_add_in

ConnectClientAddInList: TypeAlias = list[
    "aws_sdk_workspaces.types.connect_client_add_in.ConnectClientAddIn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectClientAddInList) -> list:
    import aws_sdk_workspaces.types.connect_client_add_in

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.connect_client_add_in.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectClientAddInList:
    import aws_sdk_workspaces.types.connect_client_add_in

    out: ConnectClientAddInList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.connect_client_add_in.deserialize_aws_json_1_1(
                item
            )
        )
    return out
