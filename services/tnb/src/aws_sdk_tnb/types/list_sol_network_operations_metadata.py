"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkOperationsMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_tnb.types.nsd_info_id
    import aws_sdk_tnb.types.vnf_instance_id


class ListSolNetworkOperationsMetadata(TypedDict, closed=True):
    nsd_info_id: NotRequired["aws_sdk_tnb.types.nsd_info_id.NsdInfoId"]
    """<p>The network service descriptor id used for the operation.</p> <p>Only present if the updateType is <code>UPDATE_NS</code>.</p>"""
    vnf_instance_id: NotRequired["aws_sdk_tnb.types.vnf_instance_id.VnfInstanceId"]
    """<p>The network function id used for the operation.</p> <p>Only present if the updateType is <code>MODIFY_VNF_INFO</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkOperationsMetadata) -> dict:
    out: dict = {}
    if "nsd_info_id" in value:
        out["nsdInfoId"] = value["nsd_info_id"]
    if "vnf_instance_id" in value:
        out["vnfInstanceId"] = value["vnf_instance_id"]
    import aws_sdk_tnb.types._prelude.timestamp

    out["createdAt"] = aws_sdk_tnb.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_tnb.types._prelude.timestamp

    out["lastModified"] = aws_sdk_tnb.types._prelude.timestamp.serialize_json(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> ListSolNetworkOperationsMetadata:
    out: ListSolNetworkOperationsMetadata = {}  # type: ignore[typeddict-item]
    if "nsdInfoId" in data:
        out["nsd_info_id"] = data["nsdInfoId"]
    if "vnfInstanceId" in data:
        out["vnf_instance_id"] = data["vnfInstanceId"]
    if "createdAt" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["created_at"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "ListSolNetworkOperationsMetadata.created_at required"
        )
    if "lastModified" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["last_modified"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["lastModified"]
        )
    else:
        raise DeserializationError(
            "ListSolNetworkOperationsMetadata.last_modified required"
        )
    return out
