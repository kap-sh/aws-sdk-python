"""Generated from Smithy shape ``com.amazonaws.autoscaling#PutWarmPoolType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_reuse_policy
    import capo_auto_scaling.types.max_group_prepared_capacity
    import capo_auto_scaling.types.warm_pool_min_size
    import capo_auto_scaling.types.warm_pool_state
    import capo_auto_scaling.types.xml_string_max_len255


class PutWarmPoolType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    max_group_prepared_capacity: NotRequired[
        "capo_auto_scaling.types.max_group_prepared_capacity.MaxGroupPreparedCapacity"
    ]
    """<p>Specifies the maximum number of instances that are allowed to be in the warm pool or in any state except <code>Terminated</code> for the Auto Scaling group. This is an optional property. Specify it only if you do not want the warm pool size to be determined by the difference between the group's maximum capacity and its desired capacity. </p> <important> <p>If a value for <code>MaxGroupPreparedCapacity</code> is not specified, Amazon EC2 Auto Scaling launches and maintains the difference between the group's maximum capacity and its desired capacity. If you specify a value for <code>MaxGroupPreparedCapacity</code>, Amazon EC2 Auto Scaling uses the difference between the <code>MaxGroupPreparedCapacity</code> and the desired capacity instead. </p> <p>The size of the warm pool is dynamic. Only when <code>MaxGroupPreparedCapacity</code> and <code>MinSize</code> are set to the same value does the warm pool have an absolute size.</p> </important> <p>If the desired capacity of the Auto Scaling group is higher than the <code>MaxGroupPreparedCapacity</code>, the capacity of the warm pool is 0, unless you specify a value for <code>MinSize</code>. To remove a value that you previously set, include the property but specify -1 for the value. </p>"""
    min_size: NotRequired["capo_auto_scaling.types.warm_pool_min_size.WarmPoolMinSize"]
    """<p>Specifies the minimum number of instances to maintain in the warm pool. This helps you to ensure that there is always a certain number of warmed instances available to handle traffic spikes. Defaults to 0 if not specified.</p>"""
    pool_state: NotRequired["capo_auto_scaling.types.warm_pool_state.WarmPoolState"]
    """<p>Sets the instance state to transition to after the lifecycle actions are complete. Default is <code>Stopped</code>.</p>"""
    instance_reuse_policy: NotRequired[
        "capo_auto_scaling.types.instance_reuse_policy.InstanceReusePolicy"
    ]
    """<p>Indicates whether instances in the Auto Scaling group can be returned to the warm pool on scale in. The default is to terminate instances in the Auto Scaling group when the group scales in.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutWarmPoolType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "max_group_prepared_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}MaxGroupPreparedCapacity",
                str(value["max_group_prepared_capacity"]),
            )
        )
    if "min_size" in value:
        pairs.append((f"{key_prefix}MinSize", str(value["min_size"])))
    if "pool_state" in value:
        import capo_auto_scaling.types.warm_pool_state

        capo_auto_scaling.types.warm_pool_state.serialize_query(
            value["pool_state"], pairs, f"{key_prefix}PoolState"
        )
    if "instance_reuse_policy" in value:
        import capo_auto_scaling.types.instance_reuse_policy

        capo_auto_scaling.types.instance_reuse_policy.serialize_query(
            value["instance_reuse_policy"], pairs, f"{key_prefix}InstanceReusePolicy"
        )


def deserialize_query(el: Element) -> PutWarmPoolType:
    out: PutWarmPoolType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
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
    child_instance_reuse_policy = el.find("InstanceReusePolicy")
    if child_instance_reuse_policy is not None:
        import capo_auto_scaling.types.instance_reuse_policy

        out["instance_reuse_policy"] = (
            capo_auto_scaling.types.instance_reuse_policy.deserialize_query(
                child_instance_reuse_policy
            )
        )
    return out
