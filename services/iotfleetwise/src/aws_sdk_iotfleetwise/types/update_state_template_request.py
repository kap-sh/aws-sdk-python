"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateStateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.resource_identifier
    import aws_sdk_iotfleetwise.types.state_template_data_extra_dimension_node_path_list
    import aws_sdk_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list
    import aws_sdk_iotfleetwise.types.state_template_properties


class UpdateStateTemplateRequest(TypedDict, closed=True):
    identifier: "aws_sdk_iotfleetwise.types.resource_identifier.ResourceIdentifier"
    """<p>The unique ID of the state template.</p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p>A brief description of the state template.</p>"""
    state_template_properties_to_add: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_properties.StateTemplateProperties"
    ]
    """<p>Add signals from which data is collected as part of the state template.</p>"""
    state_template_properties_to_remove: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_properties.StateTemplateProperties"
    ]
    """<p>Remove signals from which data is collected as part of the state template.</p>"""
    data_extra_dimensions: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
    ]
    r"""<p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data\"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p> <p>Default: An empty array</p>"""
    metadata_extra_dimensions: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
    ]
    r"""<p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data\"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateTemplateRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "state_template_properties_to_add" in value:
        import aws_sdk_iotfleetwise.types.state_template_properties

        out["stateTemplatePropertiesToAdd"] = (
            aws_sdk_iotfleetwise.types.state_template_properties.serialize_aws_json_1_0(
                value["state_template_properties_to_add"]
            )
        )
    if "state_template_properties_to_remove" in value:
        import aws_sdk_iotfleetwise.types.state_template_properties

        out["stateTemplatePropertiesToRemove"] = (
            aws_sdk_iotfleetwise.types.state_template_properties.serialize_aws_json_1_0(
                value["state_template_properties_to_remove"]
            )
        )
    if "data_extra_dimensions" in value:
        import aws_sdk_iotfleetwise.types.state_template_data_extra_dimension_node_path_list

        out["dataExtraDimensions"] = (
            aws_sdk_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.serialize_aws_json_1_0(
                value["data_extra_dimensions"]
            )
        )
    if "metadata_extra_dimensions" in value:
        import aws_sdk_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list

        out["metadataExtraDimensions"] = (
            aws_sdk_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.serialize_aws_json_1_0(
                value["metadata_extra_dimensions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateTemplateRequest:
    out: UpdateStateTemplateRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "stateTemplatePropertiesToAdd" in data:
        import aws_sdk_iotfleetwise.types.state_template_properties

        out["state_template_properties_to_add"] = (
            aws_sdk_iotfleetwise.types.state_template_properties.deserialize_aws_json_1_0(
                data["stateTemplatePropertiesToAdd"]
            )
        )
    if "stateTemplatePropertiesToRemove" in data:
        import aws_sdk_iotfleetwise.types.state_template_properties

        out["state_template_properties_to_remove"] = (
            aws_sdk_iotfleetwise.types.state_template_properties.deserialize_aws_json_1_0(
                data["stateTemplatePropertiesToRemove"]
            )
        )
    if "dataExtraDimensions" in data:
        import aws_sdk_iotfleetwise.types.state_template_data_extra_dimension_node_path_list

        out["data_extra_dimensions"] = (
            aws_sdk_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["dataExtraDimensions"]
            )
        )
    if "metadataExtraDimensions" in data:
        import aws_sdk_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list

        out["metadata_extra_dimensions"] = (
            aws_sdk_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["metadataExtraDimensions"]
            )
        )
    return out
