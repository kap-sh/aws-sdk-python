"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformBranchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.branch_name
    import capo_elastic_beanstalk.types.branch_order
    import capo_elastic_beanstalk.types.platform_branch_lifecycle_state
    import capo_elastic_beanstalk.types.platform_name
    import capo_elastic_beanstalk.types.supported_tier_list


class PlatformBranchSummary(TypedDict, closed=True):
    platform_name: NotRequired[
        "capo_elastic_beanstalk.types.platform_name.PlatformName"
    ]
    """<p>The name of the platform to which this platform branch belongs.</p>"""
    branch_name: NotRequired["capo_elastic_beanstalk.types.branch_name.BranchName"]
    """<p>The name of the platform branch.</p>"""
    lifecycle_state: NotRequired[
        "capo_elastic_beanstalk.types.platform_branch_lifecycle_state.PlatformBranchLifecycleState"
    ]
    """<p>The support life cycle state of the platform branch.</p> <p>Possible values: <code>beta</code> | <code>supported</code> | <code>deprecated</code> | <code>retired</code> </p>"""
    branch_order: "capo_elastic_beanstalk.types.branch_order.BranchOrder"
    """<p>An ordinal number that designates the order in which platform branches have been added to a platform. This can be helpful, for example, if your code calls the <code>ListPlatformBranches</code> action and then displays a list of platform branches.</p> <p>A larger <code>BranchOrder</code> value designates a newer platform branch within the platform.</p>"""
    supported_tier_list: NotRequired[
        "capo_elastic_beanstalk.types.supported_tier_list.SupportedTierList"
    ]
    """<p>The environment tiers that platform versions in this branch support.</p> <p>Possible values: <code>WebServer/Standard</code> | <code>Worker/SQS/HTTP</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformBranchSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_name" in value:
        pairs.append((f"{prefix}.PlatformName", str(value["platform_name"])))
    if "branch_name" in value:
        pairs.append((f"{prefix}.BranchName", str(value["branch_name"])))
    if "lifecycle_state" in value:
        pairs.append((f"{prefix}.LifecycleState", str(value["lifecycle_state"])))
    pairs.append((f"{prefix}.BranchOrder", str(value.get("branch_order", 0))))
    if "supported_tier_list" in value:
        import capo_elastic_beanstalk.types.supported_tier_list

        capo_elastic_beanstalk.types.supported_tier_list.serialize_query(
            value["supported_tier_list"], pairs, f"{prefix}.SupportedTierList"
        )


def deserialize_query(el: Element) -> PlatformBranchSummary:
    out: PlatformBranchSummary = {}  # type: ignore[typeddict-item]
    child_platform_name = el.find("PlatformName")
    if child_platform_name is not None:
        out["platform_name"] = str(child_platform_name.text or "")
    child_branch_name = el.find("BranchName")
    if child_branch_name is not None:
        out["branch_name"] = str(child_branch_name.text or "")
    child_lifecycle_state = el.find("LifecycleState")
    if child_lifecycle_state is not None:
        out["lifecycle_state"] = str(child_lifecycle_state.text or "")
    child_branch_order = el.find("BranchOrder")
    if child_branch_order is not None:
        out["branch_order"] = int(child_branch_order.text or "")
    else:
        out["branch_order"] = 0
    child_supported_tier_list = el.find("SupportedTierList")
    if child_supported_tier_list is not None:
        import capo_elastic_beanstalk.types.supported_tier_list

        out["supported_tier_list"] = (
            capo_elastic_beanstalk.types.supported_tier_list.deserialize_query(
                child_supported_tier_list
            )
        )
    return out
