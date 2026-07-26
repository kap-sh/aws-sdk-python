"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceSharingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.absolute_borrow_limit_resource_list
    import capo_sagemaker.types.borrow_limit
    import capo_sagemaker.types.resource_sharing_strategy


class ResourceSharingConfig(TypedDict, closed=True):
    strategy: NotRequired[
        "capo_sagemaker.types.resource_sharing_strategy.ResourceSharingStrategy"
    ]
    """<p>The strategy of how idle compute is shared within the cluster. The following are the options of strategies.</p> <ul> <li> <p> <code>DontLend</code>: entities do not lend idle compute.</p> </li> <li> <p> <code>Lend</code>: entities can lend idle compute to entities that can borrow.</p> </li> <li> <p> <code>LendandBorrow</code>: entities can lend idle compute and borrow idle compute from other entities.</p> </li> </ul> <p>Default is <code>LendandBorrow</code>.</p>"""
    borrow_limit: NotRequired["capo_sagemaker.types.borrow_limit.BorrowLimit"]
    """<p>The limit on how much idle compute can be borrowed.The values can be 1 - 500 percent of idle compute that the team is allowed to borrow.</p> <p>Default is <code>50</code>.</p>"""
    absolute_borrow_limits: NotRequired[
        "capo_sagemaker.types.absolute_borrow_limit_resource_list.AbsoluteBorrowLimitResourceList"
    ]
    """<p>The absolute limits on compute resources that can be borrowed from idle compute. When specified, these limits define the maximum amount of specific resource types (such as accelerators, vCPU, or memory) that an entity can borrow, regardless of the percentage-based <code>BorrowLimit</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSharingConfig) -> dict:
    out: dict = {}
    if "strategy" in value:
        import capo_sagemaker.types.resource_sharing_strategy

        out["Strategy"] = (
            capo_sagemaker.types.resource_sharing_strategy.serialize_aws_json_1_1(
                value["strategy"]
            )
        )
    if "borrow_limit" in value:
        out["BorrowLimit"] = value["borrow_limit"]
    if "absolute_borrow_limits" in value:
        import capo_sagemaker.types.absolute_borrow_limit_resource_list

        out["AbsoluteBorrowLimits"] = (
            capo_sagemaker.types.absolute_borrow_limit_resource_list.serialize_aws_json_1_1(
                value["absolute_borrow_limits"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceSharingConfig:
    out: ResourceSharingConfig = {}  # type: ignore[typeddict-item]
    if "Strategy" in data:
        import capo_sagemaker.types.resource_sharing_strategy

        out["strategy"] = (
            capo_sagemaker.types.resource_sharing_strategy.deserialize_aws_json_1_1(
                data["Strategy"]
            )
        )
    if "BorrowLimit" in data:
        out["borrow_limit"] = data["BorrowLimit"]
    if "AbsoluteBorrowLimits" in data:
        import capo_sagemaker.types.absolute_borrow_limit_resource_list

        out["absolute_borrow_limits"] = (
            capo_sagemaker.types.absolute_borrow_limit_resource_list.deserialize_aws_json_1_1(
                data["AbsoluteBorrowLimits"]
            )
        )
    return out
