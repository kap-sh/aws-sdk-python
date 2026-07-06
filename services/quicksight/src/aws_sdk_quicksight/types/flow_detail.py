"""Generated from Smithy shape ``com.amazonaws.quicksight#FlowDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.flow_description
    import aws_sdk_quicksight.types.flow_id
    import aws_sdk_quicksight.types.flow_publish_state
    import aws_sdk_quicksight.types.sensitive_document
    import aws_sdk_quicksight.types.step_alias_list
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.title


class FlowDetail(TypedDict, closed=True):
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
    publish_state: "aws_sdk_quicksight.types.flow_publish_state.FlowPublishState"
    """<p>The publish state of the flow. Valid values are <code>DRAFT</code>, <code>PUBLISHED</code>, or <code>PENDING_APPROVAL</code>.</p>"""
    created_time: "aws_sdk_quicksight.types.timestamp.Timestamp"
    """<p>The time this flow was created.</p>"""
    created_by: NotRequired["str"]
    """<p>The identifier of the principal who created the flow.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time this flow was modified.</p>"""
    last_updated_by: NotRequired["str"]
    """<p>The identifier of the last principal who updated the flow.</p>"""
    flow_definition: "aws_sdk_quicksight.types.sensitive_document.SensitiveDocument"
    """<p>The definition of the flow, specifying the steps and configurations. This is the flow definition in Quick Flow's internal format. The format is subject to change.</p>"""
    step_aliases: NotRequired["aws_sdk_quicksight.types.step_alias_list.StepAliasList"]
    """<p>A list of step alias mappings for the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowDetail) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FlowId"] = value["flow_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_quicksight.types.flow_publish_state

    out["PublishState"] = aws_sdk_quicksight.types.flow_publish_state.serialize_json(
        value["publish_state"]
    )
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
    out["FlowDefinition"] = value["flow_definition"]
    if "step_aliases" in value:
        import aws_sdk_quicksight.types.step_alias_list

        out["StepAliases"] = aws_sdk_quicksight.types.step_alias_list.serialize_json(
            value["step_aliases"]
        )
    return out


def deserialize_json(data: dict) -> FlowDetail:
    out: FlowDetail = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("FlowDetail.arn required")
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    else:
        raise DeserializationError("FlowDetail.flow_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("FlowDetail.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "PublishState" in data:
        import aws_sdk_quicksight.types.flow_publish_state

        out["publish_state"] = (
            aws_sdk_quicksight.types.flow_publish_state.deserialize_json(
                data["PublishState"]
            )
        )
    else:
        raise DeserializationError("FlowDetail.publish_state required")
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("FlowDetail.created_time required")
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "LastUpdatedBy" in data:
        out["last_updated_by"] = data["LastUpdatedBy"]
    if "FlowDefinition" in data:
        out["flow_definition"] = data["FlowDefinition"]
    else:
        raise DeserializationError("FlowDetail.flow_definition required")
    if "StepAliases" in data:
        import aws_sdk_quicksight.types.step_alias_list

        out["step_aliases"] = aws_sdk_quicksight.types.step_alias_list.deserialize_json(
            data["StepAliases"]
        )
    return out
