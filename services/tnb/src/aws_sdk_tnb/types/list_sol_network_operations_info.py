"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkOperationsInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.lcm_operation_type
    import aws_sdk_tnb.types.list_sol_network_operations_metadata
    import aws_sdk_tnb.types.ns_instance_id
    import aws_sdk_tnb.types.ns_lcm_op_occ_arn
    import aws_sdk_tnb.types.ns_lcm_op_occ_id
    import aws_sdk_tnb.types.ns_lcm_operation_state
    import aws_sdk_tnb.types.problem_details
    import aws_sdk_tnb.types.update_sol_network_type


class ListSolNetworkOperationsInfo(TypedDict):
    id: "aws_sdk_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId"
    """<p>ID of this network operation.</p>"""
    arn: "aws_sdk_tnb.types.ns_lcm_op_occ_arn.NsLcmOpOccArn"
    """<p>Network operation ARN.</p>"""
    operation_state: "aws_sdk_tnb.types.ns_lcm_operation_state.NsLcmOperationState"
    """<p>The state of the network operation.</p>"""
    ns_instance_id: "aws_sdk_tnb.types.ns_instance_id.NsInstanceId"
    """<p>ID of the network instance related to this operation.</p>"""
    lcm_operation_type: "aws_sdk_tnb.types.lcm_operation_type.LcmOperationType"
    """<p>Type of lifecycle management network operation.</p>"""
    update_type: NotRequired[
        "aws_sdk_tnb.types.update_sol_network_type.UpdateSolNetworkType"
    ]
    """<p>Type of the update. Only present if the network operation lcmOperationType is <code>UPDATE</code>.</p>"""
    error: NotRequired["aws_sdk_tnb.types.problem_details.ProblemDetails"]
    """<p>Error related to this specific network operation.</p>"""
    metadata: NotRequired[
        "aws_sdk_tnb.types.list_sol_network_operations_metadata.ListSolNetworkOperationsMetadata"
    ]
    """<p>Metadata related to this network operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkOperationsInfo) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_tnb.types.ns_lcm_operation_state

    out["operationState"] = aws_sdk_tnb.types.ns_lcm_operation_state.serialize_json(
        value["operation_state"]
    )
    out["nsInstanceId"] = value["ns_instance_id"]
    import aws_sdk_tnb.types.lcm_operation_type

    out["lcmOperationType"] = aws_sdk_tnb.types.lcm_operation_type.serialize_json(
        value["lcm_operation_type"]
    )
    if "update_type" in value:
        import aws_sdk_tnb.types.update_sol_network_type

        out["updateType"] = aws_sdk_tnb.types.update_sol_network_type.serialize_json(
            value["update_type"]
        )
    if "error" in value:
        import aws_sdk_tnb.types.problem_details

        out["error"] = aws_sdk_tnb.types.problem_details.serialize_json(value["error"])
    if "metadata" in value:
        import aws_sdk_tnb.types.list_sol_network_operations_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.list_sol_network_operations_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSolNetworkOperationsInfo:
    out: ListSolNetworkOperationsInfo = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ListSolNetworkOperationsInfo.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListSolNetworkOperationsInfo.arn required")
    if "operationState" in data:
        import aws_sdk_tnb.types.ns_lcm_operation_state

        out["operation_state"] = (
            aws_sdk_tnb.types.ns_lcm_operation_state.deserialize_json(
                data["operationState"]
            )
        )
    else:
        raise DeserializationError(
            "ListSolNetworkOperationsInfo.operation_state required"
        )
    if "nsInstanceId" in data:
        out["ns_instance_id"] = data["nsInstanceId"]
    else:
        raise DeserializationError(
            "ListSolNetworkOperationsInfo.ns_instance_id required"
        )
    if "lcmOperationType" in data:
        import aws_sdk_tnb.types.lcm_operation_type

        out["lcm_operation_type"] = (
            aws_sdk_tnb.types.lcm_operation_type.deserialize_json(
                data["lcmOperationType"]
            )
        )
    else:
        raise DeserializationError(
            "ListSolNetworkOperationsInfo.lcm_operation_type required"
        )
    if "updateType" in data:
        import aws_sdk_tnb.types.update_sol_network_type

        out["update_type"] = aws_sdk_tnb.types.update_sol_network_type.deserialize_json(
            data["updateType"]
        )
    if "error" in data:
        import aws_sdk_tnb.types.problem_details

        out["error"] = aws_sdk_tnb.types.problem_details.deserialize_json(data["error"])
    if "metadata" in data:
        import aws_sdk_tnb.types.list_sol_network_operations_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.list_sol_network_operations_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
