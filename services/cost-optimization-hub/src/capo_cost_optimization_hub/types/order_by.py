"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#OrderBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.order


class OrderBy(TypedDict, closed=True):
    dimension: NotRequired["str"]
    """<p>Sorts by dimension values.</p>"""
    order: NotRequired["capo_cost_optimization_hub.types.order.Order"]
    """<p>The order that's used to sort the data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OrderBy) -> dict:
    out: dict = {}
    if "dimension" in value:
        out["dimension"] = value["dimension"]
    if "order" in value:
        import capo_cost_optimization_hub.types.order

        out["order"] = capo_cost_optimization_hub.types.order.serialize_aws_json_1_0(
            value["order"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OrderBy:
    out: OrderBy = {}  # type: ignore[typeddict-item]
    if "dimension" in data:
        out["dimension"] = data["dimension"]
    if "order" in data:
        import capo_cost_optimization_hub.types.order

        out["order"] = capo_cost_optimization_hub.types.order.deserialize_aws_json_1_0(
            data["order"]
        )
    return out
