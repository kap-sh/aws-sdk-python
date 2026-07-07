"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateVolumeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.volume


class UpdateVolumeResponse(TypedDict, closed=True):
    volume: NotRequired["aws_sdk_fsx.types.volume.Volume"]
    """<p>A description of the volume just updated. Returned after a successful <code>UpdateVolume</code> API operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVolumeResponse) -> dict:
    out: dict = {}
    if "volume" in value:
        import aws_sdk_fsx.types.volume

        out["Volume"] = aws_sdk_fsx.types.volume.serialize_aws_json_1_1(value["volume"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVolumeResponse:
    out: UpdateVolumeResponse = {}  # type: ignore[typeddict-item]
    if "Volume" in data:
        import aws_sdk_fsx.types.volume

        out["volume"] = aws_sdk_fsx.types.volume.deserialize_aws_json_1_1(
            data["Volume"]
        )
    return out
