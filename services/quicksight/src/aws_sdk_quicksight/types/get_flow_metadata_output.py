"""Generated from Smithy shape ``com.amazonaws.quicksight#GetFlowMetadataOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.flow_description
    import aws_sdk_quicksight.types.flow_id
    import aws_sdk_quicksight.types.flow_publish_state
    import aws_sdk_quicksight.types.integer
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.title


class GetFlowMetadataOutput(TypedDict):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    flow_id: "aws_sdk_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    name: "aws_sdk_quicksight.types.title.Title"
    """<p>A display name for the flow.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.flow_description.FlowDescription"
    ]
    """<p>The description for the flow.</p>"""
    publish_state: NotRequired[
        "aws_sdk_quicksight.types.flow_publish_state.FlowPublishState"
    ]
    """<p>The publish state for the flow. Valid values are <code>DRAFT</code>, <code>PUBLISHED</code>, or <code>PENDING_APPROVAL</code>.</p>"""
    user_count: "aws_sdk_quicksight.types.integer.Integer"
    """<p>The number of users who have used the flow.</p>"""
    run_count: "aws_sdk_quicksight.types.integer.Integer"
    """<p>The number of runs done for the flow.</p>"""
    created_time: "aws_sdk_quicksight.types.timestamp.Timestamp"
    """<p>The time this flow was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time this flow was modified.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowMetadataOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FlowId"] = value["flow_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "publish_state" in value:
        import aws_sdk_quicksight.types.flow_publish_state

        out["PublishState"] = (
            aws_sdk_quicksight.types.flow_publish_state.serialize_json(
                value["publish_state"]
            )
        )
    out["UserCount"] = value.get("user_count", 0)
    out["RunCount"] = value.get("run_count", 0)
    import aws_sdk_quicksight.types.timestamp

    out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
        value["created_time"]
    )
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> GetFlowMetadataOutput:
    out: GetFlowMetadataOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetFlowMetadataOutput.arn required")
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    else:
        raise DeserializationError("GetFlowMetadataOutput.flow_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetFlowMetadataOutput.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "PublishState" in data:
        import aws_sdk_quicksight.types.flow_publish_state

        out["publish_state"] = (
            aws_sdk_quicksight.types.flow_publish_state.deserialize_json(
                data["PublishState"]
            )
        )
    if "UserCount" in data:
        out["user_count"] = data["UserCount"]
    else:
        out["user_count"] = 0
    if "RunCount" in data:
        out["run_count"] = data["RunCount"]
    else:
        out["run_count"] = 0
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("GetFlowMetadataOutput.created_time required")
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
