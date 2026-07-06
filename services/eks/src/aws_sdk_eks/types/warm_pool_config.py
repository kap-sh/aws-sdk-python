"""Generated from Smithy shape ``com.amazonaws.eks#WarmPoolConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean
    import aws_sdk_eks.types.boxed_integer
    import aws_sdk_eks.types.warm_pool_state
    import aws_sdk_eks.types.zero_capacity


class WarmPoolConfig(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether to attach warm pools on the managed node group. Set to <code>true</code> to enable the warm pool, or <code>false</code> to disable and remove it. If not specified during an update, the current value is preserved.</p>"""
    min_size: NotRequired["aws_sdk_eks.types.zero_capacity.ZeroCapacity"]
    """<p>The minimum number of instances to maintain in the warm pool. Default: <code>0</code>. Size your warm pool based on scaling patterns to balance cost and availability. Start with 10-20% of expected peak capacity.</p>"""
    max_group_prepared_capacity: NotRequired[
        "aws_sdk_eks.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum total number of instances across the warm pool and Auto Scaling group combined. This value controls the total prepared capacity available for your node group.</p>"""
    pool_state: NotRequired["aws_sdk_eks.types.warm_pool_state.WarmPoolState"]
    """<p>The desired state for warm pool instances. Default: <code>Stopped</code>. Valid values are <code>Stopped</code> (most cost-effective with EBS storage costs only), <code>Running</code> (fastest transition time with full EC2 costs), and <code>Hibernated</code> (balance between cost and speed, only supported on specific instance types). Warm pool instances in the <code>Hibernated</code> state are not supported with Bottlerocket AMIs.</p>"""
    reuse_on_scale_in: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether instances should return to the warm pool during scale-in events instead of being terminated. Default: <code>false</code>. Enable this to reduce costs by reusing instances. This feature is not supported for Bottlerocket AMIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WarmPoolConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "min_size" in value:
        out["minSize"] = value["min_size"]
    if "max_group_prepared_capacity" in value:
        out["maxGroupPreparedCapacity"] = value["max_group_prepared_capacity"]
    if "pool_state" in value:
        import aws_sdk_eks.types.warm_pool_state

        out["poolState"] = aws_sdk_eks.types.warm_pool_state.serialize_json(
            value["pool_state"]
        )
    if "reuse_on_scale_in" in value:
        out["reuseOnScaleIn"] = value["reuse_on_scale_in"]
    return out


def deserialize_json(data: dict) -> WarmPoolConfig:
    out: WarmPoolConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "minSize" in data:
        out["min_size"] = data["minSize"]
    if "maxGroupPreparedCapacity" in data:
        out["max_group_prepared_capacity"] = data["maxGroupPreparedCapacity"]
    if "poolState" in data:
        import aws_sdk_eks.types.warm_pool_state

        out["pool_state"] = aws_sdk_eks.types.warm_pool_state.deserialize_json(
            data["poolState"]
        )
    if "reuseOnScaleIn" in data:
        out["reuse_on_scale_in"] = data["reuseOnScaleIn"]
    return out
