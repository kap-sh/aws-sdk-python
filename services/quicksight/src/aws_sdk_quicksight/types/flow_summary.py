"""Generated from Smithy shape ``com.amazonaws.quicksight#FlowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.flow_description
    import aws_sdk_quicksight.types.flow_id
    import aws_sdk_quicksight.types.flow_publish_state
    import aws_sdk_quicksight.types.integer
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.title


class FlowSummary(TypedDict, closed=True):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    flow_id: "aws_sdk_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    name: "aws_sdk_quicksight.types.title.Title"
    """<p>The display name of the flow.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.flow_description.FlowDescription"
    ]
    """<p>The description of the flow.</p>"""
    created_time: "aws_sdk_quicksight.types.timestamp.Timestamp"
    """<p>The time this flow was created.</p>"""
    created_by: NotRequired["str"]
    """<p>The identifier of the principal who created the flow.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time this flow was modified.</p>"""
    last_updated_by: NotRequired["str"]
    """<p>The identifier of the last principal who updated the flow.</p>"""
    publish_state: NotRequired[
        "aws_sdk_quicksight.types.flow_publish_state.FlowPublishState"
    ]
    """<p>The publish state for the flow. The valid values are <code>DRAFT</code>, <code>PUBLISHED</code>, or <code>PENDING_APPROVAL</code>.</p>"""
    run_count: "aws_sdk_quicksight.types.integer.Integer"
    """<p>The number of runs done for the flow.</p>"""
    user_count: "aws_sdk_quicksight.types.integer.Integer"
    """<p>The number of users who have used the flow.</p>"""
    last_published_by: NotRequired["str"]
    """<p>The identifier of the last principal who published the flow.</p>"""
    last_published_at: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time this flow was published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FlowId"] = value["flow_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_quicksight.types.timestamp

    out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
        value["created_time"]
    )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "last_updated_by" in value:
        out["LastUpdatedBy"] = value["last_updated_by"]
    if "publish_state" in value:
        import aws_sdk_quicksight.types.flow_publish_state

        out["PublishState"] = (
            aws_sdk_quicksight.types.flow_publish_state.serialize_json(
                value["publish_state"]
            )
        )
    out["RunCount"] = value.get("run_count", 0)
    out["UserCount"] = value.get("user_count", 0)
    if "last_published_by" in value:
        out["LastPublishedBy"] = value["last_published_by"]
    if "last_published_at" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastPublishedAt"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_published_at"]
        )
    return out


def deserialize_json(data: dict) -> FlowSummary:
    out: FlowSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("FlowSummary.arn required")
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    else:
        raise DeserializationError("FlowSummary.flow_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("FlowSummary.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("FlowSummary.created_time required")
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "LastUpdatedBy" in data:
        out["last_updated_by"] = data["LastUpdatedBy"]
    if "PublishState" in data:
        import aws_sdk_quicksight.types.flow_publish_state

        out["publish_state"] = (
            aws_sdk_quicksight.types.flow_publish_state.deserialize_json(
                data["PublishState"]
            )
        )
    if "RunCount" in data:
        out["run_count"] = data["RunCount"]
    else:
        out["run_count"] = 0
    if "UserCount" in data:
        out["user_count"] = data["UserCount"]
    else:
        out["user_count"] = 0
    if "LastPublishedBy" in data:
        out["last_published_by"] = data["LastPublishedBy"]
    if "LastPublishedAt" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_published_at"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastPublishedAt"]
        )
    return out
