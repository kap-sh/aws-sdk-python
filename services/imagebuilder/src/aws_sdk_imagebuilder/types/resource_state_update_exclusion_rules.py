"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ResourceStateUpdateExclusionRules``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis


class ResourceStateUpdateExclusionRules(TypedDict, closed=True):
    amis: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis.LifecyclePolicyDetailExclusionRulesAmis"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStateUpdateExclusionRules) -> dict:
    out: dict = {}
    if "amis" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis

        out["amis"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis.serialize_json(
                value["amis"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceStateUpdateExclusionRules:
    out: ResourceStateUpdateExclusionRules = {}  # type: ignore[typeddict-item]
    if "amis" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis

        out["amis"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis.deserialize_json(
                data["amis"]
            )
        )
    return out
