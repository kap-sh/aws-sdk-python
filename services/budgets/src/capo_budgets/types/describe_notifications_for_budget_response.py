"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeNotificationsForBudgetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.generic_string
    import capo_budgets.types.notifications


class DescribeNotificationsForBudgetResponse(TypedDict, closed=True):
    notifications: NotRequired["capo_budgets.types.notifications.Notifications"]
    """<p>A list of notifications that are associated with a budget.</p>"""
    next_token: NotRequired["capo_budgets.types.generic_string.GenericString"]
    """<p>The pagination token in the service response that indicates the next set of results that you can retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNotificationsForBudgetResponse) -> dict:
    out: dict = {}
    if "notifications" in value:
        import capo_budgets.types.notifications

        out["Notifications"] = capo_budgets.types.notifications.serialize_aws_json_1_1(
            value["notifications"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNotificationsForBudgetResponse:
    out: DescribeNotificationsForBudgetResponse = {}  # type: ignore[typeddict-item]
    if "Notifications" in data:
        import capo_budgets.types.notifications

        out["notifications"] = (
            capo_budgets.types.notifications.deserialize_aws_json_1_1(
                data["Notifications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
