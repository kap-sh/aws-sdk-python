"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateStateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.resource_name
    import aws_sdk_iotfleetwise.types.state_template_data_extra_dimension_node_path_list
    import aws_sdk_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list
    import aws_sdk_iotfleetwise.types.state_template_properties
    import aws_sdk_iotfleetwise.types.tag_list


class CreateStateTemplateRequest(TypedDict, closed=True):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p>The name of the state template.</p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p>A brief description of the state template.</p>"""
    signal_catalog_arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p>The ARN of the signal catalog associated with the state template.</p>"""
    state_template_properties: (
        "aws_sdk_iotfleetwise.types.state_template_properties.StateTemplateProperties"
    )
    """<p>A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.</p>"""
    data_extra_dimensions: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
    ]
    r"""<p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data\"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p>"""
    metadata_extra_dimensions: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
    ]
    r"""<p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data\"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p> <p>Default: An empty array</p>"""
    tags: NotRequired["aws_sdk_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the state template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStateTemplateRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["signalCatalogArn"] = value["signal_catalog_arn"]
    import aws_sdk_iotfleetwise.types.state_template_properties

    out["stateTemplateProperties"] = (
        aws_sdk_iotfleetwise.types.state_template_properties.serialize_aws_json_1_0(
            value["state_template_properties"]
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
    if "tags" in value:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateStateTemplateRequest:
    out: CreateStateTemplateRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "signalCatalogArn" in data:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    else:
        raise DeserializationError(
            "CreateStateTemplateRequest.signal_catalog_arn required"
        )
    if "stateTemplateProperties" in data:
        import aws_sdk_iotfleetwise.types.state_template_properties

        out["state_template_properties"] = (
            aws_sdk_iotfleetwise.types.state_template_properties.deserialize_aws_json_1_0(
                data["stateTemplateProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CreateStateTemplateRequest.state_template_properties required"
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
    if "tags" in data:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
