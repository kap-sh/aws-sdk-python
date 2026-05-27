"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderStrategyItem``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider_strategy_item_base
    import aws_sdk_ecs.types.capacity_provider_strategy_item_weight
    import aws_sdk_ecs.types.string


class CapacityProviderStrategyItem(TypedDict):
    capacity_provider: "aws_sdk_ecs.types.string.String"
    """<p>The short name of the capacity provider.</p>"""
    weight: "aws_sdk_ecs.types.capacity_provider_strategy_item_weight.CapacityProviderStrategyItemWeight"
    """<p>The <i>weight</i> value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The <code>weight</code> value is taken into consideration after the <code>base</code> value, if defined, is satisfied.</p> <p>If no <code>weight</code> value is specified, the default value of <code>0</code> is used. When multiple capacity providers are specified within a capacity provider strategy, at least one of the capacity providers must have a weight value greater than zero and any capacity providers with a weight of <code>0</code> can't be used to place tasks. If you specify multiple capacity providers in a strategy that all have a weight of <code>0</code>, any <code>RunTask</code> or <code>CreateService</code> actions using the capacity provider strategy will fail.</p> <p>Weight value characteristics:</p> <ul> <li> <p>Weight is considered after the base value is satisfied</p> </li> <li> <p>The default value is <code>0</code> if not specified</p> </li> <li> <p>The valid range is 0 to 1,000</p> </li> <li> <p>At least one capacity provider must have a weight greater than zero</p> </li> <li> <p>Capacity providers with weight of <code>0</code> cannot place tasks</p> </li> </ul> <p>Task distribution logic:</p> <ol> <li> <p>Base satisfaction: The minimum number of tasks specified by the base value are placed on that capacity provider</p> </li> <li> <p>Weight distribution: After base requirements are met, additional tasks are distributed according to weight ratios</p> </li> </ol> <p>Examples:</p> <p>Equal Distribution: Two capacity providers both with weight <code>1</code> will split tasks evenly after base requirements are met.</p> <p>Weighted Distribution: If capacityProviderA has weight <code>1</code> and capacityProviderB has weight <code>4</code>, then for every 1 task on A, 4 tasks will run on B.</p>"""
    base: "aws_sdk_ecs.types.capacity_provider_strategy_item_base.CapacityProviderStrategyItemBase"
    """<p>The <i>base</i> value designates how many tasks, at a minimum, to run on the specified capacity provider for each service. Only one capacity provider in a capacity provider strategy can have a <i>base</i> defined. If no value is specified, the default value of <code>0</code> is used.</p> <p>Base value characteristics:</p> <ul> <li> <p>Only one capacity provider in a strategy can have a base defined</p> </li> <li> <p>The default value is <code>0</code> if not specified</p> </li> <li> <p>The valid range is 0 to 100,000</p> </li> <li> <p>Base requirements are satisfied first before weight distribution</p> </li> </ul>"""
