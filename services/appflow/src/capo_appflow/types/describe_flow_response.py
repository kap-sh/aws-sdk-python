"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.created_by
    import capo_appflow.types.date
    import capo_appflow.types.destination_flow_config_list
    import capo_appflow.types.execution_details
    import capo_appflow.types.flow_arn
    import capo_appflow.types.flow_description
    import capo_appflow.types.flow_name
    import capo_appflow.types.flow_status
    import capo_appflow.types.flow_status_message
    import capo_appflow.types.kms_arn
    import capo_appflow.types.long
    import capo_appflow.types.metadata_catalog_config
    import capo_appflow.types.metadata_catalog_details
    import capo_appflow.types.source_flow_config
    import capo_appflow.types.tag_map
    import capo_appflow.types.tasks
    import capo_appflow.types.trigger_config
    import capo_appflow.types.updated_by


class DescribeFlowResponse(TypedDict, closed=True):
    flow_arn: NotRequired["capo_appflow.types.flow_arn.FlowArn"]
    """<p> The flow's Amazon Resource Name (ARN). </p>"""
    description: NotRequired["capo_appflow.types.flow_description.FlowDescription"]
    """<p> A description of the flow. </p>"""
    flow_name: NotRequired["capo_appflow.types.flow_name.FlowName"]
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""
    kms_arn: NotRequired["capo_appflow.types.kms_arn.KMSArn"]
    """<p> The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key. </p>"""
    flow_status: NotRequired["capo_appflow.types.flow_status.FlowStatus"]
    """<p> Indicates the current status of the flow. </p>"""
    flow_status_message: NotRequired[
        "capo_appflow.types.flow_status_message.FlowStatusMessage"
    ]
    """<p> Contains an error message if the flow status is in a suspended or error state. This applies only to scheduled or event-triggered flows. </p>"""
    source_flow_config: NotRequired[
        "capo_appflow.types.source_flow_config.SourceFlowConfig"
    ]
    """<p> The configuration that controls how Amazon AppFlow retrieves data from the source connector. </p>"""
    destination_flow_config_list: NotRequired[
        "capo_appflow.types.destination_flow_config_list.DestinationFlowConfigList"
    ]
    """<p> The configuration that controls how Amazon AppFlow transfers data to the destination connector. </p>"""
    last_run_execution_details: NotRequired[
        "capo_appflow.types.execution_details.ExecutionDetails"
    ]
    """<p> Describes the details of the most recent flow run. </p>"""
    trigger_config: NotRequired["capo_appflow.types.trigger_config.TriggerConfig"]
    """<p> The trigger settings that determine how and when the flow runs. </p>"""
    tasks: NotRequired["capo_appflow.types.tasks.Tasks"]
    """<p> A list of tasks that Amazon AppFlow performs while transferring the data in the flow run. </p>"""
    created_at: NotRequired["capo_appflow.types.date.Date"]
    """<p> Specifies when the flow was created. </p>"""
    last_updated_at: NotRequired["capo_appflow.types.date.Date"]
    """<p> Specifies when the flow was last updated. </p>"""
    created_by: NotRequired["capo_appflow.types.created_by.CreatedBy"]
    """<p> The ARN of the user who created the flow. </p>"""
    last_updated_by: NotRequired["capo_appflow.types.updated_by.UpdatedBy"]
    """<p> Specifies the user name of the account that performed the most recent update. </p>"""
    tags: NotRequired["capo_appflow.types.tag_map.TagMap"]
    """<p> The tags used to organize, track, or control access for your flow. </p>"""
    metadata_catalog_config: NotRequired[
        "capo_appflow.types.metadata_catalog_config.MetadataCatalogConfig"
    ]
    """<p>Specifies the configuration that Amazon AppFlow uses when it catalogs the data that's transferred by the associated flow. When Amazon AppFlow catalogs the data from a flow, it stores metadata in a data catalog.</p>"""
    last_run_metadata_catalog_details: NotRequired[
        "capo_appflow.types.metadata_catalog_details.MetadataCatalogDetails"
    ]
    """<p>Describes the metadata catalog, metadata table, and data partitions that Amazon AppFlow used for the associated flow run.</p>"""
    schema_version: NotRequired["capo_appflow.types.long.Long"]
    """<p>The version number of your data schema. Amazon AppFlow assigns this version number. The version number increases by one when you change any of the following settings in your flow configuration:</p> <ul> <li> <p>Source-to-destination field mappings</p> </li> <li> <p>Field data types</p> </li> <li> <p>Partition keys</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "flow_name" in value:
        out["flowName"] = value["flow_name"]
    if "kms_arn" in value:
        out["kmsArn"] = value["kms_arn"]
    if "flow_status" in value:
        import capo_appflow.types.flow_status

        out["flowStatus"] = capo_appflow.types.flow_status.serialize_json(
            value["flow_status"]
        )
    if "flow_status_message" in value:
        out["flowStatusMessage"] = value["flow_status_message"]
    if "source_flow_config" in value:
        import capo_appflow.types.source_flow_config

        out["sourceFlowConfig"] = capo_appflow.types.source_flow_config.serialize_json(
            value["source_flow_config"]
        )
    if "destination_flow_config_list" in value:
        import capo_appflow.types.destination_flow_config_list

        out["destinationFlowConfigList"] = (
            capo_appflow.types.destination_flow_config_list.serialize_json(
                value["destination_flow_config_list"]
            )
        )
    if "last_run_execution_details" in value:
        import capo_appflow.types.execution_details

        out["lastRunExecutionDetails"] = (
            capo_appflow.types.execution_details.serialize_json(
                value["last_run_execution_details"]
            )
        )
    if "trigger_config" in value:
        import capo_appflow.types.trigger_config

        out["triggerConfig"] = capo_appflow.types.trigger_config.serialize_json(
            value["trigger_config"]
        )
    if "tasks" in value:
        import capo_appflow.types.tasks

        out["tasks"] = capo_appflow.types.tasks.serialize_json(value["tasks"])
    if "created_at" in value:
        import capo_appflow.types.date

        out["createdAt"] = capo_appflow.types.date.serialize_json(value["created_at"])
    if "last_updated_at" in value:
        import capo_appflow.types.date

        out["lastUpdatedAt"] = capo_appflow.types.date.serialize_json(
            value["last_updated_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "tags" in value:
        import capo_appflow.types.tag_map

        out["tags"] = capo_appflow.types.tag_map.serialize_json(value["tags"])
    if "metadata_catalog_config" in value:
        import capo_appflow.types.metadata_catalog_config

        out["metadataCatalogConfig"] = (
            capo_appflow.types.metadata_catalog_config.serialize_json(
                value["metadata_catalog_config"]
            )
        )
    if "last_run_metadata_catalog_details" in value:
        import capo_appflow.types.metadata_catalog_details

        out["lastRunMetadataCatalogDetails"] = (
            capo_appflow.types.metadata_catalog_details.serialize_json(
                value["last_run_metadata_catalog_details"]
            )
        )
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    return out


def deserialize_json(data: dict) -> DescribeFlowResponse:
    out: DescribeFlowResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    if "kmsArn" in data:
        out["kms_arn"] = data["kmsArn"]
    if "flowStatus" in data:
        import capo_appflow.types.flow_status

        out["flow_status"] = capo_appflow.types.flow_status.deserialize_json(
            data["flowStatus"]
        )
    if "flowStatusMessage" in data:
        out["flow_status_message"] = data["flowStatusMessage"]
    if "sourceFlowConfig" in data:
        import capo_appflow.types.source_flow_config

        out["source_flow_config"] = (
            capo_appflow.types.source_flow_config.deserialize_json(
                data["sourceFlowConfig"]
            )
        )
    if "destinationFlowConfigList" in data:
        import capo_appflow.types.destination_flow_config_list

        out["destination_flow_config_list"] = (
            capo_appflow.types.destination_flow_config_list.deserialize_json(
                data["destinationFlowConfigList"]
            )
        )
    if "lastRunExecutionDetails" in data:
        import capo_appflow.types.execution_details

        out["last_run_execution_details"] = (
            capo_appflow.types.execution_details.deserialize_json(
                data["lastRunExecutionDetails"]
            )
        )
    if "triggerConfig" in data:
        import capo_appflow.types.trigger_config

        out["trigger_config"] = capo_appflow.types.trigger_config.deserialize_json(
            data["triggerConfig"]
        )
    if "tasks" in data:
        import capo_appflow.types.tasks

        out["tasks"] = capo_appflow.types.tasks.deserialize_json(data["tasks"])
    if "createdAt" in data:
        import capo_appflow.types.date

        out["created_at"] = capo_appflow.types.date.deserialize_json(data["createdAt"])
    if "lastUpdatedAt" in data:
        import capo_appflow.types.date

        out["last_updated_at"] = capo_appflow.types.date.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if "tags" in data:
        import capo_appflow.types.tag_map

        out["tags"] = capo_appflow.types.tag_map.deserialize_json(data["tags"])
    if "metadataCatalogConfig" in data:
        import capo_appflow.types.metadata_catalog_config

        out["metadata_catalog_config"] = (
            capo_appflow.types.metadata_catalog_config.deserialize_json(
                data["metadataCatalogConfig"]
            )
        )
    if "lastRunMetadataCatalogDetails" in data:
        import capo_appflow.types.metadata_catalog_details

        out["last_run_metadata_catalog_details"] = (
            capo_appflow.types.metadata_catalog_details.deserialize_json(
                data["lastRunMetadataCatalogDetails"]
            )
        )
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    return out
