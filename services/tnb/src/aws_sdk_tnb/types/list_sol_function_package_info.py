"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionPackageInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_function_package_metadata
    import aws_sdk_tnb.types.onboarding_state
    import aws_sdk_tnb.types.operational_state
    import aws_sdk_tnb.types.usage_state
    import aws_sdk_tnb.types.vnf_pkg_arn
    import aws_sdk_tnb.types.vnf_pkg_id


class ListSolFunctionPackageInfo(TypedDict, closed=True):
    id: "aws_sdk_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>ID of the function package.</p>"""
    arn: "aws_sdk_tnb.types.vnf_pkg_arn.VnfPkgArn"
    """<p>Function package ARN.</p>"""
    onboarding_state: "aws_sdk_tnb.types.onboarding_state.OnboardingState"
    """<p>Onboarding state of the function package.</p>"""
    operational_state: "aws_sdk_tnb.types.operational_state.OperationalState"
    """<p>Operational state of the function package.</p>"""
    usage_state: "aws_sdk_tnb.types.usage_state.UsageState"
    """<p>Usage state of the function package.</p>"""
    vnfd_id: NotRequired["str"]
    """<p>Identifies the function package and the function package descriptor.</p>"""
    vnf_provider: NotRequired["str"]
    """<p>Provider of the function package and the function package descriptor.</p>"""
    vnf_product_name: NotRequired["str"]
    """<p>The product name for the network function.</p>"""
    vnfd_version: NotRequired["str"]
    """<p>Identifies the version of the function package descriptor.</p>"""
    metadata: NotRequired[
        "aws_sdk_tnb.types.list_sol_function_package_metadata.ListSolFunctionPackageMetadata"
    ]
    """<p>The metadata of the function package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionPackageInfo) -> dict:
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
        import aws_sdk_tnb.types.list_sol_function_package_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.list_sol_function_package_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSolFunctionPackageInfo:
    out: ListSolFunctionPackageInfo = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ListSolFunctionPackageInfo.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListSolFunctionPackageInfo.arn required")
    if "onboardingState" in data:
        import aws_sdk_tnb.types.onboarding_state

        out["onboarding_state"] = aws_sdk_tnb.types.onboarding_state.deserialize_json(
            data["onboardingState"]
        )
    else:
        raise DeserializationError(
            "ListSolFunctionPackageInfo.onboarding_state required"
        )
    if "operationalState" in data:
        import aws_sdk_tnb.types.operational_state

        out["operational_state"] = aws_sdk_tnb.types.operational_state.deserialize_json(
            data["operationalState"]
        )
    else:
        raise DeserializationError(
            "ListSolFunctionPackageInfo.operational_state required"
        )
    if "usageState" in data:
        import aws_sdk_tnb.types.usage_state

        out["usage_state"] = aws_sdk_tnb.types.usage_state.deserialize_json(
            data["usageState"]
        )
    else:
        raise DeserializationError("ListSolFunctionPackageInfo.usage_state required")
    if "vnfdId" in data:
        out["vnfd_id"] = data["vnfdId"]
    if "vnfProvider" in data:
        out["vnf_provider"] = data["vnfProvider"]
    if "vnfProductName" in data:
        out["vnf_product_name"] = data["vnfProductName"]
    if "vnfdVersion" in data:
        out["vnfd_version"] = data["vnfdVersion"]
    if "metadata" in data:
        import aws_sdk_tnb.types.list_sol_function_package_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.list_sol_function_package_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
