"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BudgetParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.access_budget_type
    import aws_sdk_cleanrooms.types.auto_refresh_mode
    import aws_sdk_cleanrooms.types.budget


class BudgetParameter(TypedDict):
    type: "aws_sdk_cleanrooms.types.access_budget_type.AccessBudgetType"
    """<p>The type of budget parameter being configured.</p>"""
    budget: "aws_sdk_cleanrooms.types.budget.Budget"
    """<p>The budget allocation amount for this specific parameter.</p>"""
    auto_refresh: NotRequired[
        "aws_sdk_cleanrooms.types.auto_refresh_mode.AutoRefreshMode"
    ]
    """<p>Whether this individual budget parameter automatically refreshes when the budget period resets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BudgetParameter) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.access_budget_type

    out["type"] = aws_sdk_cleanrooms.types.access_budget_type.serialize_json(
        value["type"]
    )
    out["budget"] = value["budget"]
    if "auto_refresh" in value:
        import aws_sdk_cleanrooms.types.auto_refresh_mode

        out["autoRefresh"] = aws_sdk_cleanrooms.types.auto_refresh_mode.serialize_json(
            value["auto_refresh"]
        )
    return out


def deserialize_json(data: dict) -> BudgetParameter:
    out: BudgetParameter = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_cleanrooms.types.access_budget_type

        out["type"] = aws_sdk_cleanrooms.types.access_budget_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("BudgetParameter.type required")
    if "budget" in data:
        out["budget"] = data["budget"]
    else:
        raise DeserializationError("BudgetParameter.budget required")
    if "autoRefresh" in data:
        import aws_sdk_cleanrooms.types.auto_refresh_mode

        out["auto_refresh"] = (
            aws_sdk_cleanrooms.types.auto_refresh_mode.deserialize_json(
                data["autoRefresh"]
            )
        )
    return out
