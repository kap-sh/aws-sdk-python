"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkInstanceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_network_instance_metadata
    import aws_sdk_tnb.types.ns_instance_arn
    import aws_sdk_tnb.types.ns_instance_id
    import aws_sdk_tnb.types.ns_state
    import aws_sdk_tnb.types.nsd_id
    import aws_sdk_tnb.types.nsd_info_id


class ListSolNetworkInstanceInfo(TypedDict, closed=True):
    id: "aws_sdk_tnb.types.ns_instance_id.NsInstanceId"
    """<p>ID of the network instance.</p>"""
    arn: "aws_sdk_tnb.types.ns_instance_arn.NsInstanceArn"
    """<p>Network instance ARN.</p>"""
    ns_instance_name: "str"
    """<p>Human-readable name of the network instance.</p>"""
    ns_instance_description: "str"
    """<p>Human-readable description of the network instance.</p>"""
    nsd_id: "aws_sdk_tnb.types.nsd_id.NsdId"
    """<p>ID of the network service descriptor in the network package.</p>"""
    nsd_info_id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor in the network package.</p>"""
    ns_state: "aws_sdk_tnb.types.ns_state.NsState"
    """<p>The state of the network instance.</p>"""
    metadata: "aws_sdk_tnb.types.list_sol_network_instance_metadata.ListSolNetworkInstanceMetadata"
    """<p>The metadata of the network instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkInstanceInfo) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsInstanceName"] = value["ns_instance_name"]
    out["nsInstanceDescription"] = value["ns_instance_description"]
    out["nsdId"] = value["nsd_id"]
    out["nsdInfoId"] = value["nsd_info_id"]
    import aws_sdk_tnb.types.ns_state

    out["nsState"] = aws_sdk_tnb.types.ns_state.serialize_json(value["ns_state"])
    import aws_sdk_tnb.types.list_sol_network_instance_metadata

    out["metadata"] = (
        aws_sdk_tnb.types.list_sol_network_instance_metadata.serialize_json(
            value["metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListSolNetworkInstanceInfo:
    out: ListSolNetworkInstanceInfo = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ListSolNetworkInstanceInfo.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListSolNetworkInstanceInfo.arn required")
    if "nsInstanceName" in data:
        out["ns_instance_name"] = data["nsInstanceName"]
    else:
        raise DeserializationError(
            "ListSolNetworkInstanceInfo.ns_instance_name required"
        )
    if "nsInstanceDescription" in data:
        out["ns_instance_description"] = data["nsInstanceDescription"]
    else:
        raise DeserializationError(
            "ListSolNetworkInstanceInfo.ns_instance_description required"
        )
    if "nsdId" in data:
        out["nsd_id"] = data["nsdId"]
    else:
        raise DeserializationError("ListSolNetworkInstanceInfo.nsd_id required")
    if "nsdInfoId" in data:
        out["nsd_info_id"] = data["nsdInfoId"]
    else:
        raise DeserializationError("ListSolNetworkInstanceInfo.nsd_info_id required")
    if "nsState" in data:
        import aws_sdk_tnb.types.ns_state

        out["ns_state"] = aws_sdk_tnb.types.ns_state.deserialize_json(data["nsState"])
    else:
        raise DeserializationError("ListSolNetworkInstanceInfo.ns_state required")
    if "metadata" in data:
        import aws_sdk_tnb.types.list_sol_network_instance_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.list_sol_network_instance_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("ListSolNetworkInstanceInfo.metadata required")
    return out
