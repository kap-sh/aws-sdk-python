"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkOperationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.get_sol_network_operation_metadata
    import aws_sdk_tnb.types.get_sol_network_operation_tasks_list
    import aws_sdk_tnb.types.lcm_operation_type
    import aws_sdk_tnb.types.ns_instance_id
    import aws_sdk_tnb.types.ns_lcm_op_occ_arn
    import aws_sdk_tnb.types.ns_lcm_op_occ_id
    import aws_sdk_tnb.types.ns_lcm_operation_state
    import aws_sdk_tnb.types.problem_details
    import aws_sdk_tnb.types.tag_map
    import aws_sdk_tnb.types.update_sol_network_type


class GetSolNetworkOperationOutput(TypedDict, closed=True):
    id: NotRequired["aws_sdk_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId"]
    """<p>ID of this network operation occurrence.</p>"""
    arn: "aws_sdk_tnb.types.ns_lcm_op_occ_arn.NsLcmOpOccArn"
    """<p>Network operation ARN.</p>"""
    operation_state: NotRequired[
        "aws_sdk_tnb.types.ns_lcm_operation_state.NsLcmOperationState"
    ]
    """<p>The state of the network operation.</p>"""
    ns_instance_id: NotRequired["aws_sdk_tnb.types.ns_instance_id.NsInstanceId"]
    """<p>ID of the network operation instance.</p>"""
    lcm_operation_type: NotRequired[
        "aws_sdk_tnb.types.lcm_operation_type.LcmOperationType"
    ]
    """<p>Type of the operation represented by this occurrence.</p>"""
    update_type: NotRequired[
        "aws_sdk_tnb.types.update_sol_network_type.UpdateSolNetworkType"
    ]
    """<p>Type of the update. Only present if the network operation lcmOperationType is <code>UPDATE</code>.</p>"""
    error: NotRequired["aws_sdk_tnb.types.problem_details.ProblemDetails"]
    """<p>Error related to this specific network operation occurrence.</p>"""
    metadata: NotRequired[
        "aws_sdk_tnb.types.get_sol_network_operation_metadata.GetSolNetworkOperationMetadata"
    ]
    """<p>Metadata of this network operation occurrence.</p>"""
    tasks: NotRequired[
        "aws_sdk_tnb.types.get_sol_network_operation_tasks_list.GetSolNetworkOperationTasksList"
    ]
    """<p>All tasks associated with this operation occurrence.</p>"""
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkOperationOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "operation_state" in value:
        import aws_sdk_tnb.types.ns_lcm_operation_state

        out["operationState"] = aws_sdk_tnb.types.ns_lcm_operation_state.serialize_json(
            value["operation_state"]
        )
    if "ns_instance_id" in value:
        out["nsInstanceId"] = value["ns_instance_id"]
    if "lcm_operation_type" in value:
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
        import aws_sdk_tnb.types.get_sol_network_operation_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.get_sol_network_operation_metadata.serialize_json(
                value["metadata"]
            )
        )
    if "tasks" in value:
        import aws_sdk_tnb.types.get_sol_network_operation_tasks_list

        out["tasks"] = (
            aws_sdk_tnb.types.get_sol_network_operation_tasks_list.serialize_json(
                value["tasks"]
            )
        )
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolNetworkOperationOutput:
    out: GetSolNetworkOperationOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSolNetworkOperationOutput.arn required")
    if "operationState" in data:
        import aws_sdk_tnb.types.ns_lcm_operation_state

        out["operation_state"] = (
            aws_sdk_tnb.types.ns_lcm_operation_state.deserialize_json(
                data["operationState"]
            )
        )
    if "nsInstanceId" in data:
        out["ns_instance_id"] = data["nsInstanceId"]
    if "lcmOperationType" in data:
        import aws_sdk_tnb.types.lcm_operation_type

        out["lcm_operation_type"] = (
            aws_sdk_tnb.types.lcm_operation_type.deserialize_json(
                data["lcmOperationType"]
            )
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
        import aws_sdk_tnb.types.get_sol_network_operation_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.get_sol_network_operation_metadata.deserialize_json(
                data["metadata"]
            )
        )
    if "tasks" in data:
        import aws_sdk_tnb.types.get_sol_network_operation_tasks_list

        out["tasks"] = (
            aws_sdk_tnb.types.get_sol_network_operation_tasks_list.deserialize_json(
                data["tasks"]
            )
        )
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out
