"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailExclusionRules``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis
    import capo_imagebuilder.types.tag_map


class LifecyclePolicyDetailExclusionRules(TypedDict, closed=True):
    tag_map: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Contains a list of tags that Image Builder uses to skip lifecycle actions for Image Builder image resources that have them.</p>"""
    amis: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis.LifecyclePolicyDetailExclusionRulesAmis"
    ]
    """<p>Lists configuration values that apply to AMIs that Image Builder should exclude from the lifecycle action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailExclusionRules) -> dict:
    out: dict = {}
    if "tag_map" in value:
        import capo_imagebuilder.types.tag_map

        out["tagMap"] = capo_imagebuilder.types.tag_map.serialize_json(value["tag_map"])
    if "amis" in value:
        import capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis

        out["amis"] = (
            capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis.serialize_json(
                value["amis"]
            )
        )
    return out


def deserialize_json(data: dict) -> LifecyclePolicyDetailExclusionRules:
    out: LifecyclePolicyDetailExclusionRules = {}  # type: ignore[typeddict-item]
    if "tagMap" in data:
        import capo_imagebuilder.types.tag_map

        out["tag_map"] = capo_imagebuilder.types.tag_map.deserialize_json(
            data["tagMap"]
        )
    if "amis" in data:
        import capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis

        out["amis"] = (
            capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis.deserialize_json(
                data["amis"]
            )
        )
    return out
