"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkOperationMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_tnb.types.instantiate_metadata
    import aws_sdk_tnb.types.modify_vnf_info_metadata
    import aws_sdk_tnb.types.update_ns_metadata


class GetSolNetworkOperationMetadata(TypedDict):
    update_ns_metadata: NotRequired[
        "aws_sdk_tnb.types.update_ns_metadata.UpdateNsMetadata"
    ]
    """<p>Metadata related to the network operation occurrence for network instance updates. This is populated only if the lcmOperationType is <code>UPDATE</code> and the updateType is <code>UPDATE_NS</code>.</p>"""
    modify_vnf_info_metadata: NotRequired[
        "aws_sdk_tnb.types.modify_vnf_info_metadata.ModifyVnfInfoMetadata"
    ]
    """<p>Metadata related to the network operation occurrence for network function updates in a network instance. This is populated only if the lcmOperationType is <code>UPDATE</code> and the updateType is <code>MODIFY_VNF_INFORMATION</code>.</p>"""
    instantiate_metadata: NotRequired[
        "aws_sdk_tnb.types.instantiate_metadata.InstantiateMetadata"
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
        import aws_sdk_tnb.types.update_ns_metadata

        out["updateNsMetadata"] = aws_sdk_tnb.types.update_ns_metadata.serialize_json(
            value["update_ns_metadata"]
        )
    if "modify_vnf_info_metadata" in value:
        import aws_sdk_tnb.types.modify_vnf_info_metadata

        out["modifyVnfInfoMetadata"] = (
            aws_sdk_tnb.types.modify_vnf_info_metadata.serialize_json(
                value["modify_vnf_info_metadata"]
            )
        )
    if "instantiate_metadata" in value:
        import aws_sdk_tnb.types.instantiate_metadata

        out["instantiateMetadata"] = (
            aws_sdk_tnb.types.instantiate_metadata.serialize_json(
                value["instantiate_metadata"]
            )
        )
    import aws_sdk_tnb.types._prelude.timestamp

    out["createdAt"] = aws_sdk_tnb.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_tnb.types._prelude.timestamp

    out["lastModified"] = aws_sdk_tnb.types._prelude.timestamp.serialize_json(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> GetSolNetworkOperationMetadata:
    out: GetSolNetworkOperationMetadata = {}  # type: ignore[typeddict-item]
    if "updateNsMetadata" in data:
        import aws_sdk_tnb.types.update_ns_metadata

        out["update_ns_metadata"] = (
            aws_sdk_tnb.types.update_ns_metadata.deserialize_json(
                data["updateNsMetadata"]
            )
        )
    if "modifyVnfInfoMetadata" in data:
        import aws_sdk_tnb.types.modify_vnf_info_metadata

        out["modify_vnf_info_metadata"] = (
            aws_sdk_tnb.types.modify_vnf_info_metadata.deserialize_json(
                data["modifyVnfInfoMetadata"]
            )
        )
    if "instantiateMetadata" in data:
        import aws_sdk_tnb.types.instantiate_metadata

        out["instantiate_metadata"] = (
            aws_sdk_tnb.types.instantiate_metadata.deserialize_json(
                data["instantiateMetadata"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["created_at"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetSolNetworkOperationMetadata.created_at required")
    if "lastModified" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["last_modified"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["lastModified"]
        )
    else:
        raise DeserializationError(
            "GetSolNetworkOperationMetadata.last_modified required"
        )
    return out
