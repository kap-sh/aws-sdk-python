"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceEstimatedMonthlySavings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.currency
    import capo_compute_optimizer.types.value


class InstanceEstimatedMonthlySavings(TypedDict, closed=True):
    currency: NotRequired["capo_compute_optimizer.types.currency.Currency"]
    """<p> The currency of the estimated monthly savings. </p>"""
    value: "capo_compute_optimizer.types.value.Value"
    """<p> The value of the estimated monthly savings. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceEstimatedMonthlySavings) -> dict:
    out: dict = {}
    if "currency" in value:
        import capo_compute_optimizer.types.currency

        out["currency"] = capo_compute_optimizer.types.currency.serialize_aws_json_1_0(
            value["currency"]
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceEstimatedMonthlySavings:
    out: InstanceEstimatedMonthlySavings = {}  # type: ignore[typeddict-item]
    if "currency" in data:
        import capo_compute_optimizer.types.currency

        out["currency"] = (
            capo_compute_optimizer.types.currency.deserialize_aws_json_1_0(
                data["currency"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
