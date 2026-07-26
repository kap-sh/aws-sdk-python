"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkOperationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_tnb.types.instantiate_metadata
    import capo_tnb.types.modify_vnf_info_metadata
    import capo_tnb.types.update_ns_metadata


class GetSolNetworkOperationMetadata(TypedDict, closed=True):
    update_ns_metadata: NotRequired[
        "capo_tnb.types.update_ns_metadata.UpdateNsMetadata"
    ]
    """<p>Metadata related to the network operation occurrence for network instance updates. This is populated only if the lcmOperationType is <code>UPDATE</code> and the updateType is <code>UPDATE_NS</code>.</p>"""
    modify_vnf_info_metadata: NotRequired[
        "capo_tnb.types.modify_vnf_info_metadata.ModifyVnfInfoMetadata"
    ]
    """<p>Metadata related to the network operation occurrence for network function updates in a network instance. This is populated only if the lcmOperationType is <code>UPDATE</code> and the updateType is <code>MODIFY_VNF_INFORMATION</code>.</p>"""
    instantiate_metadata: NotRequired[
        "capo_tnb.types.instantiate_metadata.InstantiateMetadata"
    ]
    """<p>Metadata related to the network operation occurrence for network instantiation. This is populated only if the lcmOperationType is <code>INSTANTIATE</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkOperationMetadata) -> dict:
    out: dict = {}
    if "update_ns_metadata" in value:
        import capo_tnb.types.update_ns_metadata

        out["updateNsMetadata"] = capo_tnb.types.update_ns_metadata.serialize_json(
            value["update_ns_metadata"]
        )
    if "modify_vnf_info_metadata" in value:
        import capo_tnb.types.modify_vnf_info_metadata

        out["modifyVnfInfoMetadata"] = (
            capo_tnb.types.modify_vnf_info_metadata.serialize_json(
                value["modify_vnf_info_metadata"]
            )
        )
    if "instantiate_metadata" in value:
        import capo_tnb.types.instantiate_metadata

        out["instantiateMetadata"] = capo_tnb.types.instantiate_metadata.serialize_json(
            value["instantiate_metadata"]
        )
    import capo_tnb.types._prelude.timestamp

    out["createdAt"] = capo_tnb.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_tnb.types._prelude.timestamp

    out["lastModified"] = capo_tnb.types._prelude.timestamp.serialize_json(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> GetSolNetworkOperationMetadata:
    out: GetSolNetworkOperationMetadata = {}  # type: ignore[typeddict-item]
    if "updateNsMetadata" in data:
        import capo_tnb.types.update_ns_metadata

        out["update_ns_metadata"] = capo_tnb.types.update_ns_metadata.deserialize_json(
            data["updateNsMetadata"]
        )
    if "modifyVnfInfoMetadata" in data:
        import capo_tnb.types.modify_vnf_info_metadata

        out["modify_vnf_info_metadata"] = (
            capo_tnb.types.modify_vnf_info_metadata.deserialize_json(
                data["modifyVnfInfoMetadata"]
            )
        )
    if "instantiateMetadata" in data:
        import capo_tnb.types.instantiate_metadata

        out["instantiate_metadata"] = (
            capo_tnb.types.instantiate_metadata.deserialize_json(
                data["instantiateMetadata"]
            )
        )
    if "createdAt" in data:
        import capo_tnb.types._prelude.timestamp

        out["created_at"] = capo_tnb.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetSolNetworkOperationMetadata.created_at required")
    if "lastModified" in data:
        import capo_tnb.types._prelude.timestamp

        out["last_modified"] = capo_tnb.types._prelude.timestamp.deserialize_json(
            data["lastModified"]
        )
    else:
        raise DeserializationError(
            "GetSolNetworkOperationMetadata.last_modified required"
        )
    return out
