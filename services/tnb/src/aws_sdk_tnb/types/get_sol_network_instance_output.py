"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkInstanceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.get_sol_network_instance_metadata
    import aws_sdk_tnb.types.lcm_operation_info
    import aws_sdk_tnb.types.ns_instance_arn
    import aws_sdk_tnb.types.ns_instance_id
    import aws_sdk_tnb.types.ns_state
    import aws_sdk_tnb.types.nsd_id
    import aws_sdk_tnb.types.nsd_info_id
    import aws_sdk_tnb.types.tag_map


class GetSolNetworkInstanceOutput(TypedDict):
    id: "aws_sdk_tnb.types.ns_instance_id.NsInstanceId"
    """<p>Network instance ID.</p>"""
    arn: "aws_sdk_tnb.types.ns_instance_arn.NsInstanceArn"
    """<p>Network instance ARN.</p>"""
    ns_instance_name: "str"
    """<p>Network instance name.</p>"""
    ns_instance_description: "str"
    """<p>Network instance description.</p>"""
    nsd_id: "aws_sdk_tnb.types.nsd_id.NsdId"
    """<p>Network service descriptor ID.</p>"""
    nsd_info_id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network service descriptor info ID.</p>"""
    ns_state: NotRequired["aws_sdk_tnb.types.ns_state.NsState"]
    """<p>Network instance state.</p>"""
    lcm_op_info: NotRequired["aws_sdk_tnb.types.lcm_operation_info.LcmOperationInfo"]
    metadata: "aws_sdk_tnb.types.get_sol_network_instance_metadata.GetSolNetworkInstanceMetadata"
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkInstanceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsInstanceName"] = value["ns_instance_name"]
    out["nsInstanceDescription"] = value["ns_instance_description"]
    out["nsdId"] = value["nsd_id"]
    out["nsdInfoId"] = value["nsd_info_id"]
    if "ns_state" in value:
        import aws_sdk_tnb.types.ns_state

        out["nsState"] = aws_sdk_tnb.types.ns_state.serialize_json(value["ns_state"])
    if "lcm_op_info" in value:
        import aws_sdk_tnb.types.lcm_operation_info

        out["lcmOpInfo"] = aws_sdk_tnb.types.lcm_operation_info.serialize_json(
            value["lcm_op_info"]
        )
    import aws_sdk_tnb.types.get_sol_network_instance_metadata

    out["metadata"] = (
        aws_sdk_tnb.types.get_sol_network_instance_metadata.serialize_json(
            value["metadata"]
        )
    )
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolNetworkInstanceOutput:
    out: GetSolNetworkInstanceOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSolNetworkInstanceOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSolNetworkInstanceOutput.arn required")
    if "nsInstanceName" in data:
        out["ns_instance_name"] = data["nsInstanceName"]
    else:
        raise DeserializationError(
            "GetSolNetworkInstanceOutput.ns_instance_name required"
        )
    if "nsInstanceDescription" in data:
        out["ns_instance_description"] = data["nsInstanceDescription"]
    else:
        raise DeserializationError(
            "GetSolNetworkInstanceOutput.ns_instance_description required"
        )
    if "nsdId" in data:
        out["nsd_id"] = data["nsdId"]
    else:
        raise DeserializationError("GetSolNetworkInstanceOutput.nsd_id required")
    if "nsdInfoId" in data:
        out["nsd_info_id"] = data["nsdInfoId"]
    else:
        raise DeserializationError("GetSolNetworkInstanceOutput.nsd_info_id required")
    if "nsState" in data:
        import aws_sdk_tnb.types.ns_state

        out["ns_state"] = aws_sdk_tnb.types.ns_state.deserialize_json(data["nsState"])
    if "lcmOpInfo" in data:
        import aws_sdk_tnb.types.lcm_operation_info

        out["lcm_op_info"] = aws_sdk_tnb.types.lcm_operation_info.deserialize_json(
            data["lcmOpInfo"]
        )
    if "metadata" in data:
        import aws_sdk_tnb.types.get_sol_network_instance_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.get_sol_network_instance_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("GetSolNetworkInstanceOutput.metadata required")
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out
