"""Generated from Smithy shape ``com.amazonaws.tnb#CreateSolFunctionPackageOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_tnb.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_tnb.types.onboarding_state
    import aws_sdk_tnb.types.operational_state
    import aws_sdk_tnb.types.tag_map
    import aws_sdk_tnb.types.usage_state
    import aws_sdk_tnb.types.vnf_pkg_arn
    import aws_sdk_tnb.types.vnf_pkg_id

class CreateSolFunctionPackageOutput(TypedDict):
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
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateSolFunctionPackageOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_tnb.types.onboarding_state
    out["onboardingState"] = aws_sdk_tnb.types.onboarding_state.serialize_json(value["onboarding_state"])
    import aws_sdk_tnb.types.operational_state
    out["operationalState"] = aws_sdk_tnb.types.operational_state.serialize_json(value["operational_state"])
    import aws_sdk_tnb.types.usage_state
    out["usageState"] = aws_sdk_tnb.types.usage_state.serialize_json(value["usage_state"])
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map
        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSolFunctionPackageOutput:
    out: CreateSolFunctionPackageOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateSolFunctionPackageOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateSolFunctionPackageOutput.arn required")
    if "onboardingState" in data:
        import aws_sdk_tnb.types.onboarding_state
        out["onboarding_state"] = aws_sdk_tnb.types.onboarding_state.deserialize_json(data["onboardingState"])
    else:
        raise DeserializationError("CreateSolFunctionPackageOutput.onboarding_state required")
    if "operationalState" in data:
        import aws_sdk_tnb.types.operational_state
        out["operational_state"] = aws_sdk_tnb.types.operational_state.deserialize_json(data["operationalState"])
    else:
        raise DeserializationError("CreateSolFunctionPackageOutput.operational_state required")
    if "usageState" in data:
        import aws_sdk_tnb.types.usage_state
        out["usage_state"] = aws_sdk_tnb.types.usage_state.deserialize_json(data["usageState"])
    else:
        raise DeserializationError("CreateSolFunctionPackageOutput.usage_state required")
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map
        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out