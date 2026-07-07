"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_action
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_filter


class LifecyclePolicyDetail(TypedDict, closed=True):
    action: "aws_sdk_imagebuilder.types.lifecycle_policy_detail_action.LifecyclePolicyDetailAction"
    """<p>Configuration details for the policy action.</p>"""
    filter: "aws_sdk_imagebuilder.types.lifecycle_policy_detail_filter.LifecyclePolicyDetailFilter"
    """<p>Specifies the resources that the lifecycle policy applies to.</p>"""
    exclusion_rules: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules.LifecyclePolicyDetailExclusionRules"
    ]
    """<p>Additional rules to specify resources that should be exempt from policy actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetail) -> dict:
    out: dict = {}
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_action

    out["action"] = (
        aws_sdk_imagebuilder.types.lifecycle_policy_detail_action.serialize_json(
            value["action"]
        )
    )
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_filter

    out["filter"] = (
        aws_sdk_imagebuilder.types.lifecycle_policy_detail_filter.serialize_json(
            value["filter"]
        )
    )
    if "exclusion_rules" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules

        out["exclusionRules"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules.serialize_json(
                value["exclusion_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> LifecyclePolicyDetail:
    out: LifecyclePolicyDetail = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_detail_action

        out["action"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_detail_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("LifecyclePolicyDetail.action required")
    if "filter" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_detail_filter

        out["filter"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_detail_filter.deserialize_json(
                data["filter"]
            )
        )
    else:
        raise DeserializationError("LifecyclePolicyDetail.filter required")
    if "exclusionRules" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules

        out["exclusion_rules"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules.deserialize_json(
                data["exclusionRules"]
            )
        )
    return out
