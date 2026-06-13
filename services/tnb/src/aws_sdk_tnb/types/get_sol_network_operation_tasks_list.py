"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkOperationTasksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_tnb.types.get_sol_network_operation_task_details

GetSolNetworkOperationTasksList: TypeAlias = list[
    "aws_sdk_tnb.types.get_sol_network_operation_task_details.GetSolNetworkOperationTaskDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkOperationTasksList) -> list:
    import aws_sdk_tnb.types.get_sol_network_operation_task_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_tnb.types.get_sol_network_operation_task_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetSolNetworkOperationTasksList:
    import aws_sdk_tnb.types.get_sol_network_operation_task_details

    out: GetSolNetworkOperationTasksList = []
    for item in data:
        out.append(
            aws_sdk_tnb.types.get_sol_network_operation_task_details.deserialize_json(
                item
            )
        )
    return out
