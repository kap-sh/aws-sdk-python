"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#OrderBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.dimension
    import capo_compute_optimizer.types.order


class OrderBy(TypedDict, closed=True):
    dimension: NotRequired["capo_compute_optimizer.types.dimension.Dimension"]
    """<p>The dimension values to sort the recommendations.</p>"""
    order: NotRequired["capo_compute_optimizer.types.order.Order"]
    """<p>The order to sort the recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OrderBy) -> dict:
    out: dict = {}
    if "dimension" in value:
        import capo_compute_optimizer.types.dimension

        out["dimension"] = (
            capo_compute_optimizer.types.dimension.serialize_aws_json_1_0(
                value["dimension"]
            )
        )
    if "order" in value:
        import capo_compute_optimizer.types.order

        out["order"] = capo_compute_optimizer.types.order.serialize_aws_json_1_0(
            value["order"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OrderBy:
    out: OrderBy = {}  # type: ignore[typeddict-item]
    if "dimension" in data:
        import capo_compute_optimizer.types.dimension

        out["dimension"] = (
            capo_compute_optimizer.types.dimension.deserialize_aws_json_1_0(
                data["dimension"]
            )
        )
    if "order" in data:
        import capo_compute_optimizer.types.order

        out["order"] = capo_compute_optimizer.types.order.deserialize_aws_json_1_0(
            data["order"]
        )
    return out
