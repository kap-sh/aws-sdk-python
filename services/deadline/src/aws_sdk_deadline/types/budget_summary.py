"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.budget_id
    import aws_sdk_deadline.types.budget_status
    import aws_sdk_deadline.types.consumed_usage_limit
    import aws_sdk_deadline.types.consumed_usages
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by
    import aws_sdk_deadline.types.usage_tracking_resource


class BudgetSummary(TypedDict):
    budget_id: "aws_sdk_deadline.types.budget_id.BudgetId"
    """<p>The budget ID.</p>"""
    usage_tracking_resource: (
        "aws_sdk_deadline.types.usage_tracking_resource.UsageTrackingResource"
    )
    """<p>The resource used to track expenditure in the budget.</p>"""
    status: "aws_sdk_deadline.types.budget_status.BudgetStatus"
    """<p>The status of the budget.</p> <ul> <li> <p> <code>ACTIVE</code>–The budget is being evaluated.</p> </li> <li> <p> <code>INACTIVE</code>–The budget is inactive. This can include Expired, Canceled, or deleted Deleted statuses.</p> </li> </ul>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The display name of the budget summary to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    approximate_dollar_limit: (
        "aws_sdk_deadline.types.consumed_usage_limit.ConsumedUsageLimit"
    )
    """<p>The approximate dollar limit of the budget.</p>"""
    usages: "aws_sdk_deadline.types.consumed_usages.ConsumedUsages"
    """<p>The consumed usage for the budget.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    description: NotRequired["aws_sdk_deadline.types.description.Description"]
    """<p>The description of the budget summary.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: BudgetSummary) -> dict:
    out: dict = {}
    out["budgetId"] = value["budget_id"]
    import aws_sdk_deadline.types.usage_tracking_resource

    out["usageTrackingResource"] = (
        aws_sdk_deadline.types.usage_tracking_resource.serialize_json(
            value["usage_tracking_resource"]
        )
    )
    import aws_sdk_deadline.types.budget_status

    out["status"] = aws_sdk_deadline.types.budget_status.serialize_json(value["status"])
    out["displayName"] = value["display_name"]
    out["approximateDollarLimit"] = value["approximate_dollar_limit"]
    import aws_sdk_deadline.types.consumed_usages

    out["usages"] = aws_sdk_deadline.types.consumed_usages.serialize_json(
        value["usages"]
    )
    out["createdBy"] = value["created_by"]
    import aws_sdk_deadline.types.created_at

    out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BudgetSummary:
    out: BudgetSummary = {}  # type: ignore[typeddict-item]
    if "budgetId" in data:
        out["budget_id"] = data["budgetId"]
    else:
        raise DeserializationError("BudgetSummary.budget_id required")
    if "usageTrackingResource" in data:
        import aws_sdk_deadline.types.usage_tracking_resource

        out["usage_tracking_resource"] = (
            aws_sdk_deadline.types.usage_tracking_resource.deserialize_json(
                data["usageTrackingResource"]
            )
        )
    else:
        raise DeserializationError("BudgetSummary.usage_tracking_resource required")
    if "status" in data:
        import aws_sdk_deadline.types.budget_status

        out["status"] = aws_sdk_deadline.types.budget_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("BudgetSummary.status required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("BudgetSummary.display_name required")
    if "approximateDollarLimit" in data:
        out["approximate_dollar_limit"] = data["approximateDollarLimit"]
    else:
        raise DeserializationError("BudgetSummary.approximate_dollar_limit required")
    if "usages" in data:
        import aws_sdk_deadline.types.consumed_usages

        out["usages"] = aws_sdk_deadline.types.consumed_usages.deserialize_json(
            data["usages"]
        )
    else:
        raise DeserializationError("BudgetSummary.usages required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("BudgetSummary.created_by required")
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("BudgetSummary.created_at required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
