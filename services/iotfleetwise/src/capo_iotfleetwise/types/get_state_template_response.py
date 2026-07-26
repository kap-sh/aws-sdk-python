"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetStateTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.resource_unique_id
    import capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_properties
    import capo_iotfleetwise.types.timestamp


class GetStateTemplateResponse(TypedDict, closed=True):
    name: NotRequired["capo_iotfleetwise.types.resource_name.resourceName"]
    """<p>The name of the state template.</p>"""
    arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The Amazon Resource Name (ARN) of the state template.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the state template.</p>"""
    signal_catalog_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The ARN of the signal catalog associated with the state template.</p>"""
    state_template_properties: NotRequired[
        "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
    ]
    """<p>A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.</p>"""
    data_extra_dimensions: NotRequired[
        "capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
    ]
    """<p>A list of vehicle attributes associated with the payload published on the state template's MQTT topic. </p> <p>Default: An empty array</p>"""
    metadata_extra_dimensions: NotRequired[
        "capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
    ]
    """<p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic.</p> <p>Default: An empty array</p>"""
    creation_time: NotRequired["capo_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time the state template was created in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: NotRequired["capo_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time the state template was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    id: NotRequired["capo_iotfleetwise.types.resource_unique_id.ResourceUniqueId"]
    """<p>The unique ID of the state template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetStateTemplateResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "signal_catalog_arn" in value:
        out["signalCatalogArn"] = value["signal_catalog_arn"]
    if "state_template_properties" in value:
        import capo_iotfleetwise.types.state_template_properties

        out["stateTemplateProperties"] = (
            capo_iotfleetwise.types.state_template_properties.serialize_aws_json_1_0(
                value["state_template_properties"]
            )
        )
    if "data_extra_dimensions" in value:
        import capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list

        out["dataExtraDimensions"] = (
            capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.serialize_aws_json_1_0(
                value["data_extra_dimensions"]
            )
        )
    if "metadata_extra_dimensions" in value:
        import capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list

        out["metadataExtraDimensions"] = (
            capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.serialize_aws_json_1_0(
                value["metadata_extra_dimensions"]
            )
        )
    if "creation_time" in value:
        import capo_iotfleetwise.types.timestamp

        out["creationTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import capo_iotfleetwise.types.timestamp

        out["lastModificationTime"] = (
            capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["last_modification_time"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetStateTemplateResponse:
    out: GetStateTemplateResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "description" in data:
        out["description"] = data["description"]
    if "signalCatalogArn" in data:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    if "stateTemplateProperties" in data:
        import capo_iotfleetwise.types.state_template_properties

        out["state_template_properties"] = (
            capo_iotfleetwise.types.state_template_properties.deserialize_aws_json_1_0(
                data["stateTemplateProperties"]
            )
        )
    if "dataExtraDimensions" in data:
        import capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list

        out["data_extra_dimensions"] = (
            capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["dataExtraDimensions"]
            )
        )
    if "metadataExtraDimensions" in data:
        import capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list

        out["metadata_extra_dimensions"] = (
            capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["metadataExtraDimensions"]
            )
        )
    if "creationTime" in data:
        import capo_iotfleetwise.types.timestamp

        out["creation_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    if "lastModificationTime" in data:
        import capo_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    return out
