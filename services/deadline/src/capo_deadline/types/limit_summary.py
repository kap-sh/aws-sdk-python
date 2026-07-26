"""Generated from Smithy shape ``com.amazonaws.deadline#LimitSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.amount_requirement_name
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.farm_id
    import capo_deadline.types.limit_id
    import capo_deadline.types.max_count
    import capo_deadline.types.min_zero_max_integer
    import capo_deadline.types.resource_name
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class LimitSummary(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the limit.</p>"""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit.</p>"""
    current_count: "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    """<p>The number of resources from the limit that are being used by jobs. The result is delayed and may not be the count at the time that you called the operation.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The Unix timestamp of the date and time that the limit was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user identifier of the person that created the limit.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The Unix timestamp of the date and time that the limit was last updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user identifier of the person that last updated the limit.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The name of the limit used in lists to identify the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    amount_requirement_name: (
        "capo_deadline.types.amount_requirement_name.AmountRequirementName"
    )
    """<p>The value that you specify as the <code>name</code> in the <code>amounts</code> field of the <code>hostRequirements</code> in a step of a job template to declare the limit requirement.</p>"""
    max_count: "capo_deadline.types.max_count.MaxCount"
    """<p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>The <code>maxValue</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitSummary) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["limitId"] = value["limit_id"]
    out["currentCount"] = value["current_count"]
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["displayName"] = value["display_name"]
    out["amountRequirementName"] = value["amount_requirement_name"]
    out["maxCount"] = value["max_count"]
    return out


def deserialize_json(data: dict) -> LimitSummary:
    out: LimitSummary = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("LimitSummary.farm_id required")
    if "limitId" in data:
        out["limit_id"] = data["limitId"]
    else:
        raise DeserializationError("LimitSummary.limit_id required")
    if "currentCount" in data:
        out["current_count"] = data["currentCount"]
    else:
        raise DeserializationError("LimitSummary.current_count required")
    if "createdAt" in data:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("LimitSummary.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("LimitSummary.created_by required")
    if "updatedAt" in data:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("LimitSummary.display_name required")
    if "amountRequirementName" in data:
        out["amount_requirement_name"] = data["amountRequirementName"]
    else:
        raise DeserializationError("LimitSummary.amount_requirement_name required")
    if "maxCount" in data:
        out["max_count"] = data["maxCount"]
    else:
        raise DeserializationError("LimitSummary.max_count required")
    return out
