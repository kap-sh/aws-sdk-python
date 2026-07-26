"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeCachediSCSIVolumesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.cachedi_scsi_volumes


class DescribeCachediSCSIVolumesOutput(TypedDict, closed=True):
    cachedi_scsi_volumes: NotRequired[
        "capo_storage_gateway.types.cachedi_scsi_volumes.CachediSCSIVolumes"
    ]
    """<p>An array of objects where each object contains metadata about one cached volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCachediSCSIVolumesOutput) -> dict:
    out: dict = {}
    if "cachedi_scsi_volumes" in value:
        import capo_storage_gateway.types.cachedi_scsi_volumes

        out["CachediSCSIVolumes"] = (
            capo_storage_gateway.types.cachedi_scsi_volumes.serialize_aws_json_1_1(
                value["cachedi_scsi_volumes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCachediSCSIVolumesOutput:
    out: DescribeCachediSCSIVolumesOutput = {}  # type: ignore[typeddict-item]
    if "CachediSCSIVolumes" in data:
        import capo_storage_gateway.types.cachedi_scsi_volumes

        out["cachedi_scsi_volumes"] = (
            capo_storage_gateway.types.cachedi_scsi_volumes.deserialize_aws_json_1_1(
                data["CachediSCSIVolumes"]
            )
        )
    return out
