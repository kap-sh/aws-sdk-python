"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#PreferredCommitment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.payment_option
    import capo_cost_optimization_hub.types.term


class PreferredCommitment(TypedDict, closed=True):
    term: NotRequired["capo_cost_optimization_hub.types.term.Term"]
    """<p>The preferred length of the commitment period. If the value is null, it will default to <code>ThreeYears</code> (highest savings) where applicable.</p>"""
    payment_option: NotRequired[
        "capo_cost_optimization_hub.types.payment_option.PaymentOption"
    ]
    """<p>The preferred upfront payment structure for commitments. If the value is null, it will default to <code>AllUpfront</code> (highest savings) where applicable.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreferredCommitment) -> dict:
    out: dict = {}
    if "term" in value:
        import capo_cost_optimization_hub.types.term

        out["term"] = capo_cost_optimization_hub.types.term.serialize_aws_json_1_0(
            value["term"]
        )
    if "payment_option" in value:
        import capo_cost_optimization_hub.types.payment_option

        out["paymentOption"] = (
            capo_cost_optimization_hub.types.payment_option.serialize_aws_json_1_0(
                value["payment_option"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PreferredCommitment:
    out: PreferredCommitment = {}  # type: ignore[typeddict-item]
    if "term" in data:
        import capo_cost_optimization_hub.types.term

        out["term"] = capo_cost_optimization_hub.types.term.deserialize_aws_json_1_0(
            data["term"]
        )
    if "paymentOption" in data:
        import capo_cost_optimization_hub.types.payment_option

        out["payment_option"] = (
            capo_cost_optimization_hub.types.payment_option.deserialize_aws_json_1_0(
                data["paymentOption"]
            )
        )
    return out
