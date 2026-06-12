"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.nielsen_pcm_to_id3_tagging_state


class NielsenConfiguration(TypedDict):
    distributor_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Enter the Distributor ID assigned to your organization by Nielsen."""
    nielsen_pcm_to_id3_tagging: NotRequired[
        "aws_sdk_medialive.types.nielsen_pcm_to_id3_tagging_state.NielsenPcmToId3TaggingState"
    ]
    """Enables Nielsen PCM to ID3 tagging"""


# --- restJson1 ser/de ---
def serialize_json(value: NielsenConfiguration) -> dict:
    out: dict = {}
    if "distributor_id" in value:
        out["distributorId"] = value["distributor_id"]
    if "nielsen_pcm_to_id3_tagging" in value:
        import aws_sdk_medialive.types.nielsen_pcm_to_id3_tagging_state

        out["nielsenPcmToId3Tagging"] = (
            aws_sdk_medialive.types.nielsen_pcm_to_id3_tagging_state.serialize_json(
                value["nielsen_pcm_to_id3_tagging"]
            )
        )
    return out


def deserialize_json(data: dict) -> NielsenConfiguration:
    out: NielsenConfiguration = {}  # type: ignore[typeddict-item]
    if "distributorId" in data:
        out["distributor_id"] = data["distributorId"]
    if "nielsenPcmToId3Tagging" in data:
        import aws_sdk_medialive.types.nielsen_pcm_to_id3_tagging_state

        out["nielsen_pcm_to_id3_tagging"] = (
            aws_sdk_medialive.types.nielsen_pcm_to_id3_tagging_state.deserialize_json(
                data["nielsenPcmToId3Tagging"]
            )
        )
    return out
