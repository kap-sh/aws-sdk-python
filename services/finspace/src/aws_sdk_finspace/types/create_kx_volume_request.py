"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.availability_zone_ids
    import aws_sdk_finspace.types.client_token
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.kx_az_mode
    import aws_sdk_finspace.types.kx_environment_id
    import aws_sdk_finspace.types.kx_nas1_configuration
    import aws_sdk_finspace.types.kx_volume_name
    import aws_sdk_finspace.types.kx_volume_type
    import aws_sdk_finspace.types.tag_map


class CreateKxVolumeRequest(TypedDict):
    client_token: NotRequired["aws_sdk_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>"""
    volume_type: "aws_sdk_finspace.types.kx_volume_type.KxVolumeType"
    """<p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. When you select <code>NAS_1</code> volume type, you must also provide <code>nas1Configuration</code>. </p>"""
    volume_name: "aws_sdk_finspace.types.kx_volume_name.KxVolumeName"
    """<p>A unique identifier for the volume.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p> A description of the volume. </p>"""
    nas1_configuration: NotRequired[
        "aws_sdk_finspace.types.kx_nas1_configuration.KxNAS1Configuration"
    ]
    """<p> Specifies the configuration for the Network attached storage (NAS_1) file system volume. This parameter is required when you choose <code>volumeType</code> as <i>NAS_1</i>.</p>"""
    az_mode: "aws_sdk_finspace.types.kx_az_mode.KxAzMode"
    """<p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>"""
    availability_zone_ids: (
        "aws_sdk_finspace.types.availability_zone_ids.AvailabilityZoneIds"
    )
    """<p>The identifier of the availability zones.</p>"""
    tags: NotRequired["aws_sdk_finspace.types.tag_map.TagMap"]
    """<p> A list of key-value pairs to label the volume. You can add up to 50 tags to a volume. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxVolumeRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_finspace.types.kx_volume_type

    out["volumeType"] = aws_sdk_finspace.types.kx_volume_type.serialize_json(
        value["volume_type"]
    )
    out["volumeName"] = value["volume_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "nas1_configuration" in value:
        import aws_sdk_finspace.types.kx_nas1_configuration

        out["nas1Configuration"] = (
            aws_sdk_finspace.types.kx_nas1_configuration.serialize_json(
                value["nas1_configuration"]
            )
        )
    import aws_sdk_finspace.types.kx_az_mode

    out["azMode"] = aws_sdk_finspace.types.kx_az_mode.serialize_json(value["az_mode"])
    import aws_sdk_finspace.types.availability_zone_ids

    out["availabilityZoneIds"] = (
        aws_sdk_finspace.types.availability_zone_ids.serialize_json(
            value["availability_zone_ids"]
        )
    )
    if "tags" in value:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateKxVolumeRequest:
    out: CreateKxVolumeRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "volumeType" in data:
        import aws_sdk_finspace.types.kx_volume_type

        out["volume_type"] = aws_sdk_finspace.types.kx_volume_type.deserialize_json(
            data["volumeType"]
        )
    else:
        raise DeserializationError("CreateKxVolumeRequest.volume_type required")
    if "volumeName" in data:
        out["volume_name"] = data["volumeName"]
    else:
        raise DeserializationError("CreateKxVolumeRequest.volume_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "nas1Configuration" in data:
        import aws_sdk_finspace.types.kx_nas1_configuration

        out["nas1_configuration"] = (
            aws_sdk_finspace.types.kx_nas1_configuration.deserialize_json(
                data["nas1Configuration"]
            )
        )
    if "azMode" in data:
        import aws_sdk_finspace.types.kx_az_mode

        out["az_mode"] = aws_sdk_finspace.types.kx_az_mode.deserialize_json(
            data["azMode"]
        )
    else:
        raise DeserializationError("CreateKxVolumeRequest.az_mode required")
    if "availabilityZoneIds" in data:
        import aws_sdk_finspace.types.availability_zone_ids

        out["availability_zone_ids"] = (
            aws_sdk_finspace.types.availability_zone_ids.deserialize_json(
                data["availabilityZoneIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateKxVolumeRequest.availability_zone_ids required"
        )
    if "tags" in data:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.deserialize_json(data["tags"])
    return out
