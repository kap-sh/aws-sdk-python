"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EstimatedMonthlySavings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.savings_estimation_mode


class EstimatedMonthlySavings(TypedDict, closed=True):
    currency: "str"
    """<p> The currency of the estimated savings. </p>"""
    before_discount_savings: "float"
    """<p> The estimated monthly savings before applying any discounts. </p>"""
    after_discount_savings: "float"
    """<p> The estimated monthly savings after applying any discounts. </p>"""
    savings_estimation_mode: "aws_sdk_compute_optimizer_automation.types.savings_estimation_mode.SavingsEstimationMode"
    """<p>The mode used to calculate savings, either BeforeDiscount or AfterDiscount.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EstimatedMonthlySavings) -> dict:
    out: dict = {}
    out["currency"] = value["currency"]
    out["beforeDiscountSavings"] = value["before_discount_savings"]
    out["afterDiscountSavings"] = value["after_discount_savings"]
    import aws_sdk_compute_optimizer_automation.types.savings_estimation_mode

    out["savingsEstimationMode"] = (
        aws_sdk_compute_optimizer_automation.types.savings_estimation_mode.serialize_aws_json_1_0(
            value["savings_estimation_mode"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EstimatedMonthlySavings:
    out: EstimatedMonthlySavings = {}  # type: ignore[typeddict-item]
    if "currency" in data:
        out["currency"] = data["currency"]
    else:
        raise DeserializationError("EstimatedMonthlySavings.currency required")
    if "beforeDiscountSavings" in data:
        out["before_discount_savings"] = data["beforeDiscountSavings"]
    else:
        raise DeserializationError(
            "EstimatedMonthlySavings.before_discount_savings required"
        )
    if "afterDiscountSavings" in data:
        out["after_discount_savings"] = data["afterDiscountSavings"]
    else:
        raise DeserializationError(
            "EstimatedMonthlySavings.after_discount_savings required"
        )
    if "savingsEstimationMode" in data:
        import aws_sdk_compute_optimizer_automation.types.savings_estimation_mode

        out["savings_estimation_mode"] = (
            aws_sdk_compute_optimizer_automation.types.savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    else:
        raise DeserializationError(
            "EstimatedMonthlySavings.savings_estimation_mode required"
        )
    return out
