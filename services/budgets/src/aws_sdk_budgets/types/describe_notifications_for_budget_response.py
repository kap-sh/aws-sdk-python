"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeNotificationsForBudgetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_budgets.types.generic_string
    import aws_sdk_budgets.types.notifications


class DescribeNotificationsForBudgetResponse(TypedDict):
    notifications: NotRequired["aws_sdk_budgets.types.notifications.Notifications"]
    """<p>A list of notifications that are associated with a budget.</p>"""
    next_token: NotRequired["aws_sdk_budgets.types.generic_string.GenericString"]
    """<p>The pagination token in the service response that indicates the next set of results that you can retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNotificationsForBudgetResponse) -> dict:
    out: dict = {}
    if "notifications" in value:
        import aws_sdk_budgets.types.notifications

        out["Notifications"] = (
            aws_sdk_budgets.types.notifications.serialize_aws_json_1_1(
                value["notifications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNotificationsForBudgetResponse:
    out: DescribeNotificationsForBudgetResponse = {}  # type: ignore[typeddict-item]
    if "Notifications" in data:
        import aws_sdk_budgets.types.notifications

        out["notifications"] = (
            aws_sdk_budgets.types.notifications.deserialize_aws_json_1_1(
                data["Notifications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
