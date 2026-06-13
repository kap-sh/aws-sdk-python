"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.get_sol_network_package_metadata
    import aws_sdk_tnb.types.nsd_id
    import aws_sdk_tnb.types.nsd_info_arn
    import aws_sdk_tnb.types.nsd_info_id
    import aws_sdk_tnb.types.nsd_onboarding_state
    import aws_sdk_tnb.types.nsd_operational_state
    import aws_sdk_tnb.types.nsd_usage_state
    import aws_sdk_tnb.types.tag_map
    import aws_sdk_tnb.types.vnf_pkg_id_list


class GetSolNetworkPackageOutput(TypedDict):
    id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network package ID.</p>"""
    arn: "aws_sdk_tnb.types.nsd_info_arn.NsdInfoArn"
    """<p>Network package ARN.</p>"""
    nsd_onboarding_state: "aws_sdk_tnb.types.nsd_onboarding_state.NsdOnboardingState"
    """<p>Network service descriptor onboarding state.</p>"""
    nsd_operational_state: "aws_sdk_tnb.types.nsd_operational_state.NsdOperationalState"
    """<p>Network service descriptor operational state.</p>"""
    nsd_usage_state: "aws_sdk_tnb.types.nsd_usage_state.NsdUsageState"
    """<p>Network service descriptor usage state.</p>"""
    nsd_id: "aws_sdk_tnb.types.nsd_id.NsdId"
    """<p>Network service descriptor ID.</p>"""
    nsd_name: "str"
    """<p>Network service descriptor name.</p>"""
    nsd_version: "str"
    """<p>Network service descriptor version.</p>"""
    vnf_pkg_ids: "aws_sdk_tnb.types.vnf_pkg_id_list.VnfPkgIdList"
    """<p>Identifies the function package for the function package descriptor referenced by the onboarded network package.</p>"""
    metadata: "aws_sdk_tnb.types.get_sol_network_package_metadata.GetSolNetworkPackageMetadata"
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_tnb.types.nsd_onboarding_state

    out["nsdOnboardingState"] = aws_sdk_tnb.types.nsd_onboarding_state.serialize_json(
        value["nsd_onboarding_state"]
    )
    import aws_sdk_tnb.types.nsd_operational_state

    out["nsdOperationalState"] = aws_sdk_tnb.types.nsd_operational_state.serialize_json(
        value["nsd_operational_state"]
    )
    import aws_sdk_tnb.types.nsd_usage_state

    out["nsdUsageState"] = aws_sdk_tnb.types.nsd_usage_state.serialize_json(
        value["nsd_usage_state"]
    )
    out["nsdId"] = value["nsd_id"]
    out["nsdName"] = value["nsd_name"]
    out["nsdVersion"] = value["nsd_version"]
    import aws_sdk_tnb.types.vnf_pkg_id_list

    out["vnfPkgIds"] = aws_sdk_tnb.types.vnf_pkg_id_list.serialize_json(
        value["vnf_pkg_ids"]
    )
    import aws_sdk_tnb.types.get_sol_network_package_metadata

    out["metadata"] = aws_sdk_tnb.types.get_sol_network_package_metadata.serialize_json(
        value["metadata"]
    )
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageOutput:
    out: GetSolNetworkPackageOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.arn required")
    if "nsdOnboardingState" in data:
        import aws_sdk_tnb.types.nsd_onboarding_state

        out["nsd_onboarding_state"] = (
            aws_sdk_tnb.types.nsd_onboarding_state.deserialize_json(
                data["nsdOnboardingState"]
            )
        )
    else:
        raise DeserializationError(
            "GetSolNetworkPackageOutput.nsd_onboarding_state required"
        )
    if "nsdOperationalState" in data:
        import aws_sdk_tnb.types.nsd_operational_state

        out["nsd_operational_state"] = (
            aws_sdk_tnb.types.nsd_operational_state.deserialize_json(
                data["nsdOperationalState"]
            )
        )
    else:
        raise DeserializationError(
            "GetSolNetworkPackageOutput.nsd_operational_state required"
        )
    if "nsdUsageState" in data:
        import aws_sdk_tnb.types.nsd_usage_state

        out["nsd_usage_state"] = aws_sdk_tnb.types.nsd_usage_state.deserialize_json(
            data["nsdUsageState"]
        )
    else:
        raise DeserializationError(
            "GetSolNetworkPackageOutput.nsd_usage_state required"
        )
    if "nsdId" in data:
        out["nsd_id"] = data["nsdId"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.nsd_id required")
    if "nsdName" in data:
        out["nsd_name"] = data["nsdName"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.nsd_name required")
    if "nsdVersion" in data:
        out["nsd_version"] = data["nsdVersion"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.nsd_version required")
    if "vnfPkgIds" in data:
        import aws_sdk_tnb.types.vnf_pkg_id_list

        out["vnf_pkg_ids"] = aws_sdk_tnb.types.vnf_pkg_id_list.deserialize_json(
            data["vnfPkgIds"]
        )
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.vnf_pkg_ids required")
    if "metadata" in data:
        import aws_sdk_tnb.types.get_sol_network_package_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.get_sol_network_package_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.metadata required")
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out
