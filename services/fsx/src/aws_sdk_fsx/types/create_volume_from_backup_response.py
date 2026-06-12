"""Generated from Smithy shape ``com.amazonaws.fsx#CreateVolumeFromBackupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.volume


class CreateVolumeFromBackupResponse(TypedDict):
    volume: NotRequired["aws_sdk_fsx.types.volume.Volume"]
    """<p>Returned after a successful <code>CreateVolumeFromBackup</code> API operation, describing the volume just created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVolumeFromBackupResponse) -> dict:
    out: dict = {}
    if "volume" in value:
        import aws_sdk_fsx.types.volume

        out["Volume"] = aws_sdk_fsx.types.volume.serialize_aws_json_1_1(value["volume"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVolumeFromBackupResponse:
    out: CreateVolumeFromBackupResponse = {}  # type: ignore[typeddict-item]
    if "Volume" in data:
        import aws_sdk_fsx.types.volume

        out["volume"] = aws_sdk_fsx.types.volume.deserialize_aws_json_1_1(
            data["Volume"]
        )
    return out
