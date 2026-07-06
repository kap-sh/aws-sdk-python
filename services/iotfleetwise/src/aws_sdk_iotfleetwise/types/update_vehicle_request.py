"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateVehicleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.attributes_map
    import aws_sdk_iotfleetwise.types.state_template_association_identifiers
    import aws_sdk_iotfleetwise.types.state_template_associations
    import aws_sdk_iotfleetwise.types.update_mode
    import aws_sdk_iotfleetwise.types.vehicle_name


class UpdateVehicleRequest(TypedDict, closed=True):
    vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"
    """<p>The unique ID of the vehicle to update.</p>"""
    model_manifest_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p>The ARN of a vehicle model (model manifest) associated with the vehicle.</p>"""
    decoder_manifest_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p>The ARN of the decoder manifest associated with this vehicle.</p>"""
    attributes: NotRequired["aws_sdk_iotfleetwise.types.attributes_map.attributesMap"]
    r"""<p>Static information about a vehicle in a key-value pair. For example:</p> <p> <code>\"engineType\"</code> : <code>\"1.3 L R2\"</code> </p>"""
    attribute_update_mode: NotRequired[
        "aws_sdk_iotfleetwise.types.update_mode.UpdateMode"
    ]
    """<p>The method the specified attributes will update the existing attributes on the vehicle. Use<code>Overwite</code> to replace the vehicle attributes with the specified attributes. Or use <code>Merge</code> to combine all attributes.</p> <p>This is required if attributes are present in the input.</p>"""
    state_templates_to_add: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
    ]
    """<p>Associate state templates with the vehicle.</p>"""
    state_templates_to_remove: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_association_identifiers.StateTemplateAssociationIdentifiers"
    ]
    """<p>Remove state templates from the vehicle.</p>"""
    state_templates_to_update: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
    ]
    """<p>Change the <code>stateTemplateUpdateStrategy</code> of state templates already associated with the vehicle.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVehicleRequest) -> dict:
    out: dict = {}
    if "model_manifest_arn" in value:
        out["modelManifestArn"] = value["model_manifest_arn"]
    if "decoder_manifest_arn" in value:
        out["decoderManifestArn"] = value["decoder_manifest_arn"]
    if "attributes" in value:
        import aws_sdk_iotfleetwise.types.attributes_map

        out["attributes"] = (
            aws_sdk_iotfleetwise.types.attributes_map.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    if "attribute_update_mode" in value:
        import aws_sdk_iotfleetwise.types.update_mode

        out["attributeUpdateMode"] = (
            aws_sdk_iotfleetwise.types.update_mode.serialize_aws_json_1_0(
                value["attribute_update_mode"]
            )
        )
    if "state_templates_to_add" in value:
        import aws_sdk_iotfleetwise.types.state_template_associations

        out["stateTemplatesToAdd"] = (
            aws_sdk_iotfleetwise.types.state_template_associations.serialize_aws_json_1_0(
                value["state_templates_to_add"]
            )
        )
    if "state_templates_to_remove" in value:
        import aws_sdk_iotfleetwise.types.state_template_association_identifiers

        out["stateTemplatesToRemove"] = (
            aws_sdk_iotfleetwise.types.state_template_association_identifiers.serialize_aws_json_1_0(
                value["state_templates_to_remove"]
            )
        )
    if "state_templates_to_update" in value:
        import aws_sdk_iotfleetwise.types.state_template_associations

        out["stateTemplatesToUpdate"] = (
            aws_sdk_iotfleetwise.types.state_template_associations.serialize_aws_json_1_0(
                value["state_templates_to_update"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVehicleRequest:
    out: UpdateVehicleRequest = {}  # type: ignore[typeddict-item]
    if "modelManifestArn" in data:
        out["model_manifest_arn"] = data["modelManifestArn"]
    if "decoderManifestArn" in data:
        out["decoder_manifest_arn"] = data["decoderManifestArn"]
    if "attributes" in data:
        import aws_sdk_iotfleetwise.types.attributes_map

        out["attributes"] = (
            aws_sdk_iotfleetwise.types.attributes_map.deserialize_aws_json_1_0(
                data["attributes"]
            )
        )
    if "attributeUpdateMode" in data:
        import aws_sdk_iotfleetwise.types.update_mode

        out["attribute_update_mode"] = (
            aws_sdk_iotfleetwise.types.update_mode.deserialize_aws_json_1_0(
                data["attributeUpdateMode"]
            )
        )
    if "stateTemplatesToAdd" in data:
        import aws_sdk_iotfleetwise.types.state_template_associations

        out["state_templates_to_add"] = (
            aws_sdk_iotfleetwise.types.state_template_associations.deserialize_aws_json_1_0(
                data["stateTemplatesToAdd"]
            )
        )
    if "stateTemplatesToRemove" in data:
        import aws_sdk_iotfleetwise.types.state_template_association_identifiers

        out["state_templates_to_remove"] = (
            aws_sdk_iotfleetwise.types.state_template_association_identifiers.deserialize_aws_json_1_0(
                data["stateTemplatesToRemove"]
            )
        )
    if "stateTemplatesToUpdate" in data:
        import aws_sdk_iotfleetwise.types.state_template_associations

        out["state_templates_to_update"] = (
            aws_sdk_iotfleetwise.types.state_template_associations.deserialize_aws_json_1_0(
                data["stateTemplatesToUpdate"]
            )
        )
    return out
