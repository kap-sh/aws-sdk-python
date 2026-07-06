"""Generated from Smithy shape ``com.amazonaws.budgets#HealthStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_budgets.types.generic_timestamp
    import aws_sdk_budgets.types.health_status_reason
    import aws_sdk_budgets.types.health_status_value


class HealthStatus(TypedDict, closed=True):
    status: NotRequired["aws_sdk_budgets.types.health_status_value.HealthStatusValue"]
    """<p>The current status of the billing view resource.</p>"""
    status_reason: NotRequired[
        "aws_sdk_budgets.types.health_status_reason.HealthStatusReason"
    ]
    """<p>The reason for the current status.</p> <ul> <li> <p> <code>BILLING_VIEW_NO_ACCESS</code>: The billing view resource does not grant <code>billing:GetBillingViewData</code> permission to this account.</p> </li> <li> <p> <code>BILLING_VIEW_UNHEALTHY</code>: The billing view associated with the budget is unhealthy.</p> </li> <li> <p> <code>FILTER_INVALID</code>: The filter contains reference to an account you do not have access to.</p> </li> <li> <p> <code>MULTI_YEAR_HISTORICAL_DATA_DISABLED</code>: The budget is not being updated. Enable multi-year historical data in your Cost Management preferences.</p> </li> </ul>"""
    last_updated_time: NotRequired[
        "aws_sdk_budgets.types.generic_timestamp.GenericTimestamp"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_budgets.types.health_status_value

        out["Status"] = (
            aws_sdk_budgets.types.health_status_value.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        import aws_sdk_budgets.types.health_status_reason

        out["StatusReason"] = (
            aws_sdk_budgets.types.health_status_reason.serialize_aws_json_1_1(
                value["status_reason"]
            )
        )
    if "last_updated_time" in value:
        import aws_sdk_budgets.types.generic_timestamp

        out["LastUpdatedTime"] = (
            aws_sdk_budgets.types.generic_timestamp.serialize_aws_json_1_1(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HealthStatus:
    out: HealthStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_budgets.types.health_status_value

        out["status"] = (
            aws_sdk_budgets.types.health_status_value.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        import aws_sdk_budgets.types.health_status_reason

        out["status_reason"] = (
            aws_sdk_budgets.types.health_status_reason.deserialize_aws_json_1_1(
                data["StatusReason"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_budgets.types.generic_timestamp

        out["last_updated_time"] = (
            aws_sdk_budgets.types.generic_timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    return out
