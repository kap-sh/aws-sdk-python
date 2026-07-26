"""Generated from Smithy shape ``com.amazonaws.tnb#PutSolNetworkPackageContentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.nsd_id
    import capo_tnb.types.nsd_info_arn
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.put_sol_network_package_content_metadata
    import capo_tnb.types.vnf_pkg_id_list


class PutSolNetworkPackageContentOutput(TypedDict, closed=True):
    id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network package ID.</p>"""
    arn: "capo_tnb.types.nsd_info_arn.NsdInfoArn"
    """<p>Network package ARN.</p>"""
    nsd_id: "capo_tnb.types.nsd_id.NsdId"
    """<p>Network service descriptor ID.</p>"""
    nsd_name: "str"
    """<p>Network service descriptor name.</p>"""
    nsd_version: "str"
    """<p>Network service descriptor version.</p>"""
    vnf_pkg_ids: "capo_tnb.types.vnf_pkg_id_list.VnfPkgIdList"
    """<p>Function package IDs.</p>"""
    metadata: "capo_tnb.types.put_sol_network_package_content_metadata.PutSolNetworkPackageContentMetadata"
    """<p>Network package metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSolNetworkPackageContentOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsdId"] = value["nsd_id"]
    out["nsdName"] = value["nsd_name"]
    out["nsdVersion"] = value["nsd_version"]
    import capo_tnb.types.vnf_pkg_id_list

    out["vnfPkgIds"] = capo_tnb.types.vnf_pkg_id_list.serialize_json(
        value["vnf_pkg_ids"]
    )
    import capo_tnb.types.put_sol_network_package_content_metadata

    out["metadata"] = (
        capo_tnb.types.put_sol_network_package_content_metadata.serialize_json(
            value["metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutSolNetworkPackageContentOutput:
    out: PutSolNetworkPackageContentOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PutSolNetworkPackageContentOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("PutSolNetworkPackageContentOutput.arn required")
    if "nsdId" in data:
        out["nsd_id"] = data["nsdId"]
    else:
        raise DeserializationError("PutSolNetworkPackageContentOutput.nsd_id required")
    if "nsdName" in data:
        out["nsd_name"] = data["nsdName"]
    else:
        raise DeserializationError(
            "PutSolNetworkPackageContentOutput.nsd_name required"
        )
    if "nsdVersion" in data:
        out["nsd_version"] = data["nsdVersion"]
    else:
        raise DeserializationError(
            "PutSolNetworkPackageContentOutput.nsd_version required"
        )
    if "vnfPkgIds" in data:
        import capo_tnb.types.vnf_pkg_id_list

        out["vnf_pkg_ids"] = capo_tnb.types.vnf_pkg_id_list.deserialize_json(
            data["vnfPkgIds"]
        )
    else:
        raise DeserializationError(
            "PutSolNetworkPackageContentOutput.vnf_pkg_ids required"
        )
    if "metadata" in data:
        import capo_tnb.types.put_sol_network_package_content_metadata

        out["metadata"] = (
            capo_tnb.types.put_sol_network_package_content_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError(
            "PutSolNetworkPackageContentOutput.metadata required"
        )
    return out
