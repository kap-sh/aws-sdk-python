"""Generated from Smithy shape ``com.amazonaws.appflow#UpdateFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.client_token
    import aws_sdk_appflow.types.destination_flow_config_list
    import aws_sdk_appflow.types.flow_description
    import aws_sdk_appflow.types.flow_name
    import aws_sdk_appflow.types.metadata_catalog_config
    import aws_sdk_appflow.types.source_flow_config
    import aws_sdk_appflow.types.tasks
    import aws_sdk_appflow.types.trigger_config


class UpdateFlowRequest(TypedDict):
    flow_name: "aws_sdk_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""
    description: NotRequired["aws_sdk_appflow.types.flow_description.FlowDescription"]
    """<p> A description of the flow. </p>"""
    trigger_config: "aws_sdk_appflow.types.trigger_config.TriggerConfig"
    """<p> The trigger settings that determine how and when the flow runs. </p>"""
    source_flow_config: "aws_sdk_appflow.types.source_flow_config.SourceFlowConfig"
    destination_flow_config_list: (
        "aws_sdk_appflow.types.destination_flow_config_list.DestinationFlowConfigList"
    )
    """<p> The configuration that controls how Amazon AppFlow transfers data to the destination connector. </p>"""
    tasks: "aws_sdk_appflow.types.tasks.Tasks"
    """<p> A list of tasks that Amazon AppFlow performs while transferring the data in the flow run. </p>"""
    metadata_catalog_config: NotRequired[
        "aws_sdk_appflow.types.metadata_catalog_config.MetadataCatalogConfig"
    ]
    """<p>Specifies the configuration that Amazon AppFlow uses when it catalogs the data that's transferred by the associated flow. When Amazon AppFlow catalogs the data from a flow, it stores metadata in a data catalog.</p>"""
    client_token: NotRequired["aws_sdk_appflow.types.client_token.ClientToken"]
    """<p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>UpdateFlow</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>UpdateFlow</code>. The token is active for 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_appflow.types.trigger_config

    out["triggerConfig"] = aws_sdk_appflow.types.trigger_config.serialize_json(
        value["trigger_config"]
    )
    import aws_sdk_appflow.types.source_flow_config

    out["sourceFlowConfig"] = aws_sdk_appflow.types.source_flow_config.serialize_json(
        value["source_flow_config"]
    )
    import aws_sdk_appflow.types.destination_flow_config_list

    out["destinationFlowConfigList"] = (
        aws_sdk_appflow.types.destination_flow_config_list.serialize_json(
            value["destination_flow_config_list"]
        )
    )
    import aws_sdk_appflow.types.tasks

    out["tasks"] = aws_sdk_appflow.types.tasks.serialize_json(value["tasks"])
    if "metadata_catalog_config" in value:
        import aws_sdk_appflow.types.metadata_catalog_config

        out["metadataCatalogConfig"] = (
            aws_sdk_appflow.types.metadata_catalog_config.serialize_json(
                value["metadata_catalog_config"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateFlowRequest:
    out: UpdateFlowRequest = {}  # type: ignore[typeddict-item]
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError("UpdateFlowRequest.flow_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "triggerConfig" in data:
        import aws_sdk_appflow.types.trigger_config

        out["trigger_config"] = aws_sdk_appflow.types.trigger_config.deserialize_json(
            data["triggerConfig"]
        )
    else:
        raise DeserializationError("UpdateFlowRequest.trigger_config required")
    if "sourceFlowConfig" in data:
        import aws_sdk_appflow.types.source_flow_config

        out["source_flow_config"] = (
            aws_sdk_appflow.types.source_flow_config.deserialize_json(
                data["sourceFlowConfig"]
            )
        )
    else:
        raise DeserializationError("UpdateFlowRequest.source_flow_config required")
    if "destinationFlowConfigList" in data:
        import aws_sdk_appflow.types.destination_flow_config_list

        out["destination_flow_config_list"] = (
            aws_sdk_appflow.types.destination_flow_config_list.deserialize_json(
                data["destinationFlowConfigList"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateFlowRequest.destination_flow_config_list required"
        )
    if "tasks" in data:
        import aws_sdk_appflow.types.tasks

        out["tasks"] = aws_sdk_appflow.types.tasks.deserialize_json(data["tasks"])
    else:
        raise DeserializationError("UpdateFlowRequest.tasks required")
    if "metadataCatalogConfig" in data:
        import aws_sdk_appflow.types.metadata_catalog_config

        out["metadata_catalog_config"] = (
            aws_sdk_appflow.types.metadata_catalog_config.deserialize_json(
                data["metadataCatalogConfig"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
