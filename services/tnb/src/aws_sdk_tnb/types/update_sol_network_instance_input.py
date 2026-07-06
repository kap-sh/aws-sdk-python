"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.ns_instance_id
    import aws_sdk_tnb.types.tag_map
    import aws_sdk_tnb.types.update_sol_network_modify
    import aws_sdk_tnb.types.update_sol_network_service_data
    import aws_sdk_tnb.types.update_sol_network_type


class UpdateSolNetworkInstanceInput(TypedDict, closed=True):
    ns_instance_id: "aws_sdk_tnb.types.ns_instance_id.NsInstanceId"
    """<p>ID of the network instance.</p>"""
    update_type: "aws_sdk_tnb.types.update_sol_network_type.UpdateSolNetworkType"
    """<p>The type of update.</p> <ul> <li> <p>Use the <code>MODIFY_VNF_INFORMATION</code> update type, to update a specific network function configuration, in the network instance.</p> </li> <li> <p>Use the <code>UPDATE_NS</code> update type, to update the network instance to a new network service descriptor.</p> </li> </ul>"""
    modify_vnf_info_data: NotRequired[
        "aws_sdk_tnb.types.update_sol_network_modify.UpdateSolNetworkModify"
    ]
    """<p>Identifies the network function information parameters and/or the configurable properties of the network function to be modified.</p> <p>Include this property only if the update type is <code>MODIFY_VNF_INFORMATION</code>.</p>"""
    update_ns: NotRequired[
        "aws_sdk_tnb.types.update_sol_network_service_data.UpdateSolNetworkServiceData"
    ]
    """<p>Identifies the network service descriptor and the configurable properties of the descriptor, to be used for the update.</p> <p>Include this property only if the update type is <code>UPDATE_NS</code>.</p>"""
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkInstanceInput) -> dict:
    out: dict = {}
    import aws_sdk_tnb.types.update_sol_network_type

    out["updateType"] = aws_sdk_tnb.types.update_sol_network_type.serialize_json(
        value["update_type"]
    )
    if "modify_vnf_info_data" in value:
        import aws_sdk_tnb.types.update_sol_network_modify

        out["modifyVnfInfoData"] = (
            aws_sdk_tnb.types.update_sol_network_modify.serialize_json(
                value["modify_vnf_info_data"]
            )
        )
    if "update_ns" in value:
        import aws_sdk_tnb.types.update_sol_network_service_data

        out["updateNs"] = (
            aws_sdk_tnb.types.update_sol_network_service_data.serialize_json(
                value["update_ns"]
            )
        )
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateSolNetworkInstanceInput:
    out: UpdateSolNetworkInstanceInput = {}  # type: ignore[typeddict-item]
    if "updateType" in data:
        import aws_sdk_tnb.types.update_sol_network_type

        out["update_type"] = aws_sdk_tnb.types.update_sol_network_type.deserialize_json(
            data["updateType"]
        )
    else:
        raise DeserializationError("UpdateSolNetworkInstanceInput.update_type required")
    if "modifyVnfInfoData" in data:
        import aws_sdk_tnb.types.update_sol_network_modify

        out["modify_vnf_info_data"] = (
            aws_sdk_tnb.types.update_sol_network_modify.deserialize_json(
                data["modifyVnfInfoData"]
            )
        )
    if "updateNs" in data:
        import aws_sdk_tnb.types.update_sol_network_service_data

        out["update_ns"] = (
            aws_sdk_tnb.types.update_sol_network_service_data.deserialize_json(
                data["updateNs"]
            )
        )
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out
