"""Generated from Smithy shape ``com.amazonaws.autoscaling#WarmPoolConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_reuse_policy
    import capo_auto_scaling.types.max_group_prepared_capacity
    import capo_auto_scaling.types.warm_pool_min_size
    import capo_auto_scaling.types.warm_pool_state
    import capo_auto_scaling.types.warm_pool_status


class WarmPoolConfiguration(TypedDict, closed=True):
    max_group_prepared_capacity: NotRequired[
        "capo_auto_scaling.types.max_group_prepared_capacity.MaxGroupPreparedCapacity"
    ]
    """<p>The maximum number of instances that are allowed to be in the warm pool or in any state except <code>Terminated</code> for the Auto Scaling group.</p>"""
    min_size: NotRequired["capo_auto_scaling.types.warm_pool_min_size.WarmPoolMinSize"]
    """<p>The minimum number of instances to maintain in the warm pool.</p>"""
    pool_state: NotRequired["capo_auto_scaling.types.warm_pool_state.WarmPoolState"]
    """<p>The instance state to transition to after the lifecycle actions are complete.</p>"""
    status: NotRequired["capo_auto_scaling.types.warm_pool_status.WarmPoolStatus"]
    """<p>The status of a warm pool that is marked for deletion.</p>"""
    instance_reuse_policy: NotRequired[
        "capo_auto_scaling.types.instance_reuse_policy.InstanceReusePolicy"
    ]
    """<p>The instance reuse policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: WarmPoolConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "max_group_prepared_capacity" in value:
        pairs.append(
            (
                f"{prefix}.MaxGroupPreparedCapacity",
                str(value["max_group_prepared_capacity"]),
            )
        )
    if "min_size" in value:
        pairs.append((f"{prefix}.MinSize", str(value["min_size"])))
    if "pool_state" in value:
        import capo_auto_scaling.types.warm_pool_state

        capo_auto_scaling.types.warm_pool_state.serialize_query(
            value["pool_state"], pairs, f"{prefix}.PoolState"
        )
    if "status" in value:
        import capo_auto_scaling.types.warm_pool_status

        capo_auto_scaling.types.warm_pool_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "instance_reuse_policy" in value:
        import capo_auto_scaling.types.instance_reuse_policy

        capo_auto_scaling.types.instance_reuse_policy.serialize_query(
            value["instance_reuse_policy"], pairs, f"{prefix}.InstanceReusePolicy"
        )


def deserialize_query(el: Element) -> WarmPoolConfiguration:
    out: WarmPoolConfiguration = {}  # type: ignore[typeddict-item]
    child_max_group_prepared_capacity = el.find("MaxGroupPreparedCapacity")
    if child_max_group_prepared_capacity is not None:
        out["max_group_prepared_capacity"] = int(
            child_max_group_prepared_capacity.text or ""
        )
    child_min_size = el.find("MinSize")
    if child_min_size is not None:
        out["min_size"] = int(child_min_size.text or "")
    child_pool_state = el.find("PoolState")
    if child_pool_state is not None:
        import capo_auto_scaling.types.warm_pool_state

        out["pool_state"] = capo_auto_scaling.types.warm_pool_state.deserialize_query(
            child_pool_state
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_auto_scaling.types.warm_pool_status

        out["status"] = capo_auto_scaling.types.warm_pool_status.deserialize_query(
            child_status
        )
    child_instance_reuse_policy = el.find("InstanceReusePolicy")
    if child_instance_reuse_policy is not None:
        import capo_auto_scaling.types.instance_reuse_policy

        out["instance_reuse_policy"] = (
            capo_auto_scaling.types.instance_reuse_policy.deserialize_query(
                child_instance_reuse_policy
            )
        )
    return out
