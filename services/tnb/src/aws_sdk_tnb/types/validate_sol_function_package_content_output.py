"""Generated from Smithy shape ``com.amazonaws.tnb#ValidateSolFunctionPackageContentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.validate_sol_function_package_content_metadata
    import aws_sdk_tnb.types.vnf_pkg_id
    import aws_sdk_tnb.types.vnfd_id


class ValidateSolFunctionPackageContentOutput(TypedDict):
    id: "aws_sdk_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>Function package ID.</p>"""
    vnfd_id: "aws_sdk_tnb.types.vnfd_id.VnfdId"
    """<p>Function package descriptor ID.</p>"""
    vnf_product_name: "str"
    """<p>Network function product name.</p>"""
    vnf_provider: "str"
    """<p>Network function provider.</p>"""
    vnfd_version: "str"
    """<p>Function package descriptor version.</p>"""
    metadata: "aws_sdk_tnb.types.validate_sol_function_package_content_metadata.ValidateSolFunctionPackageContentMetadata"
    """<p>Function package metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSolFunctionPackageContentOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["vnfdId"] = value["vnfd_id"]
    out["vnfProductName"] = value["vnf_product_name"]
    out["vnfProvider"] = value["vnf_provider"]
    out["vnfdVersion"] = value["vnfd_version"]
    import aws_sdk_tnb.types.validate_sol_function_package_content_metadata

    out["metadata"] = (
        aws_sdk_tnb.types.validate_sol_function_package_content_metadata.serialize_json(
            value["metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> ValidateSolFunctionPackageContentOutput:
    out: ValidateSolFunctionPackageContentOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "ValidateSolFunctionPackageContentOutput.id required"
        )
    if "vnfdId" in data:
        out["vnfd_id"] = data["vnfdId"]
    else:
        raise DeserializationError(
            "ValidateSolFunctionPackageContentOutput.vnfd_id required"
        )
    if "vnfProductName" in data:
        out["vnf_product_name"] = data["vnfProductName"]
    else:
        raise DeserializationError(
            "ValidateSolFunctionPackageContentOutput.vnf_product_name required"
        )
    if "vnfProvider" in data:
        out["vnf_provider"] = data["vnfProvider"]
    else:
        raise DeserializationError(
            "ValidateSolFunctionPackageContentOutput.vnf_provider required"
        )
    if "vnfdVersion" in data:
        out["vnfd_version"] = data["vnfdVersion"]
    else:
        raise DeserializationError(
            "ValidateSolFunctionPackageContentOutput.vnfd_version required"
        )
    if "metadata" in data:
        import aws_sdk_tnb.types.validate_sol_function_package_content_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.validate_sol_function_package_content_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError(
            "ValidateSolFunctionPackageContentOutput.metadata required"
        )
    return out
