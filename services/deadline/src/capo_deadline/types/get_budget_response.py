"""Generated from Smithy shape ``com.amazonaws.deadline#GetBudgetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.budget_id
    import capo_deadline.types.budget_schedule
    import capo_deadline.types.budget_status
    import capo_deadline.types.consumed_usage_limit
    import capo_deadline.types.consumed_usages
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.description
    import capo_deadline.types.resource_name
    import capo_deadline.types.response_budget_action_list
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by
    import capo_deadline.types.usage_tracking_resource


class GetBudgetResponse(TypedDict, closed=True):
    budget_id: "capo_deadline.types.budget_id.BudgetId"
    """<p>The budget ID.</p>"""
    usage_tracking_resource: (
        "capo_deadline.types.usage_tracking_resource.UsageTrackingResource"
    )
    """<p>The resource that the budget is tracking usage for.</p>"""
    status: "capo_deadline.types.budget_status.BudgetStatus"
    """<p>The status of the budget.</p> <ul> <li> <p> <code>ACTIVE</code>–Get a budget being evaluated.</p> </li> <li> <p> <code>INACTIVE</code>–Get an inactive budget. This can include expired, canceled, or deleted statuses.</p> </li> </ul>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the budget.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    approximate_dollar_limit: (
        "capo_deadline.types.consumed_usage_limit.ConsumedUsageLimit"
    )
    """<p>The consumed usage limit for the budget.</p>"""
    usages: "capo_deadline.types.consumed_usages.ConsumedUsages"
    """<p>The usages of the budget.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the budget.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    actions: "capo_deadline.types.response_budget_action_list.ResponseBudgetActionList"
    """<p>The budget actions for the budget.</p>"""
    schedule: "capo_deadline.types.budget_schedule.BudgetSchedule"
    """<p>The budget schedule.</p>"""
    queue_stopped_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the queue stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBudgetResponse) -> dict:
    out: dict = {}
    out["budgetId"] = value["budget_id"]
    import capo_deadline.types.usage_tracking_resource

    out["usageTrackingResource"] = (
        capo_deadline.types.usage_tracking_resource.serialize_json(
            value["usage_tracking_resource"]
        )
    )
    import capo_deadline.types.budget_status

    out["status"] = capo_deadline.types.budget_status.serialize_json(value["status"])
    out["displayName"] = value["display_name"]
    out["approximateDollarLimit"] = value["approximate_dollar_limit"]
    import capo_deadline.types.consumed_usages

    out["usages"] = capo_deadline.types.consumed_usages.serialize_json(value["usages"])
    out["createdBy"] = value["created_by"]
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    import capo_deadline.types.response_budget_action_list

    out["actions"] = capo_deadline.types.response_budget_action_list.serialize_json(
        value["actions"]
    )
    import capo_deadline.types.budget_schedule

    out["schedule"] = capo_deadline.types.budget_schedule.serialize_json(
        value["schedule"]
    )
    if "queue_stopped_at" in value:
        import capo_deadline.types.updated_at

        out["queueStoppedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["queue_stopped_at"]
        )
    return out


def deserialize_json(data: dict) -> GetBudgetResponse:
    out: GetBudgetResponse = {}  # type: ignore[typeddict-item]
    if "budgetId" in data:
        out["budget_id"] = data["budgetId"]
    else:
        raise DeserializationError("GetBudgetResponse.budget_id required")
    if "usageTrackingResource" in data:
        import capo_deadline.types.usage_tracking_resource

        out["usage_tracking_resource"] = (
            capo_deadline.types.usage_tracking_resource.deserialize_json(
                data["usageTrackingResource"]
            )
        )
    else:
        raise DeserializationError("GetBudgetResponse.usage_tracking_resource required")
    if "status" in data:
        import capo_deadline.types.budget_status

        out["status"] = capo_deadline.types.budget_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetBudgetResponse.status required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("GetBudgetResponse.display_name required")
    if "approximateDollarLimit" in data:
        out["approximate_dollar_limit"] = data["approximateDollarLimit"]
    else:
        raise DeserializationError(
            "GetBudgetResponse.approximate_dollar_limit required"
        )
    if "usages" in data:
        import capo_deadline.types.consumed_usages

        out["usages"] = capo_deadline.types.consumed_usages.deserialize_json(
            data["usages"]
        )
    else:
        raise DeserializationError("GetBudgetResponse.usages required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetBudgetResponse.created_by required")
    if "createdAt" in data:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetBudgetResponse.created_at required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "updatedAt" in data:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "actions" in data:
        import capo_deadline.types.response_budget_action_list

        out["actions"] = (
            capo_deadline.types.response_budget_action_list.deserialize_json(
                data["actions"]
            )
        )
    else:
        raise DeserializationError("GetBudgetResponse.actions required")
    if "schedule" in data:
        import capo_deadline.types.budget_schedule

        out["schedule"] = capo_deadline.types.budget_schedule.deserialize_json(
            data["schedule"]
        )
    else:
        raise DeserializationError("GetBudgetResponse.schedule required")
    if "queueStoppedAt" in data:
        import capo_deadline.types.updated_at

        out["queue_stopped_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["queueStoppedAt"]
        )
    return out
