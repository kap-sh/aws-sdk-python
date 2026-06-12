"""Generated from Smithy shape ``com.amazonaws.storagegateway#CachediSCSIVolumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cachedi_scsi_volume

CachediSCSIVolumes: TypeAlias = list[
    "aws_sdk_storage_gateway.types.cachedi_scsi_volume.CachediSCSIVolume"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CachediSCSIVolumes) -> list:
    import aws_sdk_storage_gateway.types.cachedi_scsi_volume

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.cachedi_scsi_volume.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CachediSCSIVolumes:
    import aws_sdk_storage_gateway.types.cachedi_scsi_volume

    out: CachediSCSIVolumes = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.cachedi_scsi_volume.deserialize_aws_json_1_1(
                item
            )
        )
    return out
