"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailExclusionRulesAmis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.account_list
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched
    import capo_imagebuilder.types.string_list
    import capo_imagebuilder.types.tag_map


class LifecyclePolicyDetailExclusionRulesAmis(TypedDict, closed=True):
    is_public: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Configures whether public AMIs are excluded from the lifecycle action.</p>"""
    regions: NotRequired["capo_imagebuilder.types.string_list.StringList"]
    """<p>Configures Amazon Web Services Regions that are excluded from the lifecycle action.</p>"""
    shared_accounts: NotRequired["capo_imagebuilder.types.account_list.AccountList"]
    """<p>Specifies Amazon Web Services accounts whose resources are excluded from the lifecycle action.</p>"""
    last_launched: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched.LifecyclePolicyDetailExclusionRulesAmisLastLaunched"
    ]
    """<p>Specifies configuration details for Image Builder to exclude the most recent resources from lifecycle actions.</p>"""
    tag_map: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Lists tags that should be excluded from lifecycle actions for the AMIs that have them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailExclusionRulesAmis) -> dict:
    out: dict = {}
    out["isPublic"] = value.get("is_public", False)
    if "regions" in value:
        import capo_imagebuilder.types.string_list

        out["regions"] = capo_imagebuilder.types.string_list.serialize_json(
            value["regions"]
        )
    if "shared_accounts" in value:
        import capo_imagebuilder.types.account_list

        out["sharedAccounts"] = capo_imagebuilder.types.account_list.serialize_json(
            value["shared_accounts"]
        )
    if "last_launched" in value:
        import capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched

        out["lastLaunched"] = (
            capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched.serialize_json(
                value["last_launched"]
            )
        )
    if "tag_map" in value:
        import capo_imagebuilder.types.tag_map

        out["tagMap"] = capo_imagebuilder.types.tag_map.serialize_json(value["tag_map"])
    return out


def deserialize_json(data: dict) -> LifecyclePolicyDetailExclusionRulesAmis:
    out: LifecyclePolicyDetailExclusionRulesAmis = {}  # type: ignore[typeddict-item]
    if "isPublic" in data:
        out["is_public"] = data["isPublic"]
    else:
        out["is_public"] = False
    if "regions" in data:
        import capo_imagebuilder.types.string_list

        out["regions"] = capo_imagebuilder.types.string_list.deserialize_json(
            data["regions"]
        )
    if "sharedAccounts" in data:
        import capo_imagebuilder.types.account_list

        out["shared_accounts"] = capo_imagebuilder.types.account_list.deserialize_json(
            data["sharedAccounts"]
        )
    if "lastLaunched" in data:
        import capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched

        out["last_launched"] = (
            capo_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched.deserialize_json(
                data["lastLaunched"]
            )
        )
    if "tagMap" in data:
        import capo_imagebuilder.types.tag_map

        out["tag_map"] = capo_imagebuilder.types.tag_map.deserialize_json(
            data["tagMap"]
        )
    return out
