"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudFormationCostEstimationResourceCollectionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.cost_estimation_stack_names


class CloudFormationCostEstimationResourceCollectionFilter(TypedDict, closed=True):
    stack_names: NotRequired[
        "capo_devops_guru.types.cost_estimation_stack_names.CostEstimationStackNames"
    ]
    """<p>An array of CloudFormation stack names. Its size is fixed at 1 item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudFormationCostEstimationResourceCollectionFilter) -> dict:
    out: dict = {}
    if "stack_names" in value:
        import capo_devops_guru.types.cost_estimation_stack_names

        out["StackNames"] = (
            capo_devops_guru.types.cost_estimation_stack_names.serialize_json(
                value["stack_names"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> CloudFormationCostEstimationResourceCollectionFilter:
    out: CloudFormationCostEstimationResourceCollectionFilter = {}  # type: ignore[typeddict-item]
    if "StackNames" in data:
        import capo_devops_guru.types.cost_estimation_stack_names

        out["stack_names"] = (
            capo_devops_guru.types.cost_estimation_stack_names.deserialize_json(
                data["StackNames"]
            )
        )
    return out
