"""Generated from Smithy shape ``com.amazonaws.tnb#ValidateSolNetworkPackageContentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.nsd_id
    import aws_sdk_tnb.types.nsd_info_arn
    import aws_sdk_tnb.types.nsd_info_id
    import aws_sdk_tnb.types.validate_sol_network_package_content_metadata
    import aws_sdk_tnb.types.vnf_pkg_id_list


class ValidateSolNetworkPackageContentOutput(TypedDict):
    id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network package ID.</p>"""
    arn: "aws_sdk_tnb.types.nsd_info_arn.NsdInfoArn"
    """<p>Network package ARN.</p>"""
    nsd_id: "aws_sdk_tnb.types.nsd_id.NsdId"
    """<p>Network service descriptor ID.</p>"""
    nsd_name: "str"
    """<p>Network service descriptor name.</p>"""
    nsd_version: "str"
    """<p>Network service descriptor version.</p>"""
    vnf_pkg_ids: "aws_sdk_tnb.types.vnf_pkg_id_list.VnfPkgIdList"
    """<p>Function package IDs.</p>"""
    metadata: "aws_sdk_tnb.types.validate_sol_network_package_content_metadata.ValidateSolNetworkPackageContentMetadata"
    """<p>Network package metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSolNetworkPackageContentOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsdId"] = value["nsd_id"]
    out["nsdName"] = value["nsd_name"]
    out["nsdVersion"] = value["nsd_version"]
    import aws_sdk_tnb.types.vnf_pkg_id_list

    out["vnfPkgIds"] = aws_sdk_tnb.types.vnf_pkg_id_list.serialize_json(
        value["vnf_pkg_ids"]
    )
    import aws_sdk_tnb.types.validate_sol_network_package_content_metadata

    out["metadata"] = (
        aws_sdk_tnb.types.validate_sol_network_package_content_metadata.serialize_json(
            value["metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> ValidateSolNetworkPackageContentOutput:
    out: ValidateSolNetworkPackageContentOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ValidateSolNetworkPackageContentOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "ValidateSolNetworkPackageContentOutput.arn required"
        )
    if "nsdId" in data:
        out["nsd_id"] = data["nsdId"]
    else:
        raise DeserializationError(
            "ValidateSolNetworkPackageContentOutput.nsd_id required"
        )
    if "nsdName" in data:
        out["nsd_name"] = data["nsdName"]
    else:
        raise DeserializationError(
            "ValidateSolNetworkPackageContentOutput.nsd_name required"
        )
    if "nsdVersion" in data:
        out["nsd_version"] = data["nsdVersion"]
    else:
        raise DeserializationError(
            "ValidateSolNetworkPackageContentOutput.nsd_version required"
        )
    if "vnfPkgIds" in data:
        import aws_sdk_tnb.types.vnf_pkg_id_list

        out["vnf_pkg_ids"] = aws_sdk_tnb.types.vnf_pkg_id_list.deserialize_json(
            data["vnfPkgIds"]
        )
    else:
        raise DeserializationError(
            "ValidateSolNetworkPackageContentOutput.vnf_pkg_ids required"
        )
    if "metadata" in data:
        import aws_sdk_tnb.types.validate_sol_network_package_content_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.validate_sol_network_package_content_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError(
            "ValidateSolNetworkPackageContentOutput.metadata required"
        )
    return out
