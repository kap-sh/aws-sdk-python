"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.get_sol_function_instance_metadata
    import aws_sdk_tnb.types.get_sol_vnf_info
    import aws_sdk_tnb.types.ns_instance_id
    import aws_sdk_tnb.types.tag_map
    import aws_sdk_tnb.types.vnf_instance_arn
    import aws_sdk_tnb.types.vnf_instance_id
    import aws_sdk_tnb.types.vnf_instantiation_state
    import aws_sdk_tnb.types.vnf_pkg_id
    import aws_sdk_tnb.types.vnfd_id


class GetSolFunctionInstanceOutput(TypedDict, closed=True):
    id: "aws_sdk_tnb.types.vnf_instance_id.VnfInstanceId"
    """<p>Network function instance ID.</p>"""
    arn: "aws_sdk_tnb.types.vnf_instance_arn.VnfInstanceArn"
    """<p>Network function instance ARN.</p>"""
    ns_instance_id: "aws_sdk_tnb.types.ns_instance_id.NsInstanceId"
    """<p>Network instance ID.</p>"""
    vnf_pkg_id: "aws_sdk_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>Function package ID.</p>"""
    vnfd_id: "aws_sdk_tnb.types.vnfd_id.VnfdId"
    """<p>Function package descriptor ID.</p>"""
    vnf_provider: NotRequired["str"]
    """<p>Network function provider.</p>"""
    vnf_product_name: NotRequired["str"]
    """<p>Network function product name.</p>"""
    vnfd_version: NotRequired["str"]
    """<p>Function package descriptor version.</p>"""
    instantiation_state: (
        "aws_sdk_tnb.types.vnf_instantiation_state.VnfInstantiationState"
    )
    """<p>Network function instantiation state.</p>"""
    instantiated_vnf_info: NotRequired[
        "aws_sdk_tnb.types.get_sol_vnf_info.GetSolVnfInfo"
    ]
    metadata: "aws_sdk_tnb.types.get_sol_function_instance_metadata.GetSolFunctionInstanceMetadata"
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionInstanceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsInstanceId"] = value["ns_instance_id"]
    out["vnfPkgId"] = value["vnf_pkg_id"]
    out["vnfdId"] = value["vnfd_id"]
    if "vnf_provider" in value:
        out["vnfProvider"] = value["vnf_provider"]
    if "vnf_product_name" in value:
        out["vnfProductName"] = value["vnf_product_name"]
    if "vnfd_version" in value:
        out["vnfdVersion"] = value["vnfd_version"]
    import aws_sdk_tnb.types.vnf_instantiation_state

    out["instantiationState"] = (
        aws_sdk_tnb.types.vnf_instantiation_state.serialize_json(
            value["instantiation_state"]
        )
    )
    if "instantiated_vnf_info" in value:
        import aws_sdk_tnb.types.get_sol_vnf_info

        out["instantiatedVnfInfo"] = aws_sdk_tnb.types.get_sol_vnf_info.serialize_json(
            value["instantiated_vnf_info"]
        )
    import aws_sdk_tnb.types.get_sol_function_instance_metadata

    out["metadata"] = (
        aws_sdk_tnb.types.get_sol_function_instance_metadata.serialize_json(
            value["metadata"]
        )
    )
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolFunctionInstanceOutput:
    out: GetSolFunctionInstanceOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSolFunctionInstanceOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSolFunctionInstanceOutput.arn required")
    if "nsInstanceId" in data:
        out["ns_instance_id"] = data["nsInstanceId"]
    else:
        raise DeserializationError(
            "GetSolFunctionInstanceOutput.ns_instance_id required"
        )
    if "vnfPkgId" in data:
        out["vnf_pkg_id"] = data["vnfPkgId"]
    else:
        raise DeserializationError("GetSolFunctionInstanceOutput.vnf_pkg_id required")
    if "vnfdId" in data:
        out["vnfd_id"] = data["vnfdId"]
    else:
        raise DeserializationError("GetSolFunctionInstanceOutput.vnfd_id required")
    if "vnfProvider" in data:
        out["vnf_provider"] = data["vnfProvider"]
    if "vnfProductName" in data:
        out["vnf_product_name"] = data["vnfProductName"]
    if "vnfdVersion" in data:
        out["vnfd_version"] = data["vnfdVersion"]
    if "instantiationState" in data:
        import aws_sdk_tnb.types.vnf_instantiation_state

        out["instantiation_state"] = (
            aws_sdk_tnb.types.vnf_instantiation_state.deserialize_json(
                data["instantiationState"]
            )
        )
    else:
        raise DeserializationError(
            "GetSolFunctionInstanceOutput.instantiation_state required"
        )
    if "instantiatedVnfInfo" in data:
        import aws_sdk_tnb.types.get_sol_vnf_info

        out["instantiated_vnf_info"] = (
            aws_sdk_tnb.types.get_sol_vnf_info.deserialize_json(
                data["instantiatedVnfInfo"]
            )
        )
    if "metadata" in data:
        import aws_sdk_tnb.types.get_sol_function_instance_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.get_sol_function_instance_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("GetSolFunctionInstanceOutput.metadata required")
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out
