"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdConditioningConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.streaming_media_file_conditioning


class AdConditioningConfiguration(TypedDict):
    streaming_media_file_conditioning: "aws_sdk_mediatailor.types.streaming_media_file_conditioning.StreamingMediaFileConditioning"
    r"""<p>For ads that have media files with streaming delivery and supported file extensions, indicates what transcoding action MediaTailor takes when it first receives these ads from the ADS. <code>TRANSCODE</code> indicates that MediaTailor must transcode the ads. <code>NONE</code> indicates that you have already transcoded the ads outside of MediaTailor and don't need them transcoded as part of the ad insertion workflow. For more information about ad conditioning see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html\">Using preconditioned ads</a> in the Elemental MediaTailor user guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdConditioningConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mediatailor.types.streaming_media_file_conditioning

    out["StreamingMediaFileConditioning"] = (
        aws_sdk_mediatailor.types.streaming_media_file_conditioning.serialize_json(
            value["streaming_media_file_conditioning"]
        )
    )
    return out


def deserialize_json(data: dict) -> AdConditioningConfiguration:
    out: AdConditioningConfiguration = {}  # type: ignore[typeddict-item]
    if "StreamingMediaFileConditioning" in data:
        import aws_sdk_mediatailor.types.streaming_media_file_conditioning

        out["streaming_media_file_conditioning"] = (
            aws_sdk_mediatailor.types.streaming_media_file_conditioning.deserialize_json(
                data["StreamingMediaFileConditioning"]
            )
        )
    else:
        raise DeserializationError(
            "AdConditioningConfiguration.streaming_media_file_conditioning required"
        )
    return out
