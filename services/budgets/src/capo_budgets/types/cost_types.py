"""Generated from Smithy shape ``com.amazonaws.budgets#CostTypes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.nullable_boolean


class CostTypes(TypedDict, closed=True):
    include_tax: NotRequired["capo_budgets.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether a budget includes taxes.</p> <p>The default value is <code>true</code>.</p>"""
    include_subscription: NotRequired[
        "capo_budgets.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether a budget includes subscriptions.</p> <p>The default value is <code>true</code>.</p>"""
    use_blended: NotRequired["capo_budgets.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether a budget uses a blended rate.</p> <p>The default value is <code>false</code>.</p>"""
    include_refund: NotRequired["capo_budgets.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether a budget includes refunds.</p> <p>The default value is <code>true</code>.</p>"""
    include_credit: NotRequired["capo_budgets.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether a budget includes credits.</p> <p>The default value is <code>true</code>.</p>"""
    include_upfront: NotRequired["capo_budgets.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether a budget includes upfront RI costs.</p> <p>The default value is <code>true</code>.</p>"""
    include_recurring: NotRequired[
        "capo_budgets.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether a budget includes recurring fees such as monthly RI fees.</p> <p>The default value is <code>true</code>.</p>"""
    include_other_subscription: NotRequired[
        "capo_budgets.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether a budget includes non-RI subscription costs.</p> <p>The default value is <code>true</code>.</p>"""
    include_support: NotRequired["capo_budgets.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether a budget includes support subscription fees.</p> <p>The default value is <code>true</code>.</p>"""
    include_discount: NotRequired["capo_budgets.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether a budget includes discounts.</p> <p>The default value is <code>true</code>.</p>"""
    use_amortized: NotRequired["capo_budgets.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether a budget uses the amortized rate.</p> <p>The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostTypes) -> dict:
    out: dict = {}
    if "include_tax" in value:
        out["IncludeTax"] = value["include_tax"]
    if "include_subscription" in value:
        out["IncludeSubscription"] = value["include_subscription"]
    if "use_blended" in value:
        out["UseBlended"] = value["use_blended"]
    if "include_refund" in value:
        out["IncludeRefund"] = value["include_refund"]
    if "include_credit" in value:
        out["IncludeCredit"] = value["include_credit"]
    if "include_upfront" in value:
        out["IncludeUpfront"] = value["include_upfront"]
    if "include_recurring" in value:
        out["IncludeRecurring"] = value["include_recurring"]
    if "include_other_subscription" in value:
        out["IncludeOtherSubscription"] = value["include_other_subscription"]
    if "include_support" in value:
        out["IncludeSupport"] = value["include_support"]
    if "include_discount" in value:
        out["IncludeDiscount"] = value["include_discount"]
    if "use_amortized" in value:
        out["UseAmortized"] = value["use_amortized"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CostTypes:
    out: CostTypes = {}  # type: ignore[typeddict-item]
    if "IncludeTax" in data:
        out["include_tax"] = data["IncludeTax"]
    if "IncludeSubscription" in data:
        out["include_subscription"] = data["IncludeSubscription"]
    if "UseBlended" in data:
        out["use_blended"] = data["UseBlended"]
    if "IncludeRefund" in data:
        out["include_refund"] = data["IncludeRefund"]
    if "IncludeCredit" in data:
        out["include_credit"] = data["IncludeCredit"]
    if "IncludeUpfront" in data:
        out["include_upfront"] = data["IncludeUpfront"]
    if "IncludeRecurring" in data:
        out["include_recurring"] = data["IncludeRecurring"]
    if "IncludeOtherSubscription" in data:
        out["include_other_subscription"] = data["IncludeOtherSubscription"]
    if "IncludeSupport" in data:
        out["include_support"] = data["IncludeSupport"]
    if "IncludeDiscount" in data:
        out["include_discount"] = data["IncludeDiscount"]
    if "UseAmortized" in data:
        out["use_amortized"] = data["UseAmortized"]
    return out
