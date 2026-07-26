"""Generated from Smithy shape ``com.amazonaws.storagegateway#StorediSCSIVolumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.storedi_scsi_volume

StorediSCSIVolumes: TypeAlias = list[
    "capo_storage_gateway.types.storedi_scsi_volume.StorediSCSIVolume"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorediSCSIVolumes) -> list:
    import capo_storage_gateway.types.storedi_scsi_volume

    out: list = []
    for item in value:
        out.append(
            capo_storage_gateway.types.storedi_scsi_volume.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StorediSCSIVolumes:
    import capo_storage_gateway.types.storedi_scsi_volume

    out: StorediSCSIVolumes = []
    for item in data:
        out.append(
            capo_storage_gateway.types.storedi_scsi_volume.deserialize_aws_json_1_1(
                item
            )
        )
    return out
