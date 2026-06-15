"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetVehicleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.attributes_map
    import aws_sdk_iotfleetwise.types.state_template_associations
    import aws_sdk_iotfleetwise.types.timestamp
    import aws_sdk_iotfleetwise.types.vehicle_name


class GetVehicleResponse(TypedDict):
    vehicle_name: NotRequired["aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"]
    """<p>The ID of the vehicle.</p>"""
    arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p> The Amazon Resource Name (ARN) of the vehicle to retrieve information about. </p>"""
    model_manifest_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p> The ARN of a vehicle model (model manifest) associated with the vehicle. </p>"""
    decoder_manifest_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p> The ARN of a decoder manifest associated with the vehicle. </p>"""
    attributes: NotRequired["aws_sdk_iotfleetwise.types.attributes_map.attributesMap"]
    r"""<p>Static information about a vehicle in a key-value pair. For example:</p> <p> <code>\"engineType\"</code> : <code>\"1.3 L R2\"</code> </p>"""
    state_templates: NotRequired[
        "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
    ]
    """<p>State templates associated with the vehicle.</p>"""
    creation_time: NotRequired["aws_sdk_iotfleetwise.types.timestamp.timestamp"]
    """<p> The time the vehicle was created in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: NotRequired[
        "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    ]
    """<p> The time the vehicle was last updated in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVehicleResponse) -> dict:
    out: dict = {}
    if "vehicle_name" in value:
        out["vehicleName"] = value["vehicle_name"]
    if "arn" in value:
        out["arn"] = value["arn"]
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
    if "state_templates" in value:
        import aws_sdk_iotfleetwise.types.state_template_associations

        out["stateTemplates"] = (
            aws_sdk_iotfleetwise.types.state_template_associations.serialize_aws_json_1_0(
                value["state_templates"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creationTime"] = (
            aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["creation_time"]
            )
        )
    if "last_modification_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["lastModificationTime"] = (
            aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["last_modification_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVehicleResponse:
    out: GetVehicleResponse = {}  # type: ignore[typeddict-item]
    if "vehicleName" in data:
        out["vehicle_name"] = data["vehicleName"]
    if "arn" in data:
        out["arn"] = data["arn"]
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
    if "stateTemplates" in data:
        import aws_sdk_iotfleetwise.types.state_template_associations

        out["state_templates"] = (
            aws_sdk_iotfleetwise.types.state_template_associations.deserialize_aws_json_1_0(
                data["stateTemplates"]
            )
        )
    if "creationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creation_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    return out
