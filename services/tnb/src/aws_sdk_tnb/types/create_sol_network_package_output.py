"""Generated from Smithy shape ``com.amazonaws.tnb#CreateSolNetworkPackageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.nsd_info_arn
    import aws_sdk_tnb.types.nsd_info_id
    import aws_sdk_tnb.types.nsd_onboarding_state
    import aws_sdk_tnb.types.nsd_operational_state
    import aws_sdk_tnb.types.nsd_usage_state
    import aws_sdk_tnb.types.tag_map


class CreateSolNetworkPackageOutput(TypedDict, closed=True):
    id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network package.</p>"""
    arn: "aws_sdk_tnb.types.nsd_info_arn.NsdInfoArn"
    """<p>Network package ARN.</p>"""
    nsd_onboarding_state: "aws_sdk_tnb.types.nsd_onboarding_state.NsdOnboardingState"
    """<p>Onboarding state of the network service descriptor in the network package.</p>"""
    nsd_operational_state: "aws_sdk_tnb.types.nsd_operational_state.NsdOperationalState"
    """<p>Operational state of the network service descriptor in the network package.</p>"""
    nsd_usage_state: "aws_sdk_tnb.types.nsd_usage_state.NsdUsageState"
    """<p>Usage state of the network service descriptor in the network package.</p>"""
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSolNetworkPackageOutput) -> dict:
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
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSolNetworkPackageOutput:
    out: CreateSolNetworkPackageOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateSolNetworkPackageOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateSolNetworkPackageOutput.arn required")
    if "nsdOnboardingState" in data:
        import aws_sdk_tnb.types.nsd_onboarding_state

        out["nsd_onboarding_state"] = (
            aws_sdk_tnb.types.nsd_onboarding_state.deserialize_json(
                data["nsdOnboardingState"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSolNetworkPackageOutput.nsd_onboarding_state required"
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
            "CreateSolNetworkPackageOutput.nsd_operational_state required"
        )
    if "nsdUsageState" in data:
        import aws_sdk_tnb.types.nsd_usage_state

        out["nsd_usage_state"] = aws_sdk_tnb.types.nsd_usage_state.deserialize_json(
            data["nsdUsageState"]
        )
    else:
        raise DeserializationError(
            "CreateSolNetworkPackageOutput.nsd_usage_state required"
        )
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out
