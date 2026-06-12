"""Generated from Smithy shape ``com.amazonaws.appflow#FlowDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_label
    import aws_sdk_appflow.types.connector_type
    import aws_sdk_appflow.types.created_by
    import aws_sdk_appflow.types.date
    import aws_sdk_appflow.types.execution_details
    import aws_sdk_appflow.types.flow_arn
    import aws_sdk_appflow.types.flow_description
    import aws_sdk_appflow.types.flow_name
    import aws_sdk_appflow.types.flow_status
    import aws_sdk_appflow.types.tag_map
    import aws_sdk_appflow.types.trigger_type
    import aws_sdk_appflow.types.updated_by


class FlowDefinition(TypedDict):
    flow_arn: NotRequired["aws_sdk_appflow.types.flow_arn.FlowArn"]
    """<p> The flow's Amazon Resource Name (ARN). </p>"""
    description: NotRequired["aws_sdk_appflow.types.flow_description.FlowDescription"]
    """<p> A user-entered description of the flow. </p>"""
    flow_name: NotRequired["aws_sdk_appflow.types.flow_name.FlowName"]
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""
    flow_status: NotRequired["aws_sdk_appflow.types.flow_status.FlowStatus"]
    """<p> Indicates the current status of the flow. </p>"""
    source_connector_type: NotRequired[
        "aws_sdk_appflow.types.connector_type.ConnectorType"
    ]
    """<p> Specifies the source connector type, such as Salesforce, Amazon S3, Amplitude, and so on. </p>"""
    source_connector_label: NotRequired[
        "aws_sdk_appflow.types.connector_label.ConnectorLabel"
    ]
    """<p>The label of the source connector in the flow.</p>"""
    destination_connector_type: NotRequired[
        "aws_sdk_appflow.types.connector_type.ConnectorType"
    ]
    """<p> Specifies the destination connector type, such as Salesforce, Amazon S3, Amplitude, and so on. </p>"""
    destination_connector_label: NotRequired[
        "aws_sdk_appflow.types.connector_label.ConnectorLabel"
    ]
    """<p>The label of the destination connector in the flow.</p>"""
    trigger_type: NotRequired["aws_sdk_appflow.types.trigger_type.TriggerType"]
    """<p> Specifies the type of flow trigger. This can be <code>OnDemand</code>, <code>Scheduled</code>, or <code>Event</code>. </p>"""
    created_at: NotRequired["aws_sdk_appflow.types.date.Date"]
    """<p> Specifies when the flow was created. </p>"""
    last_updated_at: NotRequired["aws_sdk_appflow.types.date.Date"]
    """<p> Specifies when the flow was last updated. </p>"""
    created_by: NotRequired["aws_sdk_appflow.types.created_by.CreatedBy"]
    """<p> The ARN of the user who created the flow. </p>"""
    last_updated_by: NotRequired["aws_sdk_appflow.types.updated_by.UpdatedBy"]
    """<p> Specifies the account user name that most recently updated the flow. </p>"""
    tags: NotRequired["aws_sdk_appflow.types.tag_map.TagMap"]
    """<p> The tags used to organize, track, or control access for your flow. </p>"""
    last_run_execution_details: NotRequired[
        "aws_sdk_appflow.types.execution_details.ExecutionDetails"
    ]
    """<p> Describes the details of the most recent flow run. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowDefinition) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "flow_name" in value:
        out["flowName"] = value["flow_name"]
    if "flow_status" in value:
        import aws_sdk_appflow.types.flow_status

        out["flowStatus"] = aws_sdk_appflow.types.flow_status.serialize_json(
            value["flow_status"]
        )
    if "source_connector_type" in value:
        import aws_sdk_appflow.types.connector_type

        out["sourceConnectorType"] = (
            aws_sdk_appflow.types.connector_type.serialize_json(
                value["source_connector_type"]
            )
        )
    if "source_connector_label" in value:
        out["sourceConnectorLabel"] = value["source_connector_label"]
    if "destination_connector_type" in value:
        import aws_sdk_appflow.types.connector_type

        out["destinationConnectorType"] = (
            aws_sdk_appflow.types.connector_type.serialize_json(
                value["destination_connector_type"]
            )
        )
    if "destination_connector_label" in value:
        out["destinationConnectorLabel"] = value["destination_connector_label"]
    if "trigger_type" in value:
        import aws_sdk_appflow.types.trigger_type

        out["triggerType"] = aws_sdk_appflow.types.trigger_type.serialize_json(
            value["trigger_type"]
        )
    if "created_at" in value:
        import aws_sdk_appflow.types.date

        out["createdAt"] = aws_sdk_appflow.types.date.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_appflow.types.date

        out["lastUpdatedAt"] = aws_sdk_appflow.types.date.serialize_json(
            value["last_updated_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "tags" in value:
        import aws_sdk_appflow.types.tag_map

        out["tags"] = aws_sdk_appflow.types.tag_map.serialize_json(value["tags"])
    if "last_run_execution_details" in value:
        import aws_sdk_appflow.types.execution_details

        out["lastRunExecutionDetails"] = (
            aws_sdk_appflow.types.execution_details.serialize_json(
                value["last_run_execution_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowDefinition:
    out: FlowDefinition = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    if "flowStatus" in data:
        import aws_sdk_appflow.types.flow_status

        out["flow_status"] = aws_sdk_appflow.types.flow_status.deserialize_json(
            data["flowStatus"]
        )
    if "sourceConnectorType" in data:
        import aws_sdk_appflow.types.connector_type

        out["source_connector_type"] = (
            aws_sdk_appflow.types.connector_type.deserialize_json(
                data["sourceConnectorType"]
            )
        )
    if "sourceConnectorLabel" in data:
        out["source_connector_label"] = data["sourceConnectorLabel"]
    if "destinationConnectorType" in data:
        import aws_sdk_appflow.types.connector_type

        out["destination_connector_type"] = (
            aws_sdk_appflow.types.connector_type.deserialize_json(
                data["destinationConnectorType"]
            )
        )
    if "destinationConnectorLabel" in data:
        out["destination_connector_label"] = data["destinationConnectorLabel"]
    if "triggerType" in data:
        import aws_sdk_appflow.types.trigger_type

        out["trigger_type"] = aws_sdk_appflow.types.trigger_type.deserialize_json(
            data["triggerType"]
        )
    if "createdAt" in data:
        import aws_sdk_appflow.types.date

        out["created_at"] = aws_sdk_appflow.types.date.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_appflow.types.date

        out["last_updated_at"] = aws_sdk_appflow.types.date.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if "tags" in data:
        import aws_sdk_appflow.types.tag_map

        out["tags"] = aws_sdk_appflow.types.tag_map.deserialize_json(data["tags"])
    if "lastRunExecutionDetails" in data:
        import aws_sdk_appflow.types.execution_details

        out["last_run_execution_details"] = (
            aws_sdk_appflow.types.execution_details.deserialize_json(
                data["lastRunExecutionDetails"]
            )
        )
    return out
