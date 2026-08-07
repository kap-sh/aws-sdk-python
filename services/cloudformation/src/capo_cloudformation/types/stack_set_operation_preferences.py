"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.concurrency_mode
    import capo_cloudformation.types.failure_tolerance_count
    import capo_cloudformation.types.failure_tolerance_percentage
    import capo_cloudformation.types.max_concurrent_count
    import capo_cloudformation.types.max_concurrent_percentage
    import capo_cloudformation.types.region_concurrency_type
    import capo_cloudformation.types.region_list


class StackSetOperationPreferences(TypedDict, closed=True):
    region_concurrency_type: NotRequired[
        "capo_cloudformation.types.region_concurrency_type.RegionConcurrencyType"
    ]
    """<p>The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.</p>"""
    region_order: NotRequired["capo_cloudformation.types.region_list.RegionList"]
    """<p>The order of the Regions where you want to perform the stack operation.</p>"""
    failure_tolerance_count: NotRequired[
        "capo_cloudformation.types.failure_tolerance_count.FailureToleranceCount"
    ]
    """<p>The number of accounts per Region this operation can fail in before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't attempt the operation in any subsequent Regions.</p> <p>You can specify either <code>FailureToleranceCount</code> or <code>FailureTolerancePercentage</code>, but not both.</p> <p>By default, <code>0</code> is specified.</p>"""
    failure_tolerance_percentage: NotRequired[
        "capo_cloudformation.types.failure_tolerance_percentage.FailureTolerancePercentage"
    ]
    """<p>The percentage of accounts per Region this stack operation can fail in before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't attempt the operation in any subsequent Regions.</p> <p>When calculating the number of accounts based on the specified percentage, CloudFormation rounds <i>down</i> to the next whole number.</p> <p>You can specify either <code>FailureToleranceCount</code> or <code>FailureTolerancePercentage</code>, but not both.</p> <p>By default, <code>0</code> is specified.</p>"""
    max_concurrent_count: NotRequired[
        "capo_cloudformation.types.max_concurrent_count.MaxConcurrentCount"
    ]
    """<p>The maximum number of accounts in which to perform this operation at one time. This can depend on the value of <code>FailureToleranceCount</code> depending on your <code>ConcurrencyMode</code>. <code>MaxConcurrentCount</code> is at most one more than the <code>FailureToleranceCount</code> if you're using <code>STRICT_FAILURE_TOLERANCE</code>.</p> <p>Note that this setting lets you specify the <i>maximum</i> for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.</p> <p>You can specify either <code>MaxConcurrentCount</code> or <code>MaxConcurrentPercentage</code>, but not both.</p> <p>By default, <code>1</code> is specified.</p>"""
    max_concurrent_percentage: NotRequired[
        "capo_cloudformation.types.max_concurrent_percentage.MaxConcurrentPercentage"
    ]
    """<p>The maximum percentage of accounts in which to perform this operation at one time.</p> <p>When calculating the number of accounts based on the specified percentage, CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.</p> <p>Note that this setting lets you specify the <i>maximum</i> for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.</p> <p>You can specify either <code>MaxConcurrentCount</code> or <code>MaxConcurrentPercentage</code>, but not both.</p> <p>By default, <code>1</code> is specified.</p>"""
    concurrency_mode: NotRequired[
        "capo_cloudformation.types.concurrency_mode.ConcurrencyMode"
    ]
    """<p>Specifies how the concurrency level behaves during the operation execution.</p> <ul> <li> <p> <code>STRICT_FAILURE_TOLERANCE</code>: This option dynamically lowers the concurrency level to ensure the number of failed accounts never exceeds the value of <code>FailureToleranceCount</code> +1. The initial actual concurrency is set to the lower of either the value of the <code>MaxConcurrentCount</code>, or the value of <code>FailureToleranceCount</code> +1. The actual concurrency is then reduced proportionally by the number of failures. This is the default behavior.</p> <p>If failure tolerance or Maximum concurrent accounts are set to percentages, the behavior is similar.</p> </li> <li> <p> <code>SOFT_FAILURE_TOLERANCE</code>: This option decouples <code>FailureToleranceCount</code> from the actual concurrency. This allows StackSet operations to run at the concurrency level set by the <code>MaxConcurrentCount</code> value, or <code>MaxConcurrentPercentage</code>, regardless of the number of failures.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetOperationPreferences, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "region_concurrency_type" in value:
        import capo_cloudformation.types.region_concurrency_type

        capo_cloudformation.types.region_concurrency_type.serialize_query(
            value["region_concurrency_type"],
            pairs,
            f"{key_prefix}RegionConcurrencyType",
        )
    if "region_order" in value:
        import capo_cloudformation.types.region_list

        capo_cloudformation.types.region_list.serialize_query(
            value["region_order"], pairs, f"{key_prefix}RegionOrder"
        )
    if "failure_tolerance_count" in value:
        pairs.append(
            (
                f"{key_prefix}FailureToleranceCount",
                str(value["failure_tolerance_count"]),
            )
        )
    if "failure_tolerance_percentage" in value:
        pairs.append(
            (
                f"{key_prefix}FailureTolerancePercentage",
                str(value["failure_tolerance_percentage"]),
            )
        )
    if "max_concurrent_count" in value:
        pairs.append(
            (f"{key_prefix}MaxConcurrentCount", str(value["max_concurrent_count"]))
        )
    if "max_concurrent_percentage" in value:
        pairs.append(
            (
                f"{key_prefix}MaxConcurrentPercentage",
                str(value["max_concurrent_percentage"]),
            )
        )
    if "concurrency_mode" in value:
        import capo_cloudformation.types.concurrency_mode

        capo_cloudformation.types.concurrency_mode.serialize_query(
            value["concurrency_mode"], pairs, f"{key_prefix}ConcurrencyMode"
        )


def deserialize_query(el: Element) -> StackSetOperationPreferences:
    out: StackSetOperationPreferences = {}  # type: ignore[typeddict-item]
    child_region_concurrency_type = el.find("RegionConcurrencyType")
    if child_region_concurrency_type is not None:
        import capo_cloudformation.types.region_concurrency_type

        out["region_concurrency_type"] = (
            capo_cloudformation.types.region_concurrency_type.deserialize_query(
                child_region_concurrency_type
            )
        )
    child_region_order = el.find("RegionOrder")
    if child_region_order is not None:
        import capo_cloudformation.types.region_list

        out["region_order"] = capo_cloudformation.types.region_list.deserialize_query(
            child_region_order
        )
    child_failure_tolerance_count = el.find("FailureToleranceCount")
    if child_failure_tolerance_count is not None:
        out["failure_tolerance_count"] = int(child_failure_tolerance_count.text or "")
    child_failure_tolerance_percentage = el.find("FailureTolerancePercentage")
    if child_failure_tolerance_percentage is not None:
        out["failure_tolerance_percentage"] = int(
            child_failure_tolerance_percentage.text or ""
        )
    child_max_concurrent_count = el.find("MaxConcurrentCount")
    if child_max_concurrent_count is not None:
        out["max_concurrent_count"] = int(child_max_concurrent_count.text or "")
    child_max_concurrent_percentage = el.find("MaxConcurrentPercentage")
    if child_max_concurrent_percentage is not None:
        out["max_concurrent_percentage"] = int(
            child_max_concurrent_percentage.text or ""
        )
    child_concurrency_mode = el.find("ConcurrencyMode")
    if child_concurrency_mode is not None:
        import capo_cloudformation.types.concurrency_mode

        out["concurrency_mode"] = (
            capo_cloudformation.types.concurrency_mode.deserialize_query(
                child_concurrency_mode
            )
        )
    return out
