"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateVehicleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.attributes_map
    import aws_sdk_iotfleetwise.types.state_template_associations
    import aws_sdk_iotfleetwise.types.tag_list
    import aws_sdk_iotfleetwise.types.vehicle_association_behavior
    import aws_sdk_iotfleetwise.types.vehicle_name


class CreateVehicleRequest(TypedDict):
    vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"
    """<p> The unique ID of the vehicle to create. </p>"""
    model_manifest_arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name ARN of a vehicle model. </p>"""
    decoder_manifest_arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The ARN of a decoder manifest. </p>"""
    attributes: NotRequired["aws_sdk_iotfleetwise.types.attributes_map.attributesMap"]
    """<p>Static information about a vehicle in a key-value pair. For example: <code>\"engineType\"</code> : <code>\"1.3 L R2\"</code> </p> <p>To use attributes with Campaigns or State Templates, you must include them using the request parameters <code>dataExtraDimensions</code> and/or <code>metadataExtraDimensions</code> (for state templates only) when creating your campaign/state template. </p>"""
    association_behavior: NotRequired[
        "aws_sdk_iotfleetwise.types.vehicle_association_behavior.VehicleAssociationBehavior"
    ]
    """<p> An option to create a new Amazon Web Services IoT thing when creating a vehicle, or to validate an existing Amazon Web Services IoT thing as a vehicle. </p> <p>Default: <code/> </p>"""
    tags: NotRequired["aws_sdk_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the vehicle.</p>"""
    state_templates: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
    ]
    """<p>Associate state templates with the vehicle. You can monitor the last known state of the vehicle in near real time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVehicleRequest) -> dict:
    out: dict = {}
    out["modelManifestArn"] = value["model_manifest_arn"]
    out["decoderManifestArn"] = value["decoder_manifest_arn"]
    if "attributes" in value:
        import aws_sdk_iotfleetwise.types.attributes_map

        out["attributes"] = (
            aws_sdk_iotfleetwise.types.attributes_map.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    if "association_behavior" in value:
        import aws_sdk_iotfleetwise.types.vehicle_association_behavior

        out["associationBehavior"] = (
            aws_sdk_iotfleetwise.types.vehicle_association_behavior.serialize_aws_json_1_0(
                value["association_behavior"]
            )
        )
    if "tags" in value:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "state_templates" in value:
        import aws_sdk_iotfleetwise.types.state_template_associations

        out["stateTemplates"] = (
            aws_sdk_iotfleetwise.types.state_template_associations.serialize_aws_json_1_0(
                value["state_templates"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVehicleRequest:
    out: CreateVehicleRequest = {}  # type: ignore[typeddict-item]
    if "modelManifestArn" in data:
        out["model_manifest_arn"] = data["modelManifestArn"]
    else:
        raise DeserializationError("CreateVehicleRequest.model_manifest_arn required")
    if "decoderManifestArn" in data:
        out["decoder_manifest_arn"] = data["decoderManifestArn"]
    else:
        raise DeserializationError("CreateVehicleRequest.decoder_manifest_arn required")
    if "attributes" in data:
        import aws_sdk_iotfleetwise.types.attributes_map

        out["attributes"] = (
            aws_sdk_iotfleetwise.types.attributes_map.deserialize_aws_json_1_0(
                data["attributes"]
            )
        )
    if "associationBehavior" in data:
        import aws_sdk_iotfleetwise.types.vehicle_association_behavior

        out["association_behavior"] = (
            aws_sdk_iotfleetwise.types.vehicle_association_behavior.deserialize_aws_json_1_0(
                data["associationBehavior"]
            )
        )
    if "tags" in data:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "stateTemplates" in data:
        import aws_sdk_iotfleetwise.types.state_template_associations

        out["state_templates"] = (
            aws_sdk_iotfleetwise.types.state_template_associations.deserialize_aws_json_1_0(
                data["stateTemplates"]
            )
        )
    return out
