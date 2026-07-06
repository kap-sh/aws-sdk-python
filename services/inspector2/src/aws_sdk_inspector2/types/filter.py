"""Generated from Smithy shape ``com.amazonaws.inspector2#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.date_time_timestamp
    import aws_sdk_inspector2.types.filter_action
    import aws_sdk_inspector2.types.filter_arn
    import aws_sdk_inspector2.types.filter_criteria
    import aws_sdk_inspector2.types.filter_description
    import aws_sdk_inspector2.types.filter_name
    import aws_sdk_inspector2.types.filter_reason
    import aws_sdk_inspector2.types.owner_id
    import aws_sdk_inspector2.types.tag_map


class Filter(TypedDict, closed=True):
    arn: "aws_sdk_inspector2.types.filter_arn.FilterArn"
    """<p>The Amazon Resource Number (ARN) associated with this filter.</p>"""
    owner_id: "aws_sdk_inspector2.types.owner_id.OwnerId"
    """<p>The Amazon Web Services account ID of the account that created the filter.</p>"""
    name: "aws_sdk_inspector2.types.filter_name.FilterName"
    """<p>The name of the filter.</p>"""
    criteria: "aws_sdk_inspector2.types.filter_criteria.FilterCriteria"
    """<p>Details on the filter criteria associated with this filter.</p>"""
    action: "aws_sdk_inspector2.types.filter_action.FilterAction"
    """<p>The action that is to be applied to the findings that match the filter.</p>"""
    created_at: "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    """<p>The date and time this filter was created at.</p>"""
    updated_at: "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    """<p>The date and time the filter was last updated at.</p>"""
    description: NotRequired[
        "aws_sdk_inspector2.types.filter_description.FilterDescription"
    ]
    """<p>A description of the filter.</p>"""
    reason: NotRequired["aws_sdk_inspector2.types.filter_reason.FilterReason"]
    """<p>The reason for the filter.</p>"""
    tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>The tags attached to the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["ownerId"] = value["owner_id"]
    out["name"] = value["name"]
    import aws_sdk_inspector2.types.filter_criteria

    out["criteria"] = aws_sdk_inspector2.types.filter_criteria.serialize_json(
        value["criteria"]
    )
    out["action"] = value["action"]
    import aws_sdk_inspector2.types.date_time_timestamp

    out["createdAt"] = aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_inspector2.types.date_time_timestamp

    out["updatedAt"] = aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
        value["updated_at"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "tags" in value:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Filter.arn required")
    if "ownerId" in data:
        out["owner_id"] = data["ownerId"]
    else:
        raise DeserializationError("Filter.owner_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Filter.name required")
    if "criteria" in data:
        import aws_sdk_inspector2.types.filter_criteria

        out["criteria"] = aws_sdk_inspector2.types.filter_criteria.deserialize_json(
            data["criteria"]
        )
    else:
        raise DeserializationError("Filter.criteria required")
    if "action" in data:
        out["action"] = data["action"]
    else:
        raise DeserializationError("Filter.action required")
    if "createdAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["created_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Filter.created_at required")
    if "updatedAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["updated_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Filter.updated_at required")
    if "description" in data:
        out["description"] = data["description"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "tags" in data:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.deserialize_json(data["tags"])
    return out
