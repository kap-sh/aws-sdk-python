"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.get_sol_function_package_metadata
    import aws_sdk_tnb.types.onboarding_state
    import aws_sdk_tnb.types.operational_state
    import aws_sdk_tnb.types.tag_map
    import aws_sdk_tnb.types.usage_state
    import aws_sdk_tnb.types.vnf_pkg_arn
    import aws_sdk_tnb.types.vnf_pkg_id


class GetSolFunctionPackageOutput(TypedDict):
    id: "aws_sdk_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>Function package ID.</p>"""
    arn: "aws_sdk_tnb.types.vnf_pkg_arn.VnfPkgArn"
    """<p>Function package ARN.</p>"""
    onboarding_state: "aws_sdk_tnb.types.onboarding_state.OnboardingState"
    """<p>Function package onboarding state.</p>"""
    operational_state: "aws_sdk_tnb.types.operational_state.OperationalState"
    """<p>Function package operational state.</p>"""
    usage_state: "aws_sdk_tnb.types.usage_state.UsageState"
    """<p>Function package usage state.</p>"""
    vnfd_id: NotRequired["str"]
    """<p>Function package descriptor ID.</p>"""
    vnf_provider: NotRequired["str"]
    """<p>Network function provider.</p>"""
    vnf_product_name: NotRequired["str"]
    """<p>Network function product name.</p>"""
    vnfd_version: NotRequired["str"]
    """<p>Function package descriptor version.</p>"""
    metadata: NotRequired[
        "aws_sdk_tnb.types.get_sol_function_package_metadata.GetSolFunctionPackageMetadata"
    ]
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_tnb.types.onboarding_state

    out["onboardingState"] = aws_sdk_tnb.types.onboarding_state.serialize_json(
        value["onboarding_state"]
    )
    import aws_sdk_tnb.types.operational_state

    out["operationalState"] = aws_sdk_tnb.types.operational_state.serialize_json(
        value["operational_state"]
    )
    import aws_sdk_tnb.types.usage_state

    out["usageState"] = aws_sdk_tnb.types.usage_state.serialize_json(
        value["usage_state"]
    )
    if "vnfd_id" in value:
        out["vnfdId"] = value["vnfd_id"]
    if "vnf_provider" in value:
        out["vnfProvider"] = value["vnf_provider"]
    if "vnf_product_name" in value:
        out["vnfProductName"] = value["vnf_product_name"]
    if "vnfd_version" in value:
        out["vnfdVersion"] = value["vnfd_version"]
    if "metadata" in value:
        import aws_sdk_tnb.types.get_sol_function_package_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.get_sol_function_package_metadata.serialize_json(
                value["metadata"]
            )
        )
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageOutput:
    out: GetSolFunctionPackageOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSolFunctionPackageOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSolFunctionPackageOutput.arn required")
    if "onboardingState" in data:
        import aws_sdk_tnb.types.onboarding_state

        out["onboarding_state"] = aws_sdk_tnb.types.onboarding_state.deserialize_json(
            data["onboardingState"]
        )
    else:
        raise DeserializationError(
            "GetSolFunctionPackageOutput.onboarding_state required"
        )
    if "operationalState" in data:
        import aws_sdk_tnb.types.operational_state

        out["operational_state"] = aws_sdk_tnb.types.operational_state.deserialize_json(
            data["operationalState"]
        )
    else:
        raise DeserializationError(
            "GetSolFunctionPackageOutput.operational_state required"
        )
    if "usageState" in data:
        import aws_sdk_tnb.types.usage_state

        out["usage_state"] = aws_sdk_tnb.types.usage_state.deserialize_json(
            data["usageState"]
        )
    else:
        raise DeserializationError("GetSolFunctionPackageOutput.usage_state required")
    if "vnfdId" in data:
        out["vnfd_id"] = data["vnfdId"]
    if "vnfProvider" in data:
        out["vnf_provider"] = data["vnfProvider"]
    if "vnfProductName" in data:
        out["vnf_product_name"] = data["vnfProductName"]
    if "vnfdVersion" in data:
        out["vnfd_version"] = data["vnfdVersion"]
    if "metadata" in data:
        import aws_sdk_tnb.types.get_sol_function_package_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.get_sol_function_package_metadata.deserialize_json(
                data["metadata"]
            )
        )
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out
